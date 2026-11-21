# MSC-HRI-P09 — plan badania i relacje

**Temat:** Adwersarialne falsyfikowanie reguł predykcyjnego bezpieczeństwa

**Właściciel programu:** `arc-robo`. **Obszar:** `safety-hri`. **Rodzaj:** `IDEA` (CANDIDATE). **Etap w źródle:** `IDEA_REVIEW`. **Integracja:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Zakres naukowy i operacjonalizacja

Temat badania: Adwersarialne falsyfikowanie reguł predykcyjnego bezpieczeństwa. Jest to kandydatura do oceny nowości i niezależności, a nie zatwierdzony projekt empiryczny.

- **Proponowany wynik główny:** Nieokreślony w centralnej macierzy. Wymaga prerejestracji definicji, estymandu i kryteriów oceny.
- **Granica odrębności:** Wymaga porównania zakresu z powiązanymi pracami i źródłowym protokołem, zanim rozpocznie się pomiar.
- **Uwagi klasyfikacyjne:** Warunkowe GO jako metoda falsyfikacji, nie osobny artykuł teraz.
- **Powiązane prace:** `MSC-HRI-P01 (źródłowo arc-hri-safety:M01)`, `MSC-HRI-P07 (źródłowo arc-hri-safety:M07)`

## Stanowisko badawcze

**Proponowane stanowisko:** `ST-04`, `ST-00`. To wstępne powiązanie tematyczne z rejestrem wspólnych stanowisk, **nie** potwierdzenie dostępności sprzętu ani zgody na badanie.

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

- **Repozytorium źródłowe:** `MatPomGit/arc-hri-safety`, rekord `F-HRI-01`, UID `arc-hri-safety:F-HRI-01`.
- **Oryginalna ścieżka:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-hri-safety/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
