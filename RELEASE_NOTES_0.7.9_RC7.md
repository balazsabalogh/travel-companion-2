# 0.7.9 RC7 · iPhone hotfix

- Generated POI fallback photos are embedded in app.js, so hotel / bakery / Migros and category fallbacks no longer depend on a newly-created deploy folder or service-worker timing.
- Planner swipe action colors are forcibly cleared on pointer/touch cancel, pointer loss, window blur and incomplete gestures.
- Full day carousel native iOS scroll indicator is covered/disabled; the dot pager is the only page indicator.
- Half route list gets extra bottom scroll padding so the final visible card can clear the action row.
- Navigation code is unchanged from RC6.
