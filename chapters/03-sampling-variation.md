# Chapter 3 — Use sampling variation

*The distribution of observations and the distribution of their average are not the same thing.*

Imagine a jar with three equally likely synthetic delay cards: 2, 6 and 10 minutes. A draw can never show 4. An average of two draws can. Something moved when we switched from a reading to a statistic. If you only remember the slogan of the central limit theorem, it is easy to say the jar itself is somehow becoming normal. Open the machinery instead.

By the end, enumerate a small sampling distribution, distinguish with- and without-replacement experiments, check a simulation against an exact spread, and say which assumptions make a square-root rule useful.

## Count experiments, not distinct-looking outcomes

A random variable is a rule assigning a number to each outcome of a random experiment. One draw $X$ is uniform over the three labeled cards. Its expectation is $(2+6+10)/3=6$ minutes. Its variance $\sigma^2$ is the average of squared differences from 6: $(16+0+16)/3=32/3$ squared minutes. These are population quantities of a fully specified toy law, not estimates from three recorded trips. A probability mass assigns a probability to a discrete value. The masses add to one; expect a table to identify where each count came from.

Return the first card before drawing independently again. Each of nine ordered draw sequences has probability $1/9$. The outcome (2,6) and the outcome (6,2) are different sequences that yield the same mean; counting each *mean value* as equally probable is wrong. Here is the full distribution for the mean $\bar X$:

| Mean, minutes | 2 | 4 | 6 | 8 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Count out of 9 | 1 | 2 | 3 | 2 | 1 |

The expectation of the sampling distribution is 6. Its variance is $(16+2\cdot4+3\cdot0+2\cdot4+16)/9=16/3$ squared minutes. For example, “mean at least 8” has probability $3/9$, not the probability of drawing a single 8, which is zero. An expectation need not be a possible outcome for a particular experiment; it names a weighted mean of outcomes. Here it happens to be possible.

Now do not return the first card. Equally likely two-card subsets are $\{2,6\}$, $\{2,10\}$ and $\{6,10\}$. Their means 4, 6 and 8 have masses $1/3$ each. Expectation is still 6; variance is $(4+0+4)/3=8/3$. Observing 2 first has altered the possible second draws; the draws are not independent. Independence means knowing one outcome does not change the probabilities of the other in the model. Mutually exclusive events cannot both occur; two positive-probability mutually exclusive events are therefore not independent. In a single draw, “2” and “10” cannot both happen; across independent draws with replacement, one draw being 2 gives no update about the next draw being 10.

## Why the standard error can shrink

For $n$ independent draws with a common mean $\mu$ and finite variance $\sigma^2$, the sample mean has expectation $\mu$. Each observation contributes $1/n$ of the sum. Center each observation by subtracting $\mu$; expand the square of the centered sum. The expected cross-products are zero under independence because each factor has mean zero. The remaining $n$ terms each contribute $\sigma^2$, and dividing the sum by $n^2$ gives:

$$\operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad \operatorname{SD}(\bar X)=\frac{\sigma}{\sqrt n}.$$

That standard deviation of the statistic across repeated samples is a *standard error*. It is not the standard deviation of the original delay measurements. Keeping sample size at one gives $\sqrt{32/3}\approx3.27$ minutes; taking the mean of four independent cards gives $\sqrt{8/3}\approx1.63$ minutes. Four times as many independent observations halves the standard error in this model, not the original variability and not coverage bias. If delays share a day-level cause, the cross-products may be positive; then pretending you have $n$ independent trips can shrink an uncertainty estimate on paper while leaving the actual evidence weak.

Without replacement from a finite population of size $N>1$, a simple random subset of size $n$ has variance $\sigma^2/n$ times $(N-n)/(N-1)$, when $\sigma^2$ uses population denominator $N$. In our two-card case the correction ratio is $(3-2)/(3-1)=1/2$. If you draw all three cards without replacement, the mean is 6 every time. That eliminates sampling variation for this jar, not measurement error or the difference between the jar and a city's network. The exact table above shows why a design-specific correction should not be memorized as a universal number.

## A simulation can check the setup

[The lab](../lab/check_examples.py) repeats 4,000 synthetic samples for each of two values of $n$ in the with-replacement model. It uses a local seeded pseudo-random generator and computes the standard deviation of the simulated sample means. On the checked run the spreads are about 3.27 and 1.64 minutes for $n=1$ and $n=4$. Results need not equal the exact answers, because simulation itself uses finitely many trials. A seed controls a program run on a known setup; it is not a proof of independence and not a warranty of identical pseudo-random results across all programs and versions. Do not use with-replacement code for a without-replacement claim.

The classical central limit theorem says that, for independent identically distributed observations with finite positive variance, the standardized mean $\sqrt n(\bar X-\mu)/\sigma$ approaches a standard normal law in distribution as $n$ grows. This normal limit refers to the centered and scaled mean, not the original observation. No universal sample-size cutoff guarantees an accurate normal approximation for all distributions and all tail questions. Small $n$ and highly skewed observations can make it quite poor. A continuous model assigns probability to intervals as area under its density; an exact point has probability zero in that model. The three-card model and data rounded to recorded integer minutes do not have that property. [NIST's probability distribution handbook](https://itl.nist.gov/div898/handbook/eda/section3/eda36.htm) gives further context for choosing and checking models.

Before you compute an interval, say which random experiment you are imagining repeating. If that sentence changes, the law of the estimator may change with it even if the arithmetic inside each sample looks the same.

## Exercises

- **Warm-up, enumeration:** Write the nine ordered draw sequences with their mean, then obtain the probability of mean strictly greater than 6.
- **Warm-up, design:** Compute with- and without-replacement variance for a sample of all three cards; explain the difference without using a slogan.
- **Application, spread:** What sample sizes are needed to halve or quarter the standard error in the independent model? Name what does not improve.
- **Application, simulation:** Compare $n=1,4,9$ with two different seeds. Prewrite the exact benchmarks and an acceptable comparison rule.
- **Synthesis, assumptions:** If 20 trips come from the same day and all have a shared snow shock, state which term in the variance derivation needs revisiting.
- **Challenge, communication:** Write a rebuttal to “we took 30 convenience measurements, so they are normal and representative.” Split the two unsupported claims.

You can now treat a statistic as the output of a repeated process. The next chapter uses that process to state what a confidence limit or a tail probability can actually say.

[Back to the contents](../README.md)
