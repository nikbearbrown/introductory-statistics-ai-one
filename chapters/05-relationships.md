# Chapter 5 — Model relationships carefully

*Subtract the fitted line before deciding what the fit accomplished.*

Imagine dispatch records a prior-segment congestion index $x$ from zero to four and the next arrival's lateness $y$ in minutes. A model fits a positive slope. Should the team change the notification timing of crowded trips? That decision is not in the slope. A regression summarizes a measured relationship under a choice of outcome and loss; a policy change needs other evidence.

By the end, calculate a least-squares line on paired observations, identify what residuals and in-sample fit reveal, flag an extrapolation, and separate an association from a causal action.

## Put the units and the loss on the table

Here are five ordered pairs from an invented fixture, not a representative transit study:

| Prior-segment index $x$ | 0 | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Recorded lateness $y$, minutes | 3 | 2 | 8 | 6 | 11 |

We fit $\hat y=a+bx$ by minimizing the sum of squared **vertical residuals** $e_i=y_i-\hat y_i$. Vertical means a difference in $y$ at the same supplied $x$, not the perpendicular distance to the line. Treating $x$ as the given predictor and squaring misses are design choices. Big errors get disproportionate weight, so a highly influential observation can move the line. If swapping $x$ and $y$ changes the problem you intend to solve, it is appropriate for the fitted model to change too.

Calculate the means $\bar x=2$ and $\bar y=6$. With an intercept, the slope is the sum of centered cross-products divided by the sum of centered squared predictor values:

$$b=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}=\frac{6+4+0+0+10}{4+1+0+1+4}=2.$$

The intercept is $a=\bar y-b\bar x=6-2\cdot2=2$. In these units the fitted value rises by two minutes per one additional index point. It is not a two-minute **intervention** effect. Re-expressing the predictor on a scale ten times larger would divide the numerical slope by ten and leave the fitted values unchanged. If all predictors were identical, the denominator would be zero and the slope would not be identified from these data.

Here is an algebraic check on least squares, without calculus. The residuals for the fitted line sum to zero and their weighted sum using the $x_i$ also vanishes. Any candidate change to the line alters each prediction by $u+vx_i$ for some constants $u,v$. The adjusted residual sum of squares expands as the fitted residual sum of squares plus $\sum(u+vx_i)^2$ minus twice the cross-product with the old residuals. The cross-product is $u\sum e_i+v\sum x_ie_i=0$. Therefore the adjustment cannot improve the objective. With more than one distinct predictor value, only zero adjustment leaves each prediction unchanged. The two sum checks are fast arithmetic diagnostics and also explain why the found line is truly least squares under the chosen loss.

## Read the misses, not just the score

| $x$ | Actual $y$ | Fitted $2+2x$ | Residual $y-\hat y$ |
| ---: | ---: | ---: | ---: |
| 0 | 3 | 2 | +1 |
| 1 | 2 | 4 | −2 |
| 2 | 8 | 6 | +2 |
| 3 | 6 | 8 | −2 |
| 4 | 11 | 10 | +1 |

At index 1 the predictor overestimates the measured delay by two minutes; the residual is **negative**. Across the five rows the residuals are $1,-2,2,-2,1$. The residual sum of squares is $14$, while the constant mean-only model has total squared deviation $54$. With an intercept the familiar $R^2=1-14/54=20/27\approx0.741$ describes the fraction of variation accounted for relative to that baseline **in these data under squared loss**. It is not the percentage of predictions within tolerance, the fraction of lateness caused by congestion, or a guarantee of held-out performance. If all $y$ are equal, that baseline denominator is zero and the lab reports $R^2$ undefined. With one predictor, nonzero variation in both variables and an intercept, $R^2$ is squared sample correlation; correlation retains the sign of the paired linear association but not the minutes-per-index units.

A residual plot can reveal curvature, different spreads by predictor value, or clusters by route or hour. This tiny fixture cannot support a diagnosis of real-world residual variance or prove the absence of a pattern. Draw the five residual points against predictor and mark zero before describing what you see. If a large fit concern appears only after sorting actual arrival order, inspect the same residuals by time. A useful validation split would fit on some dates and test on held-out later dates, not randomly break up rows from the same operating day if those rows share a shock. Give the baseline and the unit of loss. A high training $R^2$ can survive a narrow, biased sample and fail wherever you most want to use it. The [NIST regression diagnostics handbook](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm) gives a reference point for inspecting residuals instead of declaring a model good from a single score.

## Separate extrapolation and intervention

The algebra supplies a predicted value of 18 minutes at $x=8$. The fixture's index was defined only from 0 to 4. For this case the offer is not merely beyond the observed range; it is outside the model input's definition. Even at $x=4$ the fitted mean-like value is not a forecast with a validated uncertainty interval. For example, two routes could use the same index scale while their connection timing differs enough that the slope cannot be transported. Identify the support and who collected it before fitting a line through it.

Suppose heavier-load conditions occur almost entirely at the same time as a trial dispatch procedure. Time of day may affect lateness, and the selected procedure is not independently varied. A fitted slope for congestion could reflect a route mix, an unrecorded incident or measurement differences rather than what would happen under a dispatch intervention. Adding an extra column does not create evidence where groups do not overlap. For a decision, first ask whether the goal is useful prediction, descriptive adjustment or a causal effect under a credible design. Consider randomly assigning a procedure across eligible blocks with a prespecified outcome where operationally appropriate. The algebra does not approve an operational change. It can help specify which uncertainty the next design should resolve.

A hypothetical polished summary says “74% of late arrivals were caused by congestion.” This workbook computed no such count. Identify the actual statistic, its numerator and denominator, and the model alternatives. A better statement is “On five synthetic paired observations, the fitted slope was two minutes per index point; the line reduced squared error from 54 to 14 relative to the sample-mean baseline. The data do not show an intervention effect.” Use big words only where they do real work.

## Exercises

- **Warm-up, check:** Verify one named centered cross-product in the slope and one signed residual by hand.
- **Warm-up, units:** State the slope's units and explain what changes if all outcomes are expressed in seconds.
- **Application, leverage:** Imagine adding a point at $x=4$ with lateness 40 minutes. Predict which diagnostic would change, then refit and check.
- **Application, validation:** Choose a publicly explainable loss for a held-out emergency window. State why training $R^2$ does not answer it.
- **Synthesis, causation:** Design a setting in which the same positive slope would arise without any causal effect of the policy being discussed. Name the missing comparison.
- **Challenge, extrapolation:** A revised index ranges from 0 to 8 after recalibration. Explain why extending the original line may still be invalid even though 8 is now a legal number.

You can now report a fit with an error audit and a limit. Apply the whole chain to the [capstone](../practice/capstone.md): define the denominator, expose what disappeared, hand-check a calculation, and stop a plausible but unsupported recommendation.

[Back to the contents](../README.md)
