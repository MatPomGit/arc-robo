# MSC-RVI-P02 — plan badania i relacje

**Temat:** Odporna lokalizacja właściwego egzemplarza przy dystraktorach

**Właściciel programu:** `arc-robo`. **Obszar:** `robot-inspection`. **Rodzaj:** `MANUSCRIPT` (MANUSCRIPT). **Etap w źródle:** `PLANNED`. **Integracja:** `LINK_ONLY`.

## Zakres naukowy i operacjonalizacja

Temat badania: Odporna lokalizacja właściwego egzemplarza przy dystraktorach. Jest to roboczy wpis publikacyjny, a nie potwierdzenie ukończenia badania.

- **Proponowany wynik główny:** Nieokreślony w centralnej macierzy. Wymaga prerejestracji definicji, estymandu i kryteriów oceny.
- **Granica odrębności:** Wymaga porównania zakresu z powiązanymi pracami i źródłowym protokołem, zanim rozpocznie się pomiar.
- **Uwagi klasyfikacyjne:** Klasyfikacja wg pytania badawczego: Wybór właściwego fizycznego obiektu/egzemplarza i położenia celu inspekcji. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji.
- **Powiązane prace:** Nie wskazano formalnych powiązań w macierzy.

## Stanowisko badawcze

**Proponowane stanowisko:** `ST-04`, `ST-05`. To wstępne powiązanie tematyczne z rejestrem wspólnych stanowisk, **nie** potwierdzenie dostępności sprzętu ani zgody na badanie.

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

- **Repozytorium źródłowe:** `MatPomGit/arc-rvi`, rekord `P02`, UID `arc-rvi:P02`.
- **Oryginalna ścieżka:** `papers/paper02/README.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-rvi/blob/main/papers/paper02/README.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
