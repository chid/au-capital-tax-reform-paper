"""Deterministic policy microsimulations, policy snapshot 11 November 2026.

Run: python3 output/research/cgt_policy_model.py
All amounts AUD; no external packages. Results go beside this script.
This is a comparative-static model, not an individual tax-return calculator.
"""

import json
from pathlib import Path


THRESHOLDS = (0, 18_200, 45_000, 135_000, 190_000)
BASE_RATES = (0, .14, .30, .37, .45)
SPENDER_RATES = (0, .13, .275, .345, .425)


def basic_tax(income, spender=False):
    """Progressive basic tax, before levy and offsets. Labour >= $45k only."""
    rates = SPENDER_RATES if spender else BASE_RATES
    upper = (*THRESHOLDS[1:], float('inf'))
    return sum(max(0, min(income, hi) - lo) * rate
               for lo, hi, rate in zip(THRESHOLDS, upper, rates))


def tax(income, spender=False):
    # All principal cases exceed Medicare reduction thresholds and LITO limits.
    return basic_tax(income, spender) + .02 * income


def wage_tax(wage, regime):
    if regime == 'budget':
        return tax(wage - 1_000) - 250
    return tax(wage, regime == 'spender')


def gain_tax(wage, included_gain, regime):
    base = wage - (1_000 if regime == 'budget' else 0)
    extra_basic = basic_tax(base + included_gain, regime == 'spender') - basic_tax(base, regime == 'spender')
    if regime == 'budget':
        extra_basic = max(extra_basic, .30 * included_gain)
    return extra_basic + .02 * included_gain


def npv(flows, rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(flows))


