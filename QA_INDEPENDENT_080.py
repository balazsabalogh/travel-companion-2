from pathlib import Path
import re,json,sys,zipfile
root=Path('/mnt/data/tc090'); app=(root/'app.js').read_text(); css=(root/'app.css').read_text(); idx=(root/'index.html').read_text(); sw=(root/'service-worker.js').read_text()
checks=[]
def ck(n,c,d=''): checks.append((n,bool(c),d))
# JS/CSS structural sanity
ck('Balanced JS braces',app.count('{')==app.count('}'),f"{app.count('{')} / {app.count('}')}")
ck('Balanced CSS braces',css.count('{')==css.count('}'),f"{css.count('{')} / {css.count('}')}")
# New function definitions unique
for fn in ['startTour','renderTourStep','finishTour','checkForUpdate','refreshApp','routePathKm','optimizedRemainingOrder','showRouteOptimizer','openDayInGoogleMaps']:
    ck(f'Unique function {fn}',len(re.findall(rf'function\s+{re.escape(fn)}\s*\(',app))==1)
# Selector/handler contracts
for sel in ['data-route-opt','data-route-gmaps','data-tour','data-update-check','data-apply-opt','data-tour-next','data-tour-skip']:
    ck(f'UI selector {sel} has markup/handler',app.count(sel)>=2 if sel not in ['data-apply-opt','data-tour-next','data-tour-skip'] else app.count(sel)>=2,f'count={app.count(sel)}')
# Optimizer safety contract source-level
opt=re.search(r'function optimizedRemainingOrder\(\)\{(.+?)\}\nfunction showRouteOptimizer',app,re.S)
ck('Optimizer excludes done points',opt and '!state.done.has(id)' in opt.group(1))
ck('Optimizer excludes skipped points',opt and '!state.skipped.has(id)' in opt.group(1))
ck('Optimizer replaces only unfinished slots',opt and 'slots.forEach((slot,i)=>next[slot]=ordered[i])' in opt.group(1))
show=re.search(r'function showRouteOptimizer\(\)\{(.+?)\}\nfunction openDayInGoogleMaps',app,re.S)
ck('Optimizer captures return sheet before opening overlay',show and "returnSheet=state.sheet==='full'?'full':'two'" in show.group(1) and show.group(1).find('returnSheet=')<show.group(1).find('openOverlay('))
ck('Optimizer requires explicit user apply',show and 'data-apply-opt' in show.group(1) and "currentDay().route=[...x.route]" in show.group(1))
ck('Optimizer snapshots before mutation',show and "snapshotPlan('Optimalizálás előtt')" in show.group(1))
ck('Optimizer saves after apply',show and 'save();haptic' in show.group(1))
# Google export safety
ex=re.search(r'function openDayInGoogleMaps\(\)\{(.+?)\}\nfunction renderRouteSheet',app,re.S)
ck('Transit export does not build fake multi-stop transit',ex and "travel==='transit'&&ids.length>2" in ex.group(1) and 'openExternalTransit' in ex.group(1))
ck('Google export uses official Maps URL',ex and "https://www.google.com/maps/dir/" in ex.group(1))
# Onboarding contracts
ck('Existing users are not auto-interrupted',"if(!HAD_PRIOR_USE&&!state.tourSeen)" in app)
ck('Tour completion persisted',"localStorage.setItem('tc_tour_v2','1')" in app)
ck('Tour is replayable from settings',"data-tour>Indítás" in app and 'startTour(true)' in app)
ck('Tour has skip and finish',"data-tour-skip" in app and "last?'Kész':'Tovább'" in app)
# Update contracts
ck('Update check is silent on init','setTimeout(()=>checkForUpdate(true)' in app)
ck('Update check does not rely on cached version','cache:\'no-store\'' in app and "version.json?t=" in app)
ck('SW version fetch network-first',"pathname.endsWith('/version.json')" in sw and "fetch(e.request,{cache:'no-store'})" in sw)
ck('Update is opt-in via notification',"action:'update'" in app and "n.action==='update'" in app)
# Stable RC8 interaction contracts retained
contracts=[
 ('Logo short tap pings without opening Sonar',"longPress(logo,()=>" in app and 'runSonar();state.activeMenu' in app),
 ('Logo long press opens Sonar view',"openSonarMode(false)" in app),
 ('Route card swipe reset retained','function clearPlannerSwipeVisuals' in app),
 ('Notification swipe reset retained','function clearNotificationSwipeVisuals' in app),
 ('Route reorder uses dedicated drag handle',".planner-card .drag" in app and 'bindPlannerReorder' in app),
 ('Full day fixed hero geometry retained','Full Days cards all have identical geometry' in css),
 ('Compact day dock alignment retained','Compact Days is exactly dock-aligned' in css),
 ('Fullscreen map bleed guards retained','visibility:hidden!important' in css and 'leaflet-control-attribution' in css),
 ('Transit provider choices retained',"Apple · Tömegköz." in app and "Google · Tömegköz." in app),
 ('Navigation steps retained','Navigáció · Lépések' in app and 'navStepsHTML' in app),
]
for n,c in contracts: ck(n,c)
# POI type -> fallback coverage
poi_types=set(re.findall(r"type:'([^']+)'",app[:app.find('const DAYS')]))
generic_match=re.search(r'const GENERIC_PHOTO=\{([^}]+)\}',app)
generic_types=set(re.findall(r"([a-z]+):'\.\/assets\/generated",generic_match.group(1))) if generic_match else set()
ck('Every POI category has a generated fallback',poi_types<=generic_types,f'missing={sorted(poi_types-generic_types)}')
for f in generic_types:
    ck(f'Generated fallback exists: {f}',(root/f'assets/generated/{f}.jpg').exists())
# Manifest/icon coverage Android+iOS
man=json.loads((root/'manifest.webmanifest').read_text())
icons=man.get('icons',[])
ck('Android maskable 192',any(i.get('sizes')=='192x192' and 'maskable' in i.get('purpose','') for i in icons))
ck('Android maskable 512',any(i.get('sizes')=='512x512' and 'maskable' in i.get('purpose','') for i in icons))
ck('iOS apple touch icon exists',(root/'apple-touch-icon.png').exists())
# no visual risk from professional CSS: only additive classes + no main nav override in new block
newcss=css.split('0.8.0 beta1 — Professionalization pass.')[-1]
ck('Professional CSS does not reposition main nav','.main-nav{' not in newcss)
ck('Professional CSS does not change sheet geometry','.sheet.' not in newcss and '.sheet{' not in newcss)
ck('Professional CSS does not change navigation banner','.nav-banner' not in newcss)
# no accidental stale rc8 version refs in app/index/sw
ck('No stale rc8 app version',"APP_VERSION='0.7.9-rc8'" not in app)
ck('Index cache-buster updated','080-beta1' in idx and '079-rc8' not in idx)
# summary
p=sum(x[1] for x in checks)
for n,ok,d in checks: print(('PASS' if ok else 'FAIL'),n,d)
print(f'\n{p}/{len(checks)} PASS')
if p!=len(checks): sys.exit(1)
