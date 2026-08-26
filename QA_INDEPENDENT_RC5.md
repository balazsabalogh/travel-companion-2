# RC5 kétlépcsős QA

## 1. Fejlesztői ellenőrzés
- JS / service worker syntax
- asset és PWA-csomag ellenőrzés
- menü/sheet állapotok
- Útiterv tap/hold/handle/reorder/swipe/persistence
- Sonar távolság és panel
- POI mini + műveleti sorrend
- GPS navigáció + Apple/Google Transit
- fullscreen rétegzés

Eredmény: lásd `QA_PASS1_RC5.txt` és `QA_UI_RC5_OUTPUT.txt`.

## 2. Független audit
Második körben nem a patch-listát, hanem regressziókat és töréspontokat kerestünk: gyors tabváltás, egymásra maradó panelek, 390 px mobil szélesség, route full/half váltás, fullscreen map bleed, navigation steps visszatérés, mini POI újranyitás.

Eredmény: lásd `QA_PASS2_SOURCE_RC5.txt` és `QA_PASS2_UI_RC5.txt`.

## Korlát
A valódi iOS PWA safe-area, fizikai GPS-mozgás és az Apple/Google Maps appátadás csak cél-iPhone-on igazolható 100%-osan.
