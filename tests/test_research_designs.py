"""Regression tests for prospective research designs across ARC Robo drafts.

Run: python -m unittest discover -s tests -v
The checks are structural; they do not constitute scientific approval.
"""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANUSCRIPTS = ROOT / "manuscripts"
IDS = (
    "MSC-AFFECT-P07",
    "MSC-HRI-P09", "MSC-HRI-P10",
    *(f"MSC-RGBT-P{j:02d}" for j in range(1, 9)),
    "MSC-RVI-P09", "MSC-S4D-P02", "MSC-S4D-P03",
)


class ResearchDesignTests(unittest.TestCase):
    def test_every_new_draft_has_three_distinct_hypotheses(self):
        for ident in IDS:
            with self.subTest(ident=ident):
                tex = (MANUSCRIPTS / ident / "main.tex").read_text(encoding="utf-8")
                labels = re.findall(r"\\paragraph\{(H[1-3])\.\}", tex)
                self.assertEqual(labels, ["H1", "H2", "H3"])
                self.assertIn("Version 0.3.0", tex)

    def test_every_new_draft_defines_four_study_stages(self):
        for ident in IDS:
            with self.subTest(ident=ident):
                tex = (MANUSCRIPTS / ident / "main.tex").read_text(encoding="utf-8")
                labels = re.findall(r"\\subsection\{([A-D])\. [^\}]+\}", tex)
                self.assertEqual(labels, ["A", "B", "C", "D"])
                self.assertIn(r"\section{Detailed scientific scope and novelty boundary}", tex)
                self.assertIn(r"\section{Operationalization and study population}", tex)
                self.assertIn(r"\section{Evidence gates, reproducibility and ethical boundary}", tex)
                self.assertIn(r"\section{Results}", tex)
                self.assertIn(r"\end{document}", tex)

    def test_latex_braces_balanced(self):
        for ident in IDS:
            with self.subTest(ident=ident):
                content = (MANUSCRIPTS / ident / "main.tex").read_text(encoding="utf-8")
                depth = 0
                for i, char in enumerate(content):
                    if i and content[i - 1] == "\\":
                        continue
                    if char == "{":
                        depth += 1
                    elif char == "}":
                        depth -= 1
                        self.assertGreaterEqual(depth, 0)
                self.assertEqual(depth, 0)

    def test_existing_authoritative_sources_not_replicated(self):
        originals = [
            *(f"MSC-HRI-P{j:02d}" for j in range(1, 9)),
            *(f"MSC-RVI-P{j:02d}" for j in range(1, 9)),
            "MSC-S4D-P01",
        ]
        for ident in originals:
            with self.subTest(ident=ident):
                self.assertFalse((MANUSCRIPTS / ident / "main.tex").exists())

    def test_exact_draft_count(self):
        self.assertEqual(len(IDS), 14)
        tex = {p.parent.name for p in MANUSCRIPTS.glob("*/main.tex")}
        self.assertEqual(tex, set(IDS) | {"MSC-SUV-P05"})
        # MSC-SUV-P05 is a separate early concept and is not part of the 14\n        # historical four-stage designs covered by IDS.


if __name__ == "__main__":
    unittest.main()
