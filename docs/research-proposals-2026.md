# ARC Robo — propozycje badań nad wiarygodnością raportów inspekcyjnych

**Wersja:** 1.2.0 | **Data:** 2026-11-20 | **Status:** propozycja do oceny, bez zatwierdzenia badań z udziałem ludzi i bez wyników empirycznych.  
**Program:** ARC Robo. **Identyfikator:** `MSC-RVI-P09`.

## MSC-RVI-P09 — Błędna akceptacja ukończenia misji przez operatora robota

**Tytuł roboczy (EN):** *Detecting False Mission Completion from Robot Inspection Evidence: An Operator-Centered Study*.

**Pytanie badawcze:** Czy raport jawnie przedstawiający brakujące zdjęcia, błędnie powiązane obiekty i niedostateczne dowody wykonania ogranicza przypadki uznania nieukończonej misji za zakończoną przez operatora?

**Hipoteza:** Przy stałej rzeczywistej poprawności misji i podobnej objętości informacji raport oparty na dowodach i brakach zwiększa wykrywalność fałszywych deklaracji ukończenia względem samego komunikatu sukcesu lub statusu binarnego.

**Ponowne wykorzystanie istniejącego systemu:** Projekt [arc-rvi](https://github.com/MatPomGit/arc-rvi) zawiera scenariusze *offline* dotyczące identyfikacji właściwego samochodu/części, wymaganych ujęć, jakości zdjęć i kompletności zestawu. Należy wykorzystać je jako generator przypadków z niezależną prawdą odniesienia. W pierwszej wersji wystarcza przeglądarka pokazująca raport operatorowi. **Nie uruchamiać ruchu Unitree G1**, nie przedstawiać fixture jako rzeczywistego pomiaru robota.

**Minimalny protokół:** Losowane scenariusze misji naprawdę zakończonych, częściowo ukończonych i błędnie przypisanych do obiektu. Porównać trzy sposoby prezentacji: (a) komunikat deklaratywny, (b) status binarny, (c) lista wymaganych zdjęć, ich identyfikatorów i braków z kontrolą dowodów. Ground truth musi być tworzony niezależnie od zawartości wyświetlanego raportu, a skrypty muszą różnicować błędy, nie tylko liczbę komunikatów.

**Pierwszorzędowy wynik:** Udział **fałszywych akceptacji misji nieukończonych**, z rozbiciem na typ niedostatecznego dowodu. Drugorzędowo trafne zaakceptowanie misji kompletnych, czas decyzji, pewność decyzji i obciążenie. Brak poprawy ponad kontrolę z informacją o brakach lub przewaga wynikająca wyłącznie z ilości tekstu jest przesłanką do NO-GO.

**Odrębność:** W [RVI P08](https://github.com/MatPomGit/arc-rvi) główny przedmiot to skuteczność wykonania robotycznej misji; RVI P06 bada automatyczną ocenę jakości zdjęć. Planowany HRI Safety M08 dotyczy bezpieczeństwa i subiektywnego zaufania w kontakcie człowiek–robot. Tutaj pierwszorzędowym problemem jest **poprawność osądu operatora na podstawie niekompletnego materiału dowodowego**, a nie fizyczna skuteczność robota ani jego bezpieczeństwo.

**Bramki:** formalne sprawdzenie nowości względem literatury human–automation oversight i automation bias, niezależny scoring scenariuszy, rozłączne zbiory generujące i testowe, plan mocy/precyzji, właściwa kwalifikacja etyczna. Po ewentualnym wykorzystaniu fizycznych danych G1 dodatkowo wymagana jest jego odrębna kwalifikacja i zgoda na badania.

## Status portfolio

`MSC-RVI-P09` jest **IDEA_HOLD**. Nie przenosi protokołu RVI ani jego danych do ARC Robo, nie stanowi wpisu o zakończonej pracy i nie zatwierdza nowego manuskryptu. Publiczny katalog projektów/programu wymaga osobnej decyzji, zgodnie z zasadami repozytorium.