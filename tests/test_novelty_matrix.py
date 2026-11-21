"""Coverage of cited prior art and scientific decision boundaries for 14 plans."""
import pathlib
import re
import unittest
BASE = pathlib.Path(__file__).resolve().parents[1] / "manuscripts"
IDS = ("MSC-AFFECT-P07", "MSC-HRI-P09", "MSC-HRI-P10",
       *(f"MSC-RGBT-P{i:02d}" for i in range(1,9)), "MSC-RVI-P09",
       "MSC-S4D-P02", "MSC-S4D-P03")
class NoveltyCoverageTests(unittest.TestCase):
    def test_each_plan_has_evidence_based_comparison(self):
        for ident in IDS:
            with self.subTest(ident=ident):
                doc = (BASE/ident/"main.tex").read_text(encoding="utf-8")
                self.assertIn("Version 0.3.0",doc)
                for needle in (r"\section{Related research and novelty assessment}",
                               r"\section{Primary estimand and prospective decision rules}",
                               r"\begin{thebibliography}{9}",r"\end{thebibliography}",
                               "H1 is the primary scientific hypothesis"):
                    self.assertIn(needle,doc)
                self.assertEqual(len(re.findall(r"\\bibitem\{source\d+\}",doc)),2)
                self.assertEqual(len(re.findall(r"\\cite\{source\d+\}",doc)),2)
    def test_comparison_matrix_has_14_distinct_entries(self):
        source = (BASE/"literature"/"novelty_matrix.md").read_text(encoding="utf-8")
        rows = re.findall(r"^\| \[(MSC-[A-Z0-9]+-P\d{2})\]",source,flags=re.MULTILINE)
        self.assertEqual(len(rows),14)
        self.assertEqual(set(rows),set(IDS))
if __name__=="__main__":
    unittest.main()
