# Polityka automatyzacji ARC

Publiczne repozytoria `arc-*` **mogą korzystać z GitHub-hosted runners** (np. `ubuntu-latest`) do krótkiej, izolowanej walidacji plików, rejestrów i testów na `pull_request` oraz `push`. Użycie stałych runnerów HomeServer/Andromeda nie jest wymagane dla podstawowego CI. Dla repo prywatnych należy osobno ocenić koszt, poufność i dostęp.

W `arc-robo` działa workflow [`.github/workflows/validate-manuscripts.yml`](workflows/validate-manuscripts.yml), który sprawdza strukturę i testy Python oraz kompiluje wszystkie lokalne plany LaTeX po sprawdzeniu równości zbiorów ścieżek z manifestu i drzewa roboczego. Obecnie manifest obejmuje 31 przypiętych źródeł z lokalnymi szkicami oraz jedną lokalną koncepcję bez zewnętrznego źródła. Lokalne szkice nie są kopiami źródłowych manuskryptów. Kompilacja nie dowodzi gotowości naukowej ani prawa do publikacji. Strona Pages pozostaje osobnym procesem z wymaganą zgodą.

W workflowach używaj minimalnego `GITHUB_TOKEN` (`permissions: contents: read`). Nie uruchamiaj kodu obcych forków przez uprzywilejowane `pull_request_target`, nie przekazuj sekretów do niezaufanych PR i nie uruchamiaj ich kodu na stałych zaufanych runnerach. `audit-live` wymagający poświadczeń do prywatnych repozytoriów jest osobnym zadaniem z autoryzacją i bez automatycznego przenoszenia wyników do Pages.

Każda zmiana kontroli wymaga exact SHA, przeglądu uprawnień, zgodności z WIP Research Autopilot i **zero dodatkowych kosztów bez zgody**. Wydania, przenoszenie projektów i publikacja Pages wymagają osobnej zgody.
