# Publiczna witryna ARC Robo

Publiczne treści programu pochodzą wyłącznie z wydzielonego katalogu `site/`. Repozytorium zachowuje `docs/` dla dokumentacji technicznej; `mkdocs.yml` wskazuje na `docs_dir: site`. Witryna i jej wdrożenie są odrębne. Repozytorium nie zawiera workflow publikującego GitHub Pages. Job `pages-check` w `.github/workflows/validate-manuscripts.yml` sprawdza listę dopuszczonych treści i buduje witrynę MkDocs **wyłącznie offline w izolowanym CI**, bez wdrożenia i bez podnoszenia uprawnień.

## Identyfikacja wizualna

Logo całego programu w nagłówku MkDocs jest opcjonalne i pochodzi z `site/assets/brand/logo.png` (dopuszczalne także WebP i JPEG). W razie braku zatwierdzonej grafiki pozostaje nazwa ARC Robo. Dla poszczególnych projektów konwencją jest `site/assets/projects/<project_id>.png` (WebP/JPEG); katalog wyświetla ich logo wyłącznie przy pozycjach z `visibility=public`, `public_listing=true` i poprawnym publicznym URL.

Każdy obraz musi występować w `config/pages-policy.json:public_files` z odpowiadającym SHA-256 w `approved_image_sha256`. Kontrolę prowadzi `scripts/validate_pages.py`. Po zatwierdzeniu pliku logo programu `python scripts/site_branding.py --apply` synchronizuje `mkdocs.yml`; CI sprawdza tę zgodność bez zapisów. Zewnętrzne grafiki nie są kopiowane automatycznie.

## Kontrola publikacji

Generator `scripts/build_public_catalog.py` zapisuje jedynie `site/projects.md` z publicznie zatwierdzonych rekordów. Publiczne pliki nie zawierają źródeł manuskryptów, danych, instrukcji agentów ani notatek redakcyjnych. Konieczne są kontrola treści, pochodzenia zasobów, licencji, adresów i końcowego HTML. Samo pozytywne CI nie oznacza zgody na uruchomienie witryny.
