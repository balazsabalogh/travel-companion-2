# RC8 · final iPhone check

1. Fully kill the installed PWA, then reopen it so RC8/service-worker cache is active.
2. **Napok compact:** panel edges align with the bottom dock; title/subtitle stay readable on bright photos.
3. **Napok full:** check Day 4 (Lara + Düden) specifically. Its card/hero must be the same size as every other day; only pager dots should be visible.
4. **Útiterv:** use `Előző nap` / `Következő nap`; whole-panel horizontal day switching is intentionally removed.
5. **Útiterv handle:** tap should toggle half/full; vertical drag should snap. The handle should be easy to grab above the content.
6. **Útiterv cards:** ≡ still reorders; horizontal card swipe still works; unfinished swipe must reset.
7. **Logo / Sonar:** short tap from Route/Days/Settings closes that panel and pings on the map without opening Sonar. Long press opens Sonar view.
8. **Sonar view:** Ping works without closing the view; 250 m / 500 m / 1 km / 2 km stay one row; X closes the Sonar panel.
9. **Notifications:** partially swipe a notification then cancel/release. No colored action background may remain stuck.
10. Rapidly switch: Útiterv → Napok → Kedvencek → Beállítások → Értesítések → Navigáció → Útiterv. Never allow two panels to remain open together.
11. Confirm Hotel/Migros/Fırıncı and itinerary cards never show `?`/broken-image placeholders.
12. Regression only: current Companion navigation, Lépések view, Navigation end and Apple/Google transit handoff should behave exactly as before.
