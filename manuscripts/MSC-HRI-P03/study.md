# MSC-HRI-P03 — plan badania i relacje

**Temat:** Dynamika ładunku i omiatana geometria manipulatora w ocenie kolizji humanoida

**Właściciel programu:** `arc-robo`. **Obszar:** `safety-hri`. **Rodzaj:** `MANUSCRIPT` (MANUSCRIPT). **Etap w źródle:** `PLANNED`. **Integracja:** `LINK_ONLY`.

## Zakres naukowy i operacjonalizacja

Temat badania: Dynamika ładunku i omiatana geometria manipulatora w ocenie kolizji humanoida. Jest to roboczy wpis publikacyjny, a nie potwierdzenie ukończenia badania.

- **Proponowany wynik główny:** Błąd oszacowania ryzyka ładunku względem referencji geometrycznej i dynamicznej
- **Granica odrębności:** Odrębny model geometrii ładunku i przenoszonej masy, nie scenowy model wielu osób M01.
- **Uwagi klasyfikacyjne:** Klasyfikacja wg pytania badawczego: Modelowanie ryzyka robotycznego zależnego od ładunku, ruchu i odległości. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji. AUDYT DUPLIKACJI: nie powielać modelu pól ryzyka M01, wymagane niezależne geometryczne/dynamiczne wyniki. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Odrębny model geometrii ładunku i przenoszonej masy, nie scenowy model wielu osób M01. Główny wynik do prerejestracji: Błąd oszacowania ryzyka ładunku względem referencji geometrycznej i dynamicznej. Tytuł źródłowy zachowano w original_title_pl. Nie zmienia to zatwierdzonego tytułu manuskryptu źródłowego ani
- **Powiązane prace:** `MSC-HRI-P01 (źródłowo arc-hri-safety:M01)`

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

- **Repozytorium źródłowe:** `MatPomGit/arc-hri-safety`, rekord `M03`, UID `arc-hri-safety:M03`.
- **Oryginalna ścieżka:** `manuscripts/03_payload_aware_dynamic_risk/article_plan.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-hri-safety/blob/main/manuscripts/03_payload_aware_dynamic_risk/article_plan.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
