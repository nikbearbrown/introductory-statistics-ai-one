"""Reproduce the printed chapter calculations without external packages."""
import csv
from pathlib import Path

from lab.measure import (
    BINS, DELAYS, DEMO_X, DEMO_Y, POPULATION, T_CRIT_DF4,
    audit_trips, half_binomial_p, histogram, law_moments, regression,
    sample_mean_law, sign_flip_p, simulated_mean_sd, summary, t_interval,
)


def examples():
    location=Path(__file__).resolve().parents[1]/"data"/"weekday_snapshot.csv"
    with location.open(encoding="utf-8",newline="") as f:
        trips=audit_trips(csv.DictReader(f))
    independent=sample_mean_law(POPULATION,2)
    distinct=sample_mean_law(POPULATION,2,replacement=False)
    return {
        "trip_audit": trips,
        "original_summary": summary(DELAYS),
        "adjusted_summary": summary(DELAYS[:-1]+[8]),
        "bins": histogram(DELAYS,BINS),
        "with_replacement": (independent, law_moments(independent)),
        "without_replacement": (distinct,law_moments(distinct)),
        "simulation_sd": {n:simulated_mean_sd(POPULATION,n,4000,49) for n in (1,4)},
        "t_interval":t_interval([2,3,4,5,6],T_CRIT_DF4),
        "paired_randomization_p":sign_flip_p([1,2,2,3,4]),
        "exact_binomial_p":half_binomial_p(8,10),
        "line":regression(DEMO_X,DEMO_Y),
    }


if __name__ == "__main__":
    for name,value in examples().items():
        print(f"{name}: {value}")
