# MSC-HRI-P01 — plan badania i relacje

**Temat:** Scenowe pola ryzyka dla wielu osób w predykcyjnym bezpieczeństwie humanoida

**Właściciel programu:** `arc-robo`. **Obszar:** `safety-hri`. **Rodzaj:** `MANUSCRIPT` (MANUSCRIPT). **Etap w źródle:** `PLANNED`. **Integracja:** `LINK_ONLY`.

## Zakres naukowy i operacjonalizacja

Temat badania: Scenowe pola ryzyka dla wielu osób w predykcyjnym bezpieczeństwie humanoida. Jest to roboczy wpis publikacyjny, a nie potwierdzenie ukończenia badania.

- **Proponowany wynik główny:** Równowaga bezpieczeństwo–wydajność w wielu jednoczesnych trajektoriach osób
- **Granica odrębności:** Model scenowy wielu ludzi, bez specjalistycznej geometrii i dynamiki ładunku z M03.
- **Uwagi klasyfikacyjne:** Klasyfikacja wg pytania badawczego: Główny wynik: fizyczne/geometryczne ryzyko i efektywność interakcji człowiek–humanoid; symulacja nie certyfikuje bezpieczeństwa. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji. AUDYT DUPLIKACJI: M03 jest specjalistycznym modelem ryzyka ładunku; zachować odrębność estimandów M01/M03. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Model scenowy wielu ludzi, bez specjalistycznej geometrii i dynamiki ładunku z M03. Główny wynik do prerejestracji: Równowaga bezpieczeństwo–wydajność w wielu jednoczesnych trajektoriach osób. Tytuł źródłowy zachowano w original_title_pl. Nie zmienia to
- **Powiązane prace:** `MSC-HRI-P03 (źródłowo arc-hri-safety:M03)`

## Stanowisko badawcze

**Proponowane stanowisko:** `ST-04`. To wstępne powiązanie tematyczne z rejestrem wspólnych stanowisk, **nie** potwierdzenie dostępności sprzętu ani zgody na badanie.

[Rejestr stanowisk](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md) • [Katalog urządzeń (prywatny, kontrola dostępu)](https://github.com/MatPomGit/devices)

## Powiązane aplikacje APP

- `app-hri-console` (`APP-ARC-08`), rola `OPTIONAL`, profil `ros2-replay`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-audio`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-events`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-image` (bieżąca nazwa repozytorium do uzgodnienia: `lib-vis`): kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-ros`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-sim`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.
- `lib-vlm`: kandydatura zależności pośredniej przez `app-hri-console`. Brak dowodu implementacji w tym artykule.

Powiązania APP/LIB pochodzą z planistycznych tabel `app_publication_links.csv` i `component_dependencies.csv`. Nie oznaczają gotowych repozytoriów, integracji ani działających pomiarów. Historyczne nazwy bibliotek nie są migrowane domyślnie.

## Pochodzenie i kontrola badań

- **Repozytorium źródłowe:** `MatPomGit/arc-hri-safety`, rekord `M01`, UID `arc-hri-safety:M01`.
- **Oryginalna ścieżka:** `manuscripts/01_predictive_risk_fields/article_plan.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-hri-safety/blob/main/manuscripts/01_predictive_risk_fields/article_plan.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
