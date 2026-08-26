# Professionalization pass · 0.8.0 beta1

A cél nem az RC8 újraírása, hanem a termékérzet javítása kevés, biztonságos funkcióval.

## Alapelv
- A már működő navigáció és panelrendszer nincs refaktorálva ebben a buildben.
- Új automatizmus csak **előnézet + jóváhagyás** formában módosíthat adatot.
- Új felhasználó kap rövid, interaktív tanítást; visszatérő felhasználó nem kap kéretlen onboardingot.
- Frissítés felismerhető, de nem történik automatikus, váratlan adat- vagy UI-váltás.

## Következő lehetséges 0.8.x lépések
- „Van +15 / +30 / +60 percem” útvonal menti Companion-ajánlás.
- Valós POI nyitvatartás/értékelés csak hiteles adatforrásból.
- Központi UI state-machine refaktor külön fejlesztői ágban, regressziós tesztekkel.
