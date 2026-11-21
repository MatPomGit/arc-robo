# ARC Robo — badania percepcji, nawigacji i bezpieczeństwa robotów

**Rodzaj repozytorium:** program naukowy `arc-*`  
**Program:** `arc-robo`  
**Schemat rejestrów:** `1` (starszy format, przed migracją)  
**Autor podstawowy:** Mateusz Pomianek; dodatkowi współautorzy po potwierdzeniu wkładu  
**Stan naukowy:** indeks planowany, bez potwierdzonych wyników empirycznych

## Misja i granice programu

ARC Robo skupia projekty naukowe dotyczące percepcji RGB/LWIR, aktywnej inspekcji humanoidów, predykcyjnego bezpieczeństwa interakcji człowiek–robot, wspomaganej multimodalnie teleoperacji oraz nawigacji UAV. Kryterium przypisania stanowi robotyczny wynik główny i możliwość jego niezależnej walidacji. Szczegółowe protokoły, dane i kanoniczne źródła dojrzałych manuskryptów pozostają w projektach źródłowych; ARC Robo utrzymuje indeks przekrojowy.

## Katalog artykułów

[Indeks 31 artykułów oraz pliki LaTeX dla brakujących pozycji](manuscripts/README.md). Szczegółowy status i lokalizacja oryginalnego manuskryptu są opisane osobno dla każdego identyfikatora MSC.

## Propozycje kierunków badawczych

[MSC-RVI-P09: wiarygodność dowodów ukończenia misji inspekcyjnej w ocenie operatora](docs/research-proposals-2026.md) to propozycja naukowa oparta na planowanym wtórnym użyciu symulacji robotycznej, **bez zatwierdzonego manuskryptu i bez badania na robocie fizycznym**.

## Katalog badań

Programowy rejestr projektu i zależności znajduje się w [`portfolio/projects.json`](portfolio/projects.json) oraz [`portfolio/dependencies.json`](portfolio/dependencies.json). W obecnym schemacie v1 [`portfolio/papers.json`](portfolio/papers.json) pozostaje pusty, a **rzeczywisty indeks 31 pozycji i przypiętych źródeł** znajduje się w [`manuscripts/source_manifest.json`](manuscripts/source_manifest.json). Nie traktuj pustego `portfolio/papers.json` jako dowodu braku manuskryptów. Projekt `msc-*` ma własny protokół, manuskrypt, dane referencyjne i GitHub Pages; ARC utrzymuje tylko odnośniki oraz metadane zależności. Starsze repozytoria mogą być wskazywane pod obecną nazwą do czasu kontrolowanej migracji.

[Dokumentacja katalogu projektów](docs/projects.md) nie jest automatycznie publikowaną witryną; GitHub Pages pozostaje nieskonfigurowany. Program ARC nie jest repozytorium surowych danych uczestników ani pakietem aplikacji.

## Uruchomienie

```bash
python scripts/validate_repository.py --phase scaffold
python -m unittest discover -s tests -v
python scripts/build_public_catalog.py
# Jeśli skonfigurowano submoduły, pobierz przypięte wersje:
python scripts/bootstrap.py --mode reproduce
# Gdy potrzebujesz analizy bieżącego portfolio, sprawdź aktualne gałęzie zdalne:
python scripts/bootstrap.py --mode audit-live
```

Weryfikacja `audit-live` **nie zmienia** przypiętych commitów i nie uruchamia kodu projektów podrzędnych. Brak dostępu do prywatnego repozytorium daje `UNAVAILABLE`, nie `PASS`.

## Audyt i plan napraw

Zobacz [niezależny audyt szablonu ARC z 2026-11-19](reviews/2026-11-19-template-audit.md), zawierający priorytety P0–P2 i test akceptacyjny. Repozytorium ma workflow `.github/workflows/validate-manuscripts.yml`, który uruchamia testy struktury i kompilację 14 lokalnych planów LaTeX. Odsyłacze do pozostałych 17 manuskryptów są testowane jako źródła zewnętrzne.

## Otwartość

Strona programu: **NOT_CONFIGURED**. Strony indywidualnych projektów znajdują się w odpowiednich repozytoriach. Architektura: [ARCHITECTURE.md](ARCHITECTURE.md). Zasady badań: [RESEARCH.md](RESEARCH.md). Reprodukowanie wersji: [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Kryteria publikacji: [docs/publication-policy.md](docs/publication-policy.md).

Nie publikować prywatnych nazw, danych ani wewnętrznych ścieżek bez zgody właściciela. Plik `LICENSE` pozostaje nieaktywnym szablonem do chwili wyboru właściwej licencji.
