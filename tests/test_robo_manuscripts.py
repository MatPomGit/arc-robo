"""Structural checks for ARC Robo manuscript ownership and LaTeX drafts."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FOLDER = ROOT / "manuscripts"

TEX_NEW = {
    "MSC-AFFECT-P07",
    "MSC-HRI-P09", "MSC-HRI-P10",
    "MSC-RGBT-P01", "MSC-RGBT-P02", "MSC-RGBT-P03", "MSC-RGBT-P04",
    "MSC-RGBT-P05", "MSC-RGBT-P06", "MSC-RGBT-P07", "MSC-RGBT-P08",
    "MSC-RVI-P09", "MSC-SUV-P05", "MSC-S4D-P02", "MSC-S4D-P03",
}
TEX_EXTERNAL = {
    *(f"MSC-HRI-P{i:02d}" for i in range(1, 9)),
    *(f"MSC-RVI-P{i:02d}" for i in range(1, 9)),
    "MSC-S4D-P01",
}

class RoboManuscriptCatalogTest(unittest.TestCase):
    def test_32_distinct_manuscript_directories(self):
        got = {p.name for p in FOLDER.iterdir() if p.is_dir() and p.name.startswith("MSC-")}
        self.assertEqual(got, TEX_NEW | TEX_EXTERNAL)
        self.assertEqual(len(got), 32)

    def test_each_has_descriptive_readme(self):
        for ident in TEX_NEW | TEX_EXTERNAL:
            with self.subTest(ident=ident):
                doc = (FOLDER / ident / "README.md").read_text(encoding="utf-8")
                self.assertIn(ident, doc)
                self.assertGreater(len(doc), 240)

    def test_new_drafts_are_compilable_standalone_structure(self):
        titles = []
        for ident in sorted(TEX_NEW):
            with self.subTest(ident=ident):
                path = FOLDER / ident / "main.tex"
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                for fragment in (
                    r"\documentclass", r"\begin{document}", r"\end{document}",
                    r"\begin{abstract}", r"\end{abstract}",
                    r"\section{Operationalization and study population}", r"\section{Results}",
                ):
                    self.assertIn(fragment, text)
                title = re.search(r"\\title\{(.+?)\}", text)
                self.assertIsNotNone(title)
                titles.append(title.group(1))
        self.assertEqual(len(titles), len(set(titles)))

    def test_existing_tex_remains_canonical_in_source_repositories(self):
        for ident in TEX_EXTERNAL:
            with self.subTest(ident=ident):
                self.assertFalse((FOLDER / ident / "main.tex").exists())
                doc = (FOLDER / ident / "README.md").read_text(encoding="utf-8")
                self.assertIn("https://github.com/MatPomGit/", doc)
                self.assertIn(".tex", doc)

if __name__ == "__main__":
    unittest.main()
