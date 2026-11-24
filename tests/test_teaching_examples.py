import itertools
import math
import unittest
from fractions import Fraction as F

from lab.check_examples import examples
from lab.measure import (
    audit_trips, half_binomial_p, histogram, law_moments, regression,
    sample_mean_law, sign_flip_p, summary, t_interval,
)


class PrintedEvidence(unittest.TestCase):
    def test_snapshot_denominators_and_bounds(self):
        e=examples()["trip_audit"]
        self.assertEqual((e["planned"],e["observed"],e["late_observed"],e["cancelled"],e["unknown"]), (12,10,3,1,1))
        self.assertEqual(e["recorded_rate"],F(3,10))
        self.assertEqual(e["planned_adverse_bounds"],(F(1,3),F(5,12)))
        self.assertEqual(e["periods"]["peak"]["late"],3)
        self.assertEqual(e["periods"]["offpeak"]["late"],0)

    def test_denominator_does_not_confuse_boundary_or_missing(self):
        row=lambda i,s,d:{"trip_id":i,"period":"p","status":s,"delay_min":d}
        e=audit_trips([row("A","observed","6"),row("B","observed","7"),row("C","sensor_missing","")])
        self.assertEqual(e["recorded_rate"],F(1,2))
        self.assertEqual(e["planned_adverse_bounds"],(F(1,3),F(2,3)))
        e=audit_trips([row("A","cancelled",""),row("B","sensor_missing","")])
        self.assertIsNone(e["recorded_rate"])
        self.assertEqual(e["planned_adverse_bounds"],(F(1,2),F(1)))

    def test_missing_rows_and_duplicated_trips_raise(self):
        row={"trip_id":"A","period":"p","status":"observed","delay_min":"2"}
        for rows in [[],[row,row],[dict(row,delay_min="")],[dict(row,delay_min="-1")],[dict(row,delay_min=6.9)],[dict(row,delay_min="4.5")],
                     [dict(row,status="sensor_missing")],[dict(row,status="anything",delay_min="")]]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                audit_trips(rows)

    def test_original_mean_median_quartiles_and_variance(self):
        r=examples()["original_summary"]
        self.assertEqual((r["mean"],r["median"],r["q1"],r["q3"],r["iqr"]), (4,F(5,2),1,4,3))
        self.assertEqual(r["sample_variance"],F(80,3))
        self.assertAlmostEqual(r["sample_sd"],5.163977794943222)
        self.assertEqual(summary([0,2,4,6,8])["q3"],7)

    def test_tail_changes_mean_not_median_or_iqr(self):
        r=examples()["adjusted_summary"]
        self.assertEqual((r["mean"],r["median"],r["iqr"]), (3,F(5,2),3))

    def test_histogram_uncovered_right_bound_is_rejected(self):
        self.assertEqual(examples()["bins"],[5,4,0,0,0,0,1])
        self.assertEqual(histogram([0,3,6,8],[0,3,6,9]),[1,1,2])
        for args in [([-1],[0,3,6]),([6],[0,3,6]),([1],[0,3,3])]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                histogram(*args)

    def test_exact_sampling_masses_and_moments(self):
        e=examples()
        a={F(2):F(1,9),F(4):F(2,9),F(6):F(3,9),F(8):F(2,9),F(10):F(1,9)}
        b={F(4):F(1,3),F(6):F(1,3),F(8):F(1,3)}
        self.assertEqual(e["with_replacement"],(a,(6,F(16,3))))
        self.assertEqual(e["without_replacement"],(b,(6,F(8,3))))
        self.assertEqual(law_moments(sample_mean_law([2,6,10],3,replacement=False)),(6,0))
        self.assertEqual(sample_mean_law([0,0,3],1),{0:F(2,3),3:F(1,3)})

    def test_finite_population_formula_against_enumeration(self):
        for pop in ([0,1,2,10],[0,0,1,4,8]):
            N=len(pop)
            mu=F(sum(pop),N)
            variance=sum((x-mu)**2 for x in pop)/N
            for n in range(1,N+1):
                law=sample_mean_law(pop,n,replacement=False)
                self.assertEqual(law_moments(law),(mu,variance/n*F(N-n,N-1)))

    def test_excessive_exact_enumeration_is_rejected(self):
        with self.assertRaises(ValueError):
            sample_mean_law(range(10),12)

    def test_seeded_simulation_sanity_not_equals_proof(self):
        sim=examples()["simulation_sd"]
        self.assertAlmostEqual(sim[1],math.sqrt(F(32,3)),delta=.15)
        self.assertAlmostEqual(sim[4],math.sqrt(F(8,3)),delta=.10)

    def test_t_limits_against_df4_cdf_and_shift_invariance(self):
        e=examples()["t_interval"]
        self.assertAlmostEqual(e[0],2.0367568385224393,places=8)
        self.assertAlmostEqual(e[1],5.9632431614775607,places=8)
        critical=(e[1]-4)/math.sqrt(.5)
        u=critical/math.sqrt(critical*critical+4)
        self.assertAlmostEqual(.5+.75*u-.25*u**3,.975,places=10)
        lo,hi=t_interval([12,13,14,15,16],critical)
        self.assertAlmostEqual(lo,10+e[0])
        self.assertAlmostEqual(hi,10+e[1])
        with self.assertRaises(ValueError):
            t_interval([1,1,1],critical)

    def test_exact_randomization_includes_ties_and_zero_pairs(self):
        self.assertEqual(examples()["paired_randomization_p"],F(1,16))
        self.assertEqual(sign_flip_p([1,2,2,3,4,0]),F(1,16))
        self.assertEqual(sign_flip_p([1,-1]),F(1))
        self.assertEqual(sign_flip_p([-1,-2,-2,-3,-4]),F(1,16))

    def test_binomial_count_against_independent_outcome_strings(self):
        tails=sum(sum(seq)>=8 or sum(seq)<=2 for seq in itertools.product((0,1),repeat=10))
        self.assertEqual(half_binomial_p(8,10),F(tails,1024))
        self.assertEqual(half_binomial_p(8,10),F(7,64))
        self.assertEqual(half_binomial_p(5,10),1)

    def test_regression_residual_witness_and_degenerate_predictor(self):
        e=examples()["line"]
        self.assertEqual((e["intercept"],e["slope"],e["r2"]), (2,2,F(20,27)))
        self.assertEqual(e["residuals"],(1,-2,2,-2,1))
        self.assertEqual((e["sse"],e["sst"]),(14,54))
        self.assertEqual(sum(e["residuals"]),0)
        self.assertEqual(sum(x*r for x,r in enumerate(e["residuals"])),0)
        self.assertIsNone(regression([0,1,2],[4,4,4])["r2"])
        with self.assertRaises(ValueError):
            regression([2,2],[0,1])

    def test_regression_scaling_and_order(self):
        for x,y in [([0,1,2],[2,4,6]),([2,1,0],[6,4,2])]:
            self.assertEqual(regression(x,y)["slope"],2)
            self.assertEqual(regression([10*s for s in x],y)["slope"],F(1,5))


if __name__=="__main__":
    unittest.main()
