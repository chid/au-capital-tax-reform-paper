# Rebalancing Capital and Labour: Capital Gains Tax, Negative Gearing and Australian Tax Reform

**JEL:** H21, H24, H31, R38  
**Keywords:** capital gains tax; negative gearing; tax neutrality; housing; lifecycle incidence

## Abstract

This paper compares the pre-2026 Budget personal tax framework, Allegra Spender's Personal Tax White Paper and the 2026-27 Budget CGT and negative-gearing package. Three deterministic microsimulations examine a leveraged established residential property, a wage earner saving a deposit and a long-term growth-equity investment. For the specified property investment, nominal investment profit is $247,950 under the baseline, $203,108 under Spender's model and $245,032 under the Budget model. The latter result reflects CPI indexation and the ability to use quarantined rental losses against residential capital gains. Spender's labour tax cuts partly offset the investment-tax increase and produce the largest deposit accumulation for the prospective first-home buyer. For equities, the ranking changes with inflation: indexation taxes measured real gains, while a flat discount is an imperfect inflation proxy. Results depend on progressive brackets, loss-offset ordering and transition assumptions. These scenarios do not identify aggregate welfare, revenue or housing-market effects.

## 1. Policy context

The comparison distinguishes (i) a counterfactual continuation of the pre-Budget framework, (ii) Spender's 2026 White Paper proposal, and (iii) the Government's enacted core Budget changes beginning in 2027-28. “Status Quo” is therefore a counterfactual for future investments, not a claim that the 50% discount remains the general legislated treatment indefinitely.

The baseline offers a 50% discount on eligible individual capital gains held at least 12 months and generally permits rental losses against wages. Spender proposes a 30% discount, investment-loss ring-fencing to non-labour income, lower wage tax rates and a 27.5% minimum rate on investment income. The Government replaces the general discount with cost-base indexation plus a minimum 30% basic tax on eligible real gains. Affected established residential-property losses are quarantined to residential income and gains; new builds have preferential treatment, and properties held before the announcement are grandfathered.

The model uses 2027-28 onward baseline rates of 14%, 30%, 37% and 45%, with a tax-free threshold of $18,200. Spender's proposed basic rates are 13% for $18,201-$45,000, 27.5% for $45,001-$135,000, 34.5% for $135,001-$190,000 and 42.5% above $190,000. A 2% Medicare levy is added. Government scenarios include the $250 Working Australians Tax Offset and a $1,000 standard work deduction.

## 2. Theoretical framework

Let `m` be the marginal tax rate including Medicare and `d` the CGT discount. Tax on an incremental eligible nominal gain is `(1-d)m`. If a rental loss is immediately deducted at rate `m`, the deduction-gain wedge is `m-(1-d)m=dm`. At the top rate, the baseline wedge is 23.5 percentage points (47% versus 23.5%). Under Spender it is 13.35 points (44.5% versus 31.15%), a mechanical reduction of 43.2%, before considering ring-fencing. This wedge is not a risk-free arbitrage: borrowing costs, uncertainty and non-recoverable losses remain.

Quarantining can defer a deduction and reduce its present value. Its value depends on recovery timing, the future marginal tax rate and whether losses offset gains before or after the CGT discount. For purchase price `P0`, sale price `PH` and cumulative CPI factor `I`, the indexed gain is `max(0, PH-P0*I)`. A fixed discount equals indexation only for a particular combination of inflation and nominal return. Indexation better measures real gains but does not alone create neutrality across interest, dividends, borrowing costs, losses and corporate income.

Realisation-based CGT affects sale timing: investors may defer sale to postpone liability or reach a lower-rate year. A minimum tax reduces the retirement-rate incentive but does not remove the general deferral benefit. Intergenerational incidence depends on asset ownership, labour income and transition rules. Younger workers may benefit from wage cuts, while younger leveraged investors may face higher cash requirements.

## 3. Microsimulation method

All amounts are nominal AUD. Wages, thresholds and rates are fixed. Cash flows occur annually at year-end; disposal tax is paid in the final year. The model excludes transaction costs, depreciation, HELP, Medicare surcharge, dividends and behavioural responses. Annual CPI compounding approximates statutory indexation. The equity case is pure capital appreciation, not a typical distributing ETF. The calculation code and full outputs are in `model/`.

### 3.1 Scenario A: leveraged residential property

The investor earns $200,000, buys an established $1,000,000 property with $800,000 debt at 6%, receives $40,000 annual rent and incurs $55,000 interest and operating costs. Annual net loss is $15,000. After seven years the property sells for $1,400,000: nominal gain $400,000 and cumulative rental losses $105,000.

