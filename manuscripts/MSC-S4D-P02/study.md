# MSC-S4D-P02 — plan badania i relacje

**Temat:** Kalibracja niepewności lokalizacji drona przy degradacji GNSS i zmianie środowiska

**Właściciel programu:** `arc-robo`. **Obszar:** `embodied-uncertainty-transfer`. **Rodzaj:** `IDEA` (CANDIDATE). **Etap w źródle:** `IDEA_HOLD`. **Integracja:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Zakres naukowy i operacjonalizacja

Temat badania: Kalibracja niepewności lokalizacji drona przy degradacji GNSS i zmianie środowiska. Jest to kandydatura do oceny nowości i niezależności, a nie zatwierdzony projekt empiryczny.

- **Proponowany wynik główny:** Pokrycie i ryzyko fałszywej pewności estymacji lokalizacji UAV przy zakłóceniach GNSS
- **Granica odrębności:** Hipoteza autorsko do zatwierdzenia: wyłącznie estymacja UAV i jej ryzyko, bez humanoida. Oddzielić od jakości tras semantycznych S4D P01.
- **Uwagi klasyfikacyjne:** NO-GO teraz; [Klasyfikacja portfolio 2026-11-20] Zachować IDEA_HOLD/NO-GO i nie liczyć jako odrębnej zatwierdzonej publikacji. AUDYT ROZGRANICZENIA 2026-11-20: S4D: semantyczna nawigacja latającego UAV przy degradacji GNSS, nie fizyczne HRI humanoida. W dwóch repozytoriach znajduje się pokrewny, warunkowy szkic meta-benchmarku transferu kalibracji, ale podstawowe manuskrypty HRI M01–M08 oraz S4D P01 są odrębne i nie stanowią duplikatów. Wspólny artykuł metodologiczny byłby odrębnym przyszłym projektem tylko po zdefiniowaniu wspólnego estimandu i zweryfikowaniu danych obu platform; nie należy utożsamiać platform, dynamiki, ryzyk i metryk. | Proponowane doprecyzowanie zakresu portfolio 2026-11
- **Powiązane prace:** `MSC-HRI-P10 (źródłowo arc-hri-safety:F-HRI-02)`, `MSC-HRI-P04 (źródłowo arc-hri-safety:M04)`

## Stanowisko badawcze

**Stanowisko:** brak jednoznacznego przypisania do ST-00–ST-08. Dla tej pracy wymagany jest odrębny plan stanowiska i bramka kwalifikacji; nie przypisywać automatycznie do stanowiska humanoidalnego.

[Rejestr stanowisk](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md) • [Katalog urządzeń (prywatny, kontrola dostępu)](https://github.com/MatPomGit/devices)

## Powiązane aplikacje APP

Brak przypisanej aplikacji w centralnej tabeli. Nie utożsamiać tego z brakiem potrzeb programowych.

## Powiązane biblioteki LIB

Brak zadeklarowanych powiązań LIB wynikających z aplikacji w centralnej tabeli.

Powiązania APP/LIB pochodzą z planistycznych tabel `app_publication_links.csv` i `component_dependencies.csv`. Nie oznaczają gotowych repozytoriów, integracji ani działających pomiarów. Historyczne nazwy bibliotek nie są migrowane domyślnie.

## Pochodzenie i kontrola badań

- **Repozytorium źródłowe:** `MatPomGit/arc-s4d-tam`, rekord `F-S4D-01`, UID `arc-s4d-tam:F-S4D-01`.
- **Oryginalna ścieżka:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-s4d-tam/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
