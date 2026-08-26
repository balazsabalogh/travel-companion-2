# Travel Companion Antalya · 0.7.9 RC6

Final iPhone polish after live RC5 feedback.

- Companion logo: short tap = Sonar ping only; long press = opens Sonar view without automatically pinging.
- Sonar view gets an explicit close button and still closes automatically on menu change.
- Joined compact/half sheets align to the inset dock instead of spanning edge-to-edge.
- Full-screen surfaces remain opaque through the iPhone home-indicator area.
- Removed the native horizontal scrollbar from the full day selector; the dot indicator is the only page indicator.
- Planner green/red action layer exists only during an active horizontal swipe and resets on pointer cancel/lost capture.
- Added bundled local generated image fallbacks for every POI category plus dedicated hotel/bakery/shop/food/service fallbacks. Broken-image icons should never be user-visible.
- Service worker cache bumped to RC6 and includes all new generated fallback images.