Under the baseline, deducting $15,000 crosses a tax threshold: `$10,000*47% + $5,000*39% = $6,650` annual relief. Annual after-tax holding shortfall is $8,350. In the sale year, the $200,000 discounted gain adds $93,600 tax because $5,000 falls in the 39% band and $195,000 in the 47% band. Lifecycle investment tax is $93,600 less seven annual deductions, or $47,050. Nominal investment profit is **$247,950**.

Under Spender, the investor cannot offset losses against wages and has no other investment income. The main case applies losses before the discount, consistent with the supplied draft's convention: `(400,000-105,000)*70%=$206,500` included gain. At 44.5%, exit CGT is $91,892.50 and investment profit is **$203,107.50**. Wage tax falls by $4,143 annually, or $29,001 over seven years if retained without interest. If losses instead offset the discounted gain after discounting, included gain is $175,000, CGT $77,875 and profit $217,125. The White Paper does not settle statutory loss ordering; this is a material design sensitivity.

Under the Government package, seven-year CPI at 2.5% is 18.87%, indexed cost base is $1,188,686, and real gain is $211,314. After $105,000 quarantined rental losses, taxable gain is $106,314. Ordinary marginal income tax exceeds the 30% minimum. Including Medicare, exit tax is $49,968 and investment profit is **$245,032**. A qualifying new-build sensitivity permits wage deductions and a choice of CGT method; under the supplied assumptions it yields about $247,470 investment profit.

| Scenario A outcome | Status Quo | Spender | Government |
|---|---:|---:|---:|
| Annual rental-loss tax benefit | $6,650 | $0 | $0 |
| Annual investment cash shortfall | $8,350 | $15,000 | $15,000 |
| Exit CGT | $93,600 | $91,893 | $49,968 |
| Lifecycle net investment tax | $47,050 | $91,893 | $49,968 |
| Investment profit | $247,950 | $203,108 | $245,032 |
| Investment IRR | 11.33% | 9.16% | 10.61% |
| NPV at 5% | $111,573 | $74,307 | $104,102 |
| Annual wage-tax relief | $0 | $4,143 | $720 |

### 3.2 Scenario B: worker saving a deposit

A worker earns $95,000, owns no capital assets and saves $10,000 annually under the baseline. Baseline tax including Medicare is $20,652. Spender tax is $19,134 (saving $1,518); Government tax after the standard deduction and WATO is $20,082 (saving $570). Consumption is fixed at $64,348, permitting annual deposit contributions of $10,000, $11,518 and $10,570, respectively. Savings earn 4% before tax, taxed at 32% under Status Quo/Government and 29.5% under Spender.

| Five-year outcome | Status Quo | Spender | Government |
|---|---:|---:|---:|
| Annual wage tax | $20,652 | $19,134 | $20,082 |
| Annual deposit contribution | $10,000 | $11,518 | $10,570 |
| Wage tax over five years | $103,260 | $95,670 | $100,410 |
| Deposit balance | $52,795 | $60,931 | $55,804 |
| Additional balance vs baseline | — | $8,136 | $3,009 |

No house-price or rent effect is imposed. Those require a market model and supply and demand elasticities.

### 3.3 Scenario C: growth-equity accumulator

A $100,000 equity investment compounds at 8% for 15 years to $317,217, a nominal gain of $217,217. The investor earns $150,000 wages, so progressive rates apply. At 2.5% CPI, indexed cost base is $144,830 and real gain $172,387. At 5% CPI, indexed cost base is $207,893 and real gain $109,324. The Government minimum does not bind because ordinary basic tax on these gains exceeds 30%.

| CPI | Regime | Exit CGT | Terminal wealth | After-tax nominal CAGR | After-tax real CAGR |
|---:|---|---:|---:|---:|---:|
| 2.5% | Status Quo | $47,846 | $269,371 | 6.83% | 4.22% |
| 2.5% | Spender | $64,463 | $252,754 | 6.38% | 3.78% |
| 2.5% | Government | $77,742 | $239,475 | 5.99% | 3.41% |
| 5.0% | Status Quo | $47,846 | $269,371 | 6.83% | 1.74% |
| 5.0% | Spender | $64,463 | $252,754 | 6.38% | 1.31% |
| 5.0% | Government | $48,102 | $269,115 | 6.82% | 1.74% |

