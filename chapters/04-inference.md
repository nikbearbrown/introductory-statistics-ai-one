# Chapter 4 — Estimate and test with uncertainty

*An interval describes a method's coverage. A test asks how surprising a result is under a promise.*

Suppose a made-up service agreement uses six minutes as a fixed reference for average signed schedule error. The quality team sees five independent measurements and asks, “How uncertain is our mean?” Another team runs a small matched-day randomized trial and asks, “Would this result be unusual if swapping the assigned procedure changed nothing?” These are related questions about evidence, not interchangeable vocabulary for a verdict.

After this chapter, calculate a one-sample confidence interval, audit the assumptions behind it, compute a tiny two-sided randomization probability, and get effect size, significance and a decision into separate sentences.

## Build an interval for the parameter actually named

For a worked case, suppose five recorded **signed** deviations in minutes, positive for late and negative for early, are a faithful independent sample from an approximately normal process. Assume exactly normal draws if interpreting the procedure's nominal coverage as exact. These values are 2, 3, 4, 5 and 6. They are not the convenience snapshot or the clamp-at-zero delays from Chapter 1. The target $\mu$ is the model's mean deviation, not each trip's measurement or the next single deviation. If trips share a cause or selected estimates omit late observations, the model needs reconsideration regardless of how well the five points fit a dot plot.

The sample mean is 4. Squared deviations from 4 sum to $4+1+0+1+4=10$. Sample variance is $10/4=2.5$ and the estimated standard error is $s/\sqrt5=\sqrt{2.5/5}=\sqrt{0.5}\approx0.7071$ minutes. It measures uncertainty of the mean under the model, not the spread of an individual trip. Under independent normal sampling with unknown variance, the pivot $(\bar X-\mu)/(S/\sqrt n)$ follows Student's t with $n-1$ degrees of freedom. For five observations the two-sided 95% cutoff at the 97.5th percentile is about 2.7764, not 1.96. Inserting it gives:

$$4\pm 2.7764\sqrt{0.5}\approx[2.037,5.963]\text{ minutes}.$$

Under the ideal model, repeatedly drawing samples this way and computing the interval this way covers the fixed true mean in 95% of repetitions. Once you have the data and a fixed interval, this frequentist statement is not “there is a 95% posterior probability that this mean is within this interval.” It is also not “95% of trips land between those limits.” A prediction interval for a future individual uses a different distribution and uncertainty. The [NIST handbook on confidence limits for a mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) derives the interval and its connection to a one-sample test.

If the null asks whether the mean is exactly the fixed benchmark 6, the test statistic is $(4-6)/0.7071\approx-2.828$. Its absolute value exceeds 2.7764, so the specified two-sided test rejects at level 0.05 under the stated assumptions. This agrees with the unrounded interval excluding 6. If 6 was itself estimated from a separate noisy sample, a one-sample procedure treating it as known would discard uncertainty; an independent-group difference method then needs both group errors. If two readings belong to the same day, model day-level paired differences rather than automatically saying there are twice as many independent units. If the five readings were known to be rounded estimates from heavily correlated trip clusters, a good result is not a narrower decimal: it is a redesigned comparison.

The point estimate is a difference of −2 minutes from benchmark. The data and ideal model are compatible with a range of values, including values less than one minute below benchmark. A test of equality to 6 does not confirm a reduction of at least one minute; the upper limit is about 5.963, not 5.0 or less. The operational threshold tells you a decision criterion; the evidence tells you how well you met it. Do not conflate the two because a number crossed a significance cutoff.

## Count a different null that does not need a t curve

Imagine five distinct blocks of two comparable fictional operations. In each block, one operation receives a revised dispatch checklist, selected by a fair independent assignment swap; the other receives the standard checklist. The outcome and analysis were chosen in advance. Assume no interference and a sharp null of no effect on any operation. Under that null, swapping labels within a block reverses the sign of the observed standard-minus-revised difference without changing its magnitude. The five block differences in minutes are $1,2,2,3,4$. Average improvement is $12/5=2.4$ minutes in the observed arrangement.

Use the absolute sum as the test statistic. Every independent sign choice is equally likely under the design, so there are $2^5=32$ assignments to enumerate. Sum of absolute magnitudes is 12. Exactly two assignments reach absolute sum 12: all plus and all minus. None can exceed it. The two-sided probability of a statistic **at least** as extreme as observed under this sharp null and assignment is $2/32=0.0625$. Retain ties at the boundary. If one pair had a zero difference, changing its sign would give the same statistic but still a distinct assignment; probabilities should be over assignments, not unique statistic values.

This p-value is not the chance the checklist has no effect. It is not a measurement of how many minutes it saves, and not the probable improvement on an unobserved route. The design needs the swaps to have actually been randomized in those blocks; performing the same enumeration after observers chose which units received the change cannot retroactively create assignment. A p-value above 0.05 does not establish equivalence or make the observed difference zero. The study is small and this exact test has coarse resolution. As a separate introductory check, for 8 successes among 10 independent Bernoulli trials under a fixed $p=1/2$ null, the count-based two-sided tail at least three away from 5 has $2(\binom{10}{8}+\binom{10}{9}+\binom{10}{10})/2^{10}=7/64$. That calculation needs a different sampling model and cannot be reused for the clustered records in Chapter 1.

Type I error means rejecting a true null. A level controls its probability under the declared test and model when the null holds, not the error rate among all reported findings. Type II error means failing to reject under a specified false alternative. Power, one minus Type II error probability at that alternative, generally depends on effect, variation, design and sample size. Looking repeatedly until one p-value falls below a chosen threshold can alter the intended error guarantee if the test did not account for that plan. The [American Statistical Association's statement on p-values](https://doi.org/10.1080/00031305.2016.1154108) gives primary guidance on these interpretation limits.

## Exercises

- **Warm-up, quantile:** Explain why using 1.96 instead of 2.7764 here would make the displayed interval shorter but not make the study more precise.
- **Warm-up, hypothesis:** State the nulls separately for benchmark estimation and the block-swap example.
- **Application, interpretation:** Rewrite “there is a 95% chance the next trip is within 2.037 to 5.963.”
- **Application, enumeration:** For four positive paired differences, calculate the smallest possible two-sided p-value with the same sign-flip rule. State why a small effect can have a small p-value in a different design.
- **Synthesis, decision:** Pick a minimum meaningful reduction and compare it with a hypothetical interval that excludes zero but includes effects smaller than that reduction.
- **Challenge, method choice:** Choose a method for a new two-group study with randomized weather blocks and within-day dependence; name the correct unit of assignment and what existing formulas cannot be reused.

You can now justify what an interval covers over repeats and what a null calculation measures. The next chapter adds a predictor, which introduces a new temptation: to mistake fit for explanation.

[Back to the contents](../README.md)
