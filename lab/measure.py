"""Small offline statistics tools. Original teaching code, Python 3.10+."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, isfinite, sqrt
from random import Random
from statistics import median, stdev


def audit_trips(rows, threshold=6):
    """Outcomes require integer delay for observed trips, blank otherwise."""
    rows = list(rows)
    seen, periods = set(), {}
    total_observed = total_late = total_cancelled = total_unknown = 0
    for row in rows:
        trip_id, period, status, raw = (row[k] for k in ("trip_id", "period", "status", "delay_min"))
        if not trip_id or not period or trip_id in seen:
            raise ValueError("missing identifier/period or duplicate trip")
        seen.add(trip_id)
        count = periods.setdefault(period, Counter())
        count["planned"] += 1
        if status == "observed":
            if not isinstance(raw,str) or not raw.isascii() or not raw.isdecimal():
                raise ValueError("observed trip needs nonnegative integer text")
            delay = int(raw)
            total_observed += 1
            total_late += delay > threshold
            count["observed"] += 1
            count["late"] += delay > threshold
        elif status in {"cancelled", "sensor_missing"} and raw == "":
            if status == "cancelled":
                total_cancelled += 1
            else:
                total_unknown += 1
            count[status] += 1
        else:
            raise ValueError("invalid trip status or delay on an unobserved trip")
    if not rows:
        raise ValueError("at least one planned trip required")
    low = total_late + total_cancelled
    return {"planned": len(rows), "observed": total_observed, "late_observed": total_late,
            "cancelled": total_cancelled, "unknown": total_unknown,
            "recorded_rate": Fraction(total_late, total_observed) if total_observed else None,
            "planned_adverse_bounds": (Fraction(low, len(rows)), Fraction(low+total_unknown, len(rows))),
            "periods": {period: dict(count) for period, count in periods.items()}}


def summary(values):
    values = sorted(map(Fraction, values))
    n = len(values)
    if n < 2:
        raise ValueError("need at least two values")
    mean = sum(values)/n
    sse = sum((x-mean)**2 for x in values)
    q1, q3 = median(values[:n//2]), median(values[(n+1)//2:])
    return {"mean": mean, "median": median(values), "q1": q1, "q3": q3, "iqr": q3-q1,
            "sample_variance": sse/(n-1), "sample_sd": sqrt(sse/(n-1))}


def histogram(values, edges):
    """Integer-valued example bins [left, right), including the final bin."""
    if len(edges) < 2 or any(a >= b for a,b in zip(edges,edges[1:])):
        raise ValueError("increasing bin edges are required")
    counts = [0]*(len(edges)-1)
    for x in values:
        for i,(a,b) in enumerate(zip(edges,edges[1:])):
            if a <= x < b:
                counts[i] += 1
                break
        else:
            raise ValueError(f"uncovered value {x}")
    return counts


def sample_mean_law(population, n, *, replacement=True):
    """Exact equiprobable ordered draws or equiprobable simple random subsets."""
    pop = tuple(map(Fraction, population))
    if not pop or not 1 <= n <= 30 or len(pop) > 500 or (not replacement and n > len(pop)):
        raise ValueError("sample dimensions outside the small teaching domain")
    size = len(pop)**n if replacement else comb(len(pop),n)
    if size > 100000:
        raise ValueError("enumeration exceeds 100000 equally likely samples")
    draws = product(pop, repeat=n) if replacement else combinations(pop,n)
    counts = Counter(sum(draw)/n for draw in draws)
    return {value: Fraction(count,size) for value,count in sorted(counts.items())}


def law_moments(law):
    if sum(law.values()) != 1 or any(p < 0 for p in law.values()):
        raise ValueError("need a probability law")
    mu = sum(x*p for x,p in law.items())
    return mu, sum((x-mu)**2*p for x,p in law.items())


def simulated_mean_sd(population, n, repeats, seed):
    if not population or not 1 <= n <= 100 or not 2 <= repeats <= 20000:
        raise ValueError("simulation dimensions exceed teaching bounds")
    rng = Random(seed)
    means = [sum(rng.choice(population) for _ in range(n))/n for _ in range(repeats)]
    return stdev(means)


def t_interval(values, critical):
    """One-sample t interval for a supplied correct two-sided critical value."""
    if not isfinite(critical) or critical <= 0:
        raise ValueError("positive finite critical value required")
    vals = tuple(map(Fraction,values))
    data = summary(vals)
    if data["sample_variance"] == 0:
        raise ValueError("this exercise doesn't treat zero observed variation as certainty")
    se = sqrt(data["sample_variance"]/len(vals))
    mean = data["mean"]
    return float(mean)-critical*se, float(mean)+critical*se


def sign_flip_p(differences):
    """Exact two-sided absolute-sum randomization probability under independent fair swaps."""
    diffs = tuple(map(Fraction,differences))
    if not 1 <= len(diffs) <= 15:
        raise ValueError("need 1..15 paired differences")
    observed = abs(sum(diffs))
    tail = sum(abs(sum(s*x for s,x in zip(signs,diffs))) >= observed
               for signs in product((-1,1),repeat=len(diffs)))
    return Fraction(tail,2**len(diffs))


def half_binomial_p(k, n):
    """Two-sided exact probability of at least the observed departure from n/2."""
    if not 1 <= n <= 250 or not 0 <= k <= n:
        raise ValueError("require 1 <= n <= 250 and 0 <= k <= n")
    return Fraction(sum(comb(n,j) for j in range(n+1) if abs(2*j-n) >= abs(2*k-n)),2**n)


def regression(x, y):
    """Least-squares line with intercept; exact decimal-free rationals on integer data."""
    x,y=tuple(map(Fraction,x)),tuple(map(Fraction,y))
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("need paired data")
    n=len(x)
    xb,yb=sum(x)/n,sum(y)/n
    sxx=sum((a-xb)**2 for a in x)
    if sxx==0:
        raise ValueError("slope unidentified when all x are equal")
    b=sum((a-xb)*(b-yb) for a,b in zip(x,y))/sxx
    a=yb-b*xb
    residuals=tuple(b_obs-(a+b*a_obs) for a_obs,b_obs in zip(x,y))
    sse=sum(e**2 for e in residuals)
    sst=sum((b_obs-yb)**2 for b_obs in y)
    return {"intercept":a,"slope":b,"residuals":residuals,
            "sse":sse,"sst":sst,"r2":1-sse/sst if sst else None}


DELAYS=[0,1,1,2,2,3,4,4,5,18]
BINS=[0,3,6,9,12,15,18,21]
POPULATION=[2,6,10]
T_CRIT_DF4=2.7764451051977987
DEMO_X=[0,1,2,3,4]
DEMO_Y=[3,2,8,6,11]
