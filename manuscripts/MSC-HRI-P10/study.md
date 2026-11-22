# MSC-HRI-P10 — Wpływ opóźnienia telemetrii na błędną pewność oceny ryzyka w HRI humanoida

**Program:** `arc-robo` · **obszar:** `embodied-uncertainty-transfer` · **rodzaj:** `IDEA` · **etap źródłowy:** `IDEA_REVIEW`.

## Projekt badania

**Przedmiot:** Wpływ opóźnienia telemetrii na błędną pewność oceny ryzyka w HRI humanoida.

- **Proponowany wynik główny:** Odsetek niebezpiecznie pewnych ocen ryzyka przy zadanym opóźnieniu danych
- **Odrębność i ograniczenia:** Hipoteza autorsko do zatwierdzenia: opóźnienie i nieaktualność telemetrii humanoida, nie nawigacja UAV i nie kalibracja zasięgalności M04.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-HRI-P04`, `MSC-S4D-P02`.

## Stanowisko badawcze

**`ST-04`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-hri-console`** (`APP-ARC-08`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-audio`**: `SCOPE_CONSOLIDATED_PLAN`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-events`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-ros`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-sim`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-track`**: `NEW_SCAFFOLD_EXISTS`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-vis`**: `RENAMED_ARCHITECTURE_ONLY`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.
- **`lib-vlm`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-hri-console`; wykonanie integracji niezweryfikowane.

## Proweniencja i bramki

Dane o niepublicznych repozytoriach i pełnej historii pochodzenia znajdują się poza dokumentacją publiczną.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
