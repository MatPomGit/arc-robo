# MSC-HRI-P10 — plan badania i relacje

**Temat:** Wpływ opóźnienia telemetrii na błędną pewność oceny ryzyka w HRI humanoida

**Właściciel programu:** `arc-robo`. **Obszar:** `embodied-uncertainty-transfer`. **Rodzaj:** `IDEA` (CANDIDATE). **Etap w źródle:** `IDEA_REVIEW`. **Integracja:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Zakres naukowy i operacjonalizacja

Temat badania: Wpływ opóźnienia telemetrii na błędną pewność oceny ryzyka w HRI humanoida. Jest to kandydatura do oceny nowości i niezależności, a nie zatwierdzony projekt empiryczny.

- **Proponowany wynik główny:** Odsetek niebezpiecznie pewnych ocen ryzyka przy zadanym opóźnieniu danych
- **Granica odrębności:** Hipoteza autorsko do zatwierdzenia: opóźnienie i nieaktualność telemetrii humanoida, nie nawigacja UAV i nie kalibracja zasięgalności M04.
- **Uwagi klasyfikacyjne:** NO-GO: brak wspólnego estimandu i realnych zamrożonych domen. [Klasyfikacja portfolio 2026-11-20] Zagadnienie transferu kalibracji ryzyka i niepewności między humanoidem a UAV; fizyczne semantyki i benchmarki autonomii są rdzeniem pytania. Powiązane z F-S4D-01 jako jeden pomysł; brak obecnie niezależnego wspólnego estimandu i gotowości dowodowej, NO-GO pozostaje. AUDYT ROZGRANICZENIA 2026-11-20: HRI: bezpieczeństwo humanoida i fizyczna interakcja człowiek–robot (Unitree G1), nie badanie drona. W dwóch repozytoriach znajduje się pokrewny, warunkowy szkic meta-benchmarku transferu kalibracji, ale podstawowe manuskrypty HRI M01–M08 oraz S4D P01 są odrębne i nie stanowią duplikatów. Wspólny arty
- **Powiązane prace:** `MSC-HRI-P04 (źródłowo arc-hri-safety:M04)`, `MSC-S4D-P02 (źródłowo arc-s4d-tam:F-S4D-01)`

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

- **Repozytorium źródłowe:** `MatPomGit/arc-hri-safety`, rekord `F-HRI-02`, UID `arc-hri-safety:F-HRI-02`.
- **Oryginalna ścieżka:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał źródłowy:** [otwórz źródło](https://github.com/MatPomGit/arc-hri-safety/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Macierz rejestru:** [publication_matrix.csv](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed nowym eksperymentem należy sprawdzić prawa do danych i sprzętu, zgodę etyczną, niezależny wynik główny, plan analizy, próbę, metryki, podziały danych i ryzyka powielania publikacji. Brak rezultatów w karcie nie jest wynikiem zerowym.
