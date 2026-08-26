# RC8 QA summary

## Pass 1 — developer QA
- Static/source regression: 39/39 PASS
- 414 px mobile UI/gesture run: 21/21 PASS
- JS syntax: PASS
- Service worker syntax: PASS
- Local service-worker assets: PASS
- Bundled raster decode: PASS

## Pass 2 — independent developer audit
- 390 px independent stress/UI run: 20/20 PASS
- Rapid menu surface switching: PASS
- Compact Days alignment/contrast: PASS
- Full Days equal geometry including Day 4: PASS
- Route explicit previous/next + exclusive handle zone: PASS
- Logo short/long Sonar semantics: PASS
- Sonar radius row + close/ping: PASS
- Notification cancelled-swipe reset: PASS
- POI offline image fallback coverage: PASS
- Runtime JS exceptions: 0

## Frozen regression surface
The following navigation functions were compared against RC7 and intentionally left unchanged: transitUrl, openExternalTransit, showNavigationChoice, startNavigation, drawNavigationRoute, renderNavBanner, nextNavigationTarget, hideNavigationUI, endNavigation, navigationMain.
