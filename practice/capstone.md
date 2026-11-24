# Unaided capstone — Does the trial routing version deserve a rollout?

*Give a decision record, not a number dressed up as a decision.*

The [sixteen scheduled trips](../data/capstone_arrivals.csv) are fictional. They describe two selected windows on a single day. The analyst did not randomly sample the day or randomly assign the routing version. All early trips used the standard version; all late-window trips used the trial. Here “late window” labels a clock period, not a trip's delay. Lateness is nonnegative minutes after the scheduled arrival; exactly six does not count as a late arrival. The load index, an ordinal toy measure 0 to 4 treated as evenly spaced only for this exercise, is recorded on observed arrivals. A cancelled trip did not arrive; a sensor-missing trip ran but has unknown lateness. Do not recode either as zero. No patient, employee, vendor, or real transit data belong in this activity.

## Worksheet to fill before you consult any assistant

1. **Name the target.** Write the actual 16-trip population for this packet, then contrast it with a decision target of all trips in the next month. Describe the event unit, load measure and two metrics: late among observed and adverse (late or cancelled) among scheduled.
2. **Reconcile data.** On separate rows record scheduled, observed, late observed, cancelled, and sensor missing by window. Give a pooled late-observed fraction and an adverse-scheduled lower and upper bound. Mark the unknown outcome's two possible cases and explain why the bounds are not confidence limits.
3. **Display variation.** Choose equal bin widths and list edges and boundary rule before plotting. Give measured-only median and mean for each window with the row counts. Independently verify one bin from the CSV. Describe what changes when the value 20 is hypothetically replaced by 10; keep the original observation and do not label it erroneous by default.
4. **Name the comparison.** Fit a simple pooled least-squares model of observed lateness on load index. Verify one residual with original units and explain which group differences a pooled line might absorb. Name an extrapolation you will not make. If you choose not to fit in a short run, write the required variables, assumptions and one residual check rather than inventing coefficients.
5. **Ask for better evidence.** State one design for estimating time-window performance and one design to test a routing change. For the second, explain why a p-value computed by blindly shuffling the two version labels here would not be a valid randomized-assignment result. Note what outcomes you would include and declare a minimum practically important difference.
6. **Write a short release memo.** Supply a checked numerical headline and one limited recommendation about what can be measured next. Distinguish measured observations, unrecorded outcomes, sampling variation and unsupported causal claims. Include a reproducible worksheet or show enough calculations to rerun by hand.

## Transfer after the first attempt

An unseen packet adds a third date. The load meter resets midafternoon, the new delay was logged only for arrivals, and a dashboard says the routing change reduced average delay by 1.2 minutes. Explain which observations you would separate or drop from the comparison and why; specify what comparison was never made. Then solve a separate boundary update: one originally sensor-missing trip in the 16-trip exercise is verified on time. Indicate precisely which denominators, point estimates and bounds can change. Do not rewrite the original result without noting this updated record.

## Review

Score 0–2 on each: declared unit and denominator; exact check against original data; method and assumption fit; bounded interpretation; independent unseen-case defense. An accurate denominator paired with an unsupported claim of a treatment effect still needs revision. For optional AI critique after completing the worksheet, show only the synthetic packet plus your draft memo. Ask it to point to one calculation or causal inference that would fail. Verify the objection from the CSV or model yourself and note what changed. It is fine to keep a correct answer.

[Back to the contents](../README.md)