Wage-tax relief is separate from investment returns. At $150,000 wages, Spender saves $2,893 per year and Government $640. Retained without interest for 15 years, this adds $43,395 and $9,600. Taxed distributions would change timing and composition; this is not a complete ETF tax model.

## 4. Comparative matrix

| Dimension | Status Quo | Spender | Government |
|---|---|---|---|
| Eligible CGT | 50% nominal discount | 30% nominal discount | CPI-indexed cost base |
| Investment losses | Generally offset wages | Ring-fenced to investment income | Affected established residential losses quarantined to residential income/gains |
| Top labour rate incl. Medicare | 47% | 44.5% | 47% |
| Top-rate CGT marginal rate on nominal gain | 23.5% | 31.15% | Inflation-dependent; 30% minimum basic tax on eligible real gain |
| Wage relief in Scenario B | None | $1,518/year | $570/year |
| Scenario A investment profit | $247,950 | $203,108* | $245,032 |
| Inflation recognition | Approximate, variable | Approximate, variable | Explicit indexation |
| Administration | Existing cost-base and loss records | Loss balances and income classification | Indexation, transition and residential classification |
| Lock-in | Realisation deferral remains | Remains; higher gain tax can strengthen it | Remains; minimum reduces low-income-year timing advantage |
| Equity and neutrality | Preferential gains and geared-loss treatment | Narrows labour/asset gap; retains discounts | Better real-gain measurement; classifications remain |

*Spender result assumes losses applied before discount. These examples do not estimate population-average effective marginal rates or compliance deadweight.

## 5. Macroeconomic and welfare implications

Tax payments are transfers; excess burden arises from induced changes in labour, saving, financing, investment and realisation. Spender's wage cuts can improve work incentives while higher asset taxation affects saving and portfolio choices. The net welfare effect requires elasticities and distributional weights and cannot be established from these microsimulations.

Reform can reduce the tax advantage of leveraged investment in existing housing. Rent effects depend on tenure switching, rental demand and new-construction elasticity. New-build concessions may direct investment toward added supply, although benefits can be capitalised into scarce land. Treasury's Budget modelling projected about 75,000 additional owner-occupiers over a decade, roughly 35,000 fewer dwellings than the no-reform counterfactual and a small rent increase. These are model results, not observed outcomes. Grattan's analysis of a different 25% discount proposal also projected modest supply and rent effects; neither identifies Spender's full package.

Indexation measures real gains more directly but entails incremental calculation and transition costs. A fixed discount is simpler but can over- or under-compensate for inflation. Ring-fencing also requires loss records and clear classification rules. Compliance burden should be measured rather than presumed negligible or severe.

Post-implementation evaluation should use linked tax, property, rent and construction data to measure leverage, holding periods, first-home ownership, rents and completions. Policy cut-offs can aid identification, but anticipation, asset selection and concurrent supply measures complicate causal estimates.

## 6. Conclusion and recommendations

Spender's proposal links lower labour taxation to narrower investment concessions and a simpler CGT formula. The Government's indexed base measures inflation-adjusted gains more directly and treats established residential losses differently from new-build losses. Neither dominates across all examples: outcomes vary with inflation, leverage, asset appreciation and loss timing.

Policy design should specify loss ordering; publish integrated distributional and revenue costings; assess inflation treatment across income, expenses and losses; coordinate tax reform with housing-supply policy; and commit to independent evaluation of behavioural and administrative effects. The choice between a fixed discount and indexation is a choice among neutrality, simplicity, revenue, distribution and transition costs.

## References and policy sources

- Allegra Spender, *Personal Tax White Paper* (March 2026), https://www.allegraspender.com.au/tax
- Australian Treasury, *Budget 2026-27 Tax Reform*, https://treasury.gov.au/policy-topics/taxation/budget2026-27
- Australian Treasury, *Budget Paper No. 1, 2026-27*, https://budget.gov.au/content/bp1/download/bp1_2026-27.pdf
- *Treasury Laws Amendment (Tax Reform No. 1) Act 2026*, https://www.legislation.gov.au/C2026A00049/latest
- Henry, K. (2009), “Towards a better taxation of savings,” Australian Treasury.
- Coates, B., Moloney, J. and Sathanapally, A. (2025), “Reforming the Capital Gains Tax discount,” Grattan Institute.
- Dwyer, E. and Garvin, N. (2026), “How many housing investors pay more tax under the reforms?”, e61 Research Note.
- Slemrod, J. (1978), “The Lock-In Effect of the Capital Gains Tax: Some Time Series Evidence,” NBER Working Paper 257.
