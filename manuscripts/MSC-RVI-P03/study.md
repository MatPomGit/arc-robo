# MSC-RVI-P03 — Kinematyczne ograniczenia całego ciała humanoida w planowaniu punktów obserwacji

**Program:** `arc-robo` · **obszar:** `robot-inspection` · **rodzaj:** `MANUSCRIPT` · **etap źródłowy:** `PLANNED`.

## Projekt badania

**Przedmiot:** Kinematyczne ograniczenia całego ciała humanoida w planowaniu punktów obserwacji.

- **Proponowany wynik główny:** Wykonalność kinematyczna i jakość punktu widzenia przy ograniczeniach całego ciała
- **Odrębność i ograniczenia:** Planowanie widoków przy znanej scenie z fizycznymi ograniczeniami humanoida; nie niepewność mapy z P04.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-RVI-P04`.

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

Źródło opisuje publiczny projekt [`arc-rvi`](https://github.com/MatPomGit/arc-rvi); pierwotny identyfikator `P03`.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
