# Chapter 1 — Ask what the data can represent

*Before you calculate a rate, locate the people and events that can enter it.*

Imagine a transit team tapes a reassuring number to its planning wall: “70% on time.” Look underneath the paper. Was each row a passenger, a recorded arrival, or a scheduled trip? A cancellation produces no arrival reading. If the spreadsheet quietly replaces it with zero delay, the headline becomes a reward for failing to run the bus. This is not a problem with percentages. It is a problem with what got to count.

After this chapter, write a population and unit statement, audit denominators and missing statuses, compare sampling with assignment, and redraw a sampling plan without promising what it cannot deliver.

## Define the unit before the measurement

The fictional analyst wants a planning statement about **all scheduled trips on Route H on weekdays next month, in two specified time windows**. One unit is a scheduled trip at its designated stop and date/time, not each boarding passenger. A trip's lateness in the toy data is the number of minutes after its scheduled arrival, with early/on-schedule arrivals assigned zero for this measure. This is not signed schedule deviation, route-wide performance, or a passenger's waiting time. A measurement is a rule, not merely a column with a plausible name.

The analyst's available twelve-row convenience snapshot [is here](../data/weekday_snapshot.csv). It covers two short windows on one day that the analysts were available to inspect. It neither randomly samples next month's service nor identifies passenger experiences. The scheduled trip list is a *frame*: it tells us which scheduled units are supposed to be available for study. The snapshot records statuses for 12 of those units. Only 10 have a measured delay. For this exercise define a late arrival as **more than six minutes late**; exactly six is within threshold. Define a separate outcome, *adverse planned-trip status*, as cancelled or late. An unobserved noncancelled trip has unknown late status.

| Window in snapshot | Planned | Recorded delay | Late among recorded | Cancelled | Sensor missing |
| --- | ---: | ---: | ---: | ---: | ---: |
| Peak | 8 | 6 | 3 | 1 | 1 |
| Off-peak | 4 | 4 | 0 | 0 | 0 |
| Combined | 12 | 10 | 3 | 1 | 1 |

The observed-trip late share is $3/10=30\%$. It is a description of the records that actually have a measurement under this definition. The 70% complement is at-or-within-threshold among those same 10, not a system-level success rate. The known adverse planned trips are the three late observed trips and the cancelled trip. One missed sensor reading could be late or not. The adverse share of these 12 planned trips is at least $4/12$ and at most $5/12$, about 33.3% to 41.7%. There is no probability model in that range. It is a bound from letting the one unknown case take either value. The sample was not random; calling the range a confidence interval would confuse a missing-record question with repeated sampling.

<!-- → [TABLE: separate sampling frame, observed dataset and complete cases; cancellation and sensor missing need different branches] -->

If someone averages the peak rate $3/6$ and off-peak rate $0/4$ as ordinary numbers, the output is 25%. If someone pools recorded trips, the output is 30%. Neither calculation is inherently malformed: the first gives each of two windows equal weight, while the second gives each recorded trip equal weight. Only the second answers the observed-trip question used above. The lesson is not “never average percentages.” It is “write what receives one vote.”

## Separate selection from measurement

Selection bias can arise because different target units have different and uncontrolled chances to appear. A phone survey only of riders on arriving vehicles may miss people who gave up after a cancellation. Coverage error means the frame does not span the intended population; a vendor feed can omit one operating company, even if it perfectly records its own buses. Nonresponse or missing measurements can occur after a unit is selected; a radio link may fail just when many late buses arrive together. Measurement error can arise even with complete records; a timestamp set by the reporting device instead of the door sensor answers a different timing question. Repeated records for the same late trip can inflate the apparent number of trips without adding a unit. These mechanisms can coexist. The [U.S. Census Bureau's survey methodology](https://www.census.gov/programs-surveys/sas/technical-documentation/methodology.html) distinguishes sampling and nonsampling errors in an actual survey setting.

A larger convenience sample only makes its own measurements less noisy under some conditions; it does not repair who is missing or redefine an ambiguous outcome. One improvement would be a probability sample from a complete schedule, with randomly selected dates/trips within each prespecified time window, documented selection probabilities, and a separate audit stream for missing and cancelled trips. If randomizing days rather than trips, account for trips on one day sharing conditions and not behaving like independent draws. Deliberate oversampling of a rare period may be sensible, but population summaries then need an explicit design or weights. This compact book does not give a generic weighting fix for records lost on bad days.

A random **sample** concerns who is selected and can support a design-based inference to a frame under appropriate measurement and response conditions. Random **assignment** concerns who receives a treatment. For example, randomly assigning a schedule notification within each selected planning day can help isolate its causal effect in the enrolled units, provided the design and assumptions hold. It does not automatically generalize to all routes and all times. A citywide random survey of riders can describe their satisfaction, but if riders choose their own service, the survey alone does not isolate an intervention's effect.

## A defendable memo, not a polished wrong answer

A hypothetical assistant says: “90% of buses were measured, so the missing trips cannot change the recommendation.” First check the numbers: 10 out of 12 is about 83.3%, not 90%. Then check the claim: even a correctly calculated coverage share does not supply the outcomes of missing units or support next month's forecasts. A suitable memo says **what was counted**, **why it falls short**, and **what evidence to request next**. In this case: “Three of ten measured arrivals exceeded six minutes; counting cancellation as adverse leaves four to five adverse trips among the twelve scheduled in this snapshot. Before a network-wide conclusion, record representative days and audit sensor loss by time and running conditions.”

## Exercises

- **Warm-up, unit:** Write a different population statement for passenger delay. What denominator and measurement would you need?
- **Warm-up, threshold:** Classify measured delays of 6 and 7 minutes, a cancellation, and a missing sensor record for both outcomes.
- **Application, weights:** If the window counts change to 2/5 and 2/10, give the per-window-average and recorded-trip pooled rates and the questions they answer.
- **Application, bound:** Add two scheduled trips with unknown delay and one known on-time trip. Recompute only the planned-status bounds before interpreting them.
- **Synthesis, design:** Specify a feasible sampling scheme and a separate assignment scheme to test a new notification. State an assumption each design needs.
- **Challenge, missingness:** The reporting system keeps only each bus's most delayed stop. Explain why extra buses under that rule do not fix a stop-level target.

You can now audit a percentage before deciding whether it deserves a summary. The next chapter takes the numbers we actually observed and asks which summaries preserve the features that matter.

[Back to the contents](../README.md)