def irr(flows):
    lo, hi = -.9, 1.
    assert npv(flows, lo) > 0 > npv(flows, hi)
    for _ in range(150):
        mid = (lo + hi) / 2
        if npv(flows, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def property_case():
    wage, loss, years, gain = 200_000, 15_000, 7, 400_000
    inflation = 1.025 ** years
    real_gain = 1_400_000 - 1_000_000 * inflation
    rows = {}
    for regime in ('status_quo', 'spender', 'budget'):
        wage_relief = wage_tax(wage, 'status_quo') - wage_tax(wage, regime)
        if regime == 'status_quo':
            annual_loss_relief = tax(wage) - tax(wage - loss)
            exit_tax = tax(wage - loss + .5 * gain) - tax(wage - loss)
            included_gain = .5 * gain
        else:
            annual_loss_relief = 0
            # White Paper does not settle pre/post discount ordering.
            # Main Spender case explicitly adopts the user's pre-discount rule.
            included_gain = .7 * (gain - years * loss) if regime == 'spender' else max(0, real_gain - years * loss)
            exit_tax = gain_tax(wage, included_gain, regime)
        annual_outlay = loss - annual_loss_relief
        flows = [-200_000] + [-annual_outlay] * years
        flows[-1] += 600_000 - exit_tax
        investment_tax = exit_tax - annual_loss_relief * years
        profit = sum(flows)
        rows[regime] = dict(
            wage_tax_without_investment=wage_tax(wage, regime),
            annual_wage_tax_relief=wage_relief,
            annual_rental_loss_tax_relief=annual_loss_relief,
            annual_investment_cash_shortfall=annual_outlay,
            annual_cash_shortfall_net_wage_relief=annual_outlay-wage_relief,
            included_gain=included_gain,
            incremental_exit_cgt=exit_tax,
            lifetime_net_investment_tax=investment_tax,
            lifetime_total_tax=years*wage_tax(wage,regime)+investment_tax,
            nominal_investment_profit=profit,
            profit_plus_uninvested_wage_tax_relief=profit+years*wage_relief,
            investment_irr=irr(flows),
            investment_npv_5pct=npv(flows,.05),
            investment_cash_flows=flows,
        )
    after_discount_gain = .7*gain-years*loss
    after_discount_tax = gain_tax(wage,after_discount_gain,'spender')
    # Qualifying new-build sensitivity under Budget: wage deduction allowed,
    # taxpayer chooses the smaller of discount and indexation liabilities.
    budget_base = wage-1_000
    newbuild_loss_relief = tax(budget_base)-tax(budget_base-loss)
    newbuild_discount_cgt = tax(budget_base-loss+.5*gain)-tax(budget_base-loss)
    newbuild_index_cgt = max(basic_tax(budget_base-loss+real_gain)-basic_tax(budget_base-loss), .30*real_gain)+.02*real_gain
    return dict(
        inflation_factor=inflation,
        indexed_cost_base=1_000_000*inflation,
        indexed_gain_before_rental_losses=real_gain,
        main=rows,
        spender_after_discount_loss_sensitivity=dict(
            included_gain=after_discount_gain,
            cgt=after_discount_tax,
            investment_profit=gain-years*loss-after_discount_tax,
            profit_plus_uninvested_wage_relief=gain-years*loss-after_discount_tax+years*rows['spender']['annual_wage_tax_relief'],
        ),
        budget_newbuild_sensitivity=dict(
            annual_loss_tax_relief=newbuild_loss_relief,
            discount_cgt=newbuild_discount_cgt,
            indexation_cgt=newbuild_index_cgt,
            investment_profit=gain-years*loss-min(newbuild_discount_cgt,newbuild_index_cgt)+years*newbuild_loss_relief,
        ),
    )


def deposit_case():
    wage, years = 95_000, 5
    living_expense = wage-wage_tax(wage,'status_quo')-10_000
    rows = {}
    for regime in ('status_quo','spender','budget'):
        wage_liability = wage_tax(wage,regime)
        annual_contribution = wage-wage_liability-living_expense
        interest_tax_rate = .295 if regime == 'spender' else .32
        balance, total_interest_tax = 0., 0.
        ledger=[]
        for year in range(1,years+1):
            interest = balance*.04
            interest_tax = interest*interest_tax_rate
            balance += interest-interest_tax+annual_contribution
            total_interest_tax += interest_tax
            ledger.append(dict(year=year,interest=interest,interest_tax=interest_tax,end_balance=balance))
        relief = wage_tax(wage,'status_quo')-wage_liability
        rows[regime]=dict(
            annual_wage_tax=wage_liability,
            annual_take_home_wage=wage-wage_liability,
            annual_wage_tax_relief=relief,
            five_year_wage_tax=years*wage_liability,
            five_year_uninvested_tax_relief=years*relief,
            annual_deposit_contribution=annual_contribution,
            five_year_interest_tax=total_interest_tax,
            five_year_total_tax=years*wage_liability+total_interest_tax,
            five_year_deposit_balance=balance,
            ledger=ledger,
        )
    return dict(annual_consumption=living_expense,main=rows)


def equity_case():
    principal,wage,years=100_000,150_000,15
    value=principal*1.08**years
    gain=value-principal
    rows={}
    for inflation in (.025,.05):
        factor=(1+inflation)**years
        real_gain=max(0,value-principal*factor)
        scenario={}
        for regime in ('status_quo','spender','budget'):
            included = gain*.5 if regime=='status_quo' else gain*.7 if regime=='spender' else real_gain
            cgt=gain_tax(wage,included,regime)
            terminal=value-cgt
            wage_relief=wage_tax(wage,'status_quo')-wage_tax(wage,regime)
            scenario[regime]=dict(
                indexed_cost_base=principal*factor if regime=='budget' else None,
                included_gain=included,
                incremental_exit_cgt=cgt,
                cgt_over_nominal_gain=cgt/gain,
                cgt_over_inflation_adjusted_gain=cgt/real_gain,
                terminal_investment_wealth=terminal,
                nominal_profit=terminal-principal,
                after_tax_nominal_cagr=(terminal/principal)**(1/years)-1,
                after_tax_real_cagr=(terminal/principal)**(1/years)/(1+inflation)-1,
                annual_wage_tax_relief=wage_relief,
                cumulative_wage_tax_relief=years*wage_relief,
                terminal_wealth_plus_uninvested_wage_relief=terminal+years*wage_relief,
                lifetime_total_tax=years*wage_tax(wage,regime)+cgt,
            )
        rows[str(inflation)]=scenario
    # Fixed MTR approximation from the supplied draft, corrected so the
    # Government does not receive Spender's personal income tax cuts.
    fixed={}
    for inflation in (.025,.05):
        real_gain=value-principal*(1+inflation)**years
        fixed[str(inflation)]={
            'status_quo':gain*.5*.39,
            'spender':gain*.7*.365,
            'budget':real_gain*.39,
        }
    return dict(principal=principal,wage=wage,years=years,nominal_terminal_value=value,nominal_gain=gain,main=rows,fixed_mtr_sensitivity=fixed)


def build():
    result=dict(
        assumptions=dict(
            snapshot_date='2026-11-11',
            start='2027-07-01',
            status_quo='Pre-2026-Budget counterfactual, including previously legislated 14% first bracket from 2027-28; no 2026 Budget standard deduction or WATO.',
            spender='Alternative package: 13/27.5/34.5/42.5% labour rates, 30% CGT discount, broad investment loss ring-fence. Labour >45k means investment minimum does not separately bind.',
            budget='14/30/37/45% basic rates, $1000 standard work deduction and $250 WATO; established residential acquisition after 1 July 2027; indexed gains net of rental losses; 30% basic-tax floor before 2% levy.',
            loss_order='Spender main case assumes losses deducted before discount; after-discount sensitivity supplied, as White Paper not legislative on ordering.',
            timing='Annual end-of-year cash flows, disposal and CGT paid at final year end.',
            exclusions='No HELP, Medicare surcharge, offsets other than WATO, transaction costs, depreciation, dividends, company tax, fees or superannuation; 2% flat Medicare appropriate to principal high-income cases.',
            limitations='Nominal incomes, brackets and parameters frozen; no behavioural adjustment or price response; not a revenue or welfare estimate. Equity is pure capital appreciation, not a typical distributing ETF.',
        ),
        scenario_a=property_case(),scenario_b=deposit_case(),scenario_c=equity_case(),
    )
    # Independent hand-calculation anchors for bracket crossing and cash flows.
    a=result['scenario_a']['main']
    assert abs(a['status_quo']['annual_rental_loss_tax_relief']-(10_000*.47+5_000*.39))<1e-8
    assert abs(a['status_quo']['incremental_exit_cgt']-(5_000*.39+195_000*.47))<1e-8
    assert abs(a['status_quo']['nominal_investment_profit']-247_950)<1e-8
    assert abs(a['spender']['incremental_exit_cgt']-91_892.5)<1e-8
    assert abs(result['scenario_b']['main']['spender']['annual_wage_tax_relief']-(26_800*.01+50_000*.025))<1e-8
    for row in a.values():
        assert abs(npv(row['investment_cash_flows'],row['investment_irr']))<1e-7
        assert abs(row['nominal_investment_profit']-(295_000-row['lifetime_net_investment_tax']))<1e-7
    return result


if __name__=='__main__':
    data=build()
    target=Path(__file__).with_name('cgt_policy_results.json')
    target.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
