# MSC-RVI-P09 — plan badania i relacje

**Temat:** Czy operator rozpozna fałszywie zakończoną misję inspekcji robota dzięki ujawnieniu dowodów?

**Właściciel programu:** `arc-robo`. **Obszar:** `operator-inspection-evidence-judgment`. **Rodzaj:** `IDEA` (CANDIDATE). **Etap w źródle:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Integracja:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Zakres naukowy i operacjonalizacja

Temat badania: Czy operator rozpozna fałszywie zakończoną misję inspekcji robota dzięki ujawnieniu dowodów?. Jest to kandydatura do oceny nowości i niezależności, a nie zatwierdzony projekt empiryczny.

- **Proponowany wynik główny:** Nieokreślony w centralnej macierzy. Wymaga prerejestracji definicji, estymandu i kryteriów oceny.
- **Granica odrębności:** Wymaga porównania zakresu z powiązanymi pracami i źródłowym protokołem, zanim rozpocznie się pomiar.
- **Uwagi klasyfikacyjne:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet B] Badanie false acceptance na już istniejących symulowanych fixture RVI z niezależną prawdą i trzema wariantami raportu. Główny wynik to błąd decyzji operatora, nie obiektywna skuteczność robota P08, jakość zdjęć P06 ani poczucie safety M08. Bez ruchu G1; etyka przed badaniem ludzi. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Propozycja znajduje się w dokumentacji programu, w otwartym PR, bez wpisu do katalogu zatwierdzonych publikacji.
- **Powiązane prace:** `MSC-RVI-P08 (źródłowo arc-rvi:P08)`, `MSC-RVI-P06 (źródłowo arc-rvi:P06)`, `MSC-HRI-P08 (źródłowo arc-hri-safety:M08)`

## Stanowisko badawcze

**Proponowane stanowisko:** `ST-04`, `ST-05`. To wstępne powiązanie tematyczne z rejestrem wspólnych stanowisk, **nie** potwierdzenie dostępności sprzętu ani zgody na badanie.

[Rejestr stanowisk](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md) • [Katalog urządzeń (prywatny, kontrola dostępu)](https://github.com/MatPomGit/devices)

## Powiązane aplikacje APP

- `app-hri-console` (`APP-ARC-08`), rola `PRIMARY`, profil `ros2-replay`, bramka `MVP`.

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

- **Repozytorium źródłowe:** `MatPomGit/arc-robo`, rekord `ROBO-IDEA-01`, UID `arc-robo:ROBO-IDEA-01`.
- **Oryginalna ścieżka:** `docs/research-proposals-2026.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-robo/blob/c8a8d59e735def4d0912dd5c81431766b0535d14/docs/research-proposals-2026.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
