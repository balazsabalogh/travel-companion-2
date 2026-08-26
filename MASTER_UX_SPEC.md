# Travel Companion · Antalya — master UX spec (RC4)

Ez a dokumentum a 2026-08-25-i véglegesített működési alap. Korábbi, ezzel ellentétes specifikáció nem irányadó.

## 1. Alsó főmenü
Fix sorrend, minden térképes főnézetben ugyanott:
1. Útiterv
2. Napok
3. Kedvencek
4. középen Companion ország-embléma: rövid tap = fő/térkép, hosszú nyomás = Sonar
5. Beállítások
6. Értesítések
7. Navigáció

A Sonarnak nincs külön tab ikonja; a középső logó hosszú nyomásra indítja. Az aktív funkció vizuálisan kiemelt. A dock az iPhone home indicator fölött, stabil safe-area távolsággal marad. A középső logót egy sheet sem takarhatja.

## 2. Közös sheet engine
Rétegsorrend: térkép → térképes markerek/gombok → sheet → főmenü → középső embléma. Egy időben egy sheet/overlay lehet aktív; tabváltás mindig kitakarítja az előző átmeneti állapotot.

Állapotok:
- closed: nincs sheet
- mini: egy POI-kártyányi kompakt állapot
- two: kb. félképernyős munkanézet
- full: csak ott, ahol valóban kell

A sheet soha nem futhat a dock alá. Hosszú tartalom a sheet belsejében scrollozik. A felső fogópont nagy érintési területű, tapre és dragre reagál.

## 3. POI
- mini: kis kép + név + típus + távolság/gyaloglás
- half: kisebb kép, azonnal látható szöveg és műveletek
- full Guide: nagy hero, részletes tartalom
- full Guide X → ugyanaz a POI mini állapotban marad
- broken image, kérdőjel vagy üres képhely nem jelenhet meg; helyi fallback kötelező

## 4. Útiterv
- rövid tap az Útiterv ikonon → félképernyős szerkesztő
- hosszú nyomás → teljes képernyős szerkesztő
- teljes nézetben balra/jobbra swipe → napváltás
- ≡ fogantyú → állomássorrend átrendezése
- kártya vízszintes swipe: jobbra Megnéztem, balra Kihagyás
- swipe action layer pontosan a kártya mérete, nem maradhat piros/zöld toldás
- Térképről és Mentettekből hozzáadás
- sok kártyánál csak a lista scrollozik; a hozzáadás gombok hozzáférhetők maradnak
- módosított sorrend, hozzáadások, kivételek és aktív nap reload után is megmaradnak

## 5. Napok
- kompakt napválasztó alacsony, térkép-domináns
- egy tap választ napot
- teljes napnézet valóban opaque/full, egy jobb felső X-szel
- teljes nézetben vízszintes carousel

## 6. Sonar
- középső Companion logó indítja
- 250 m / 500 m / 1 km / 2 km egy sorban
- kategóriaszűrők aktívan a marker kategóriaszínét, kikapcsolva sötét állapotot használják
- sheet magassága a tartalomhoz igazodik, ne maradjon nagy üres navy rész
- Kedvencek elérhetők a Sonarból
- találatok idővel lejárnak; értesítési előzményből visszanyithatók

## 7. Navigáció
A jelenlegi navigációs panel vizuális kialakítása fagyasztott, csak hibajavítás végezhető rajta.

Companion belső navigáció:
- GPS watchPosition fut navigálás közben
- távolság/banner frissül
- útvonal időszakosan újrarajzolható mozgáskor
- következő cél és navigáció vége swipe működik

Tömegközlekedés MVP:
- Apple Maps Transit átadás
- Google Maps Transit átadás
- a Companion nem állít elő hamis busz/átszállási részleteket
- külső térképből visszatérve az eredeti POI mini kártyája áll helyre

## 8. Beállítások
Full-screen, opaque, egy jobb felső X. Csak valóban működő kapcsolók jelenhetnek meg. A béta/tesztkörnyezet információ itt van, a térkép szélén nincs külön béta badge.

## 9. Értesítések
A kialakítás stabilnak tekintendő. Nincs felső drag handle. Swipe műveletek működnek, badge frissül.

## 10. Offline / PWA
A POI-k, Guide, útiterv és helyi fallback képek csomagoltak. Leaflet és megnyitott térképcsempék online indítás után cache-elhetők. Offline állapotban az app ne állítsa, hogy nem cache-elt térképcsempék biztosan rendelkezésre állnak.

iOS: normál app icon. Android: külön adaptive/maskable ikon, ugyanazzal a földgömb + iránytű arculattal, safe-zone-ba húzva.

## 11. Build QA kapu
Minden build két külön körön megy át:
1. fejlesztői QA — kért változtatások + regressziók
2. független audit — teljes rendszer, állapotkezelés, persistence, hibás/ál-funkciók, csomag és mobil edge case-ek

Build csak mindkét kör után adható át tesztre.


## RC5 navigációs kiegészítés
- Companion navigáció térképes módban fut tovább.
- A navigációs banner tapra teljes képernyős **Navigáció · Lépések** nézet nyílik.
- A lépések a routing szolgáltatás step adataiból származnak, nem kitalált instrukciók.
- **Térképnézet** gombbal ugyanabba az aktív navigációba térünk vissza.
- Tömegközlekedéshez Apple Maps / Google Maps transit handoff marad.
