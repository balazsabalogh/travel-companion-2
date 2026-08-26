# 0.7.9 RC5 — Live candidate

- Companion logó: tap = vissza a térkép/főnézetre; hosszú nyomás = Sonar.
- POI fő műveletek: Guide → Útitervhez/Kivétel → Navigáció.
- POI mini panel izolálva, kontraszt- és rétegződési hiba megszüntetve.
- Útiterv ≡ drag & drop újraírt, pointer tracking + autoscroll + mentés.
- Útiterv fogópont érzékelési felülete nagyobb; tap fél/full állapotot vált.
- Companion navigáció új Lépések teljes képernyős nézettel; nav banner tapra nyílik, Térképnézet gombbal tér vissza.
- A lépések a routing API valódi step adataiból készülnek; tömegközlekedés továbbra is Apple/Google Transit handoff.
- Fullscreen sheet/overlay alatt térkép, map control és Leaflet attribution nem szivároghat át.
- Navigációs route visszaáll overlay/menü bezárás után.
- Light/Auto basemap módban a Companion chrome kontrasztja stabilan sötét marad.
- Service worker cache bump: tc-antalya-079-rc5.
