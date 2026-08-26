from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib,sys
root=Path('/mnt/data/tc090'); base=Path('/mnt/data/tc085_release')
app=(root/'app.js').read_text(); css=(root/'app.css').read_text(); idx=(root/'index.html').read_text(); sw=(root/'service-worker.js').read_text(); version=json.loads((root/'version.json').read_text())
checks=[]
def ck(name, cond, detail=''):
    checks.append((name,bool(cond),detail))
# version/build
ck('APP_VERSION is 0.8.0-beta1', "const APP_VERSION='0.8.0-beta1';" in app)
ck('version.json matches', version.get('version')=='0.8.0-beta1')
ck('service worker cache bumped', "tc-antalya-080-beta1" in sw)
ck('version.json uses network-first SW path', "version.json" in sw and "cache:'no-store'" in sw)
# professional features
for name,token in [
 ('Onboarding functions','function startTour('),('Tour replay setting','data-tour'),('Update check','function checkForUpdate('),('Update notification action',"n.action==='update'"),
 ('Route optimizer','function showRouteOptimizer('),('Optimizer requires apply','data-apply-opt'),('Google Maps day export','function openDayInGoogleMaps('),('Route smart buttons','route-smart-tools')]: ck(name,token in app)
# no fake POI ratings/open states added
ck('No fabricated rating system','rating:' not in app.lower() and '4.7 ★' not in app)
# stable rules from RC8
for name,token in [
 ('Logo short tap still runSonar','longPress(logo,()=>'),('Logo hold still opens Sonar view',"openSonarMode(false)"),('Transit Apple present',"openExternalTransit(next,'apple')"),('Transit Google present',"openExternalTransit(next,'google')"),
 ('Route reorder present','function bindPlannerReorder('),('Notification cancel reset','function clearNotificationSwipeVisuals('),('Day explicit prev/next','data-route-day'),('POI primary order','Guide')]: ck(name,token in app)
# UI integrity
ck('Coach overlay exists', 'id="coachOverlay"' in idx)
ck('No risky global button sizing','button{min-height:var(--tap)}' not in css)
ck('RC8 geometry CSS retained','0.7.9 RC8 — final layout/gesture polish' in css)
ck('Fullscreen map bleed guard retained','body.sheet-fullscreen #map' in css and 'body.overlay-fullscreen #map' in css)
ck('Generated image fallback retained','assets/generated/' in app and 'offlinePhoto' in app)
# asset refs in CORE exist
refs=re.findall(r"'\./([^']+)'", re.search(r"const CORE=\[(.*?)\];",sw,re.S).group(1))
missing=[r for r in refs if r and not (root/r).exists() and r not in ('',)]
ck('All service worker CORE assets exist', not missing, ', '.join(missing))
# html local refs exist
local_refs=re.findall(r'(?:href|src)="\.\/([^"?]+)',idx)
missing_html=[r for r in local_refs if not (root/r).exists()]
ck('All local HTML refs exist',not missing_html,', '.join(missing_html))
# route optimizer is preview-only (no automatic invoke in init)
init=re.search(r'function init\(\)\{(.+?)\}\ninit\(\);',app,re.S)
ck('Optimizer not auto-applied', bool(init) and 'showRouteOptimizer' not in init.group(1) and 'optimizedRemainingOrder' not in init.group(1))
# new user only onboarding
ck('Onboarding does not auto-open for existing users','!HAD_PRIOR_USE&&!state.tourSeen' in app)
# function extraction helper

def fn(src,name):
    marker=f'function {name}('
    i=src.find(marker)
    if i<0:return None
    b=src.find('{',i); depth=0; quote=None; esc=False; template_depth=[]
    # Lightweight JS brace scanner respecting strings/templates/comments well enough for these functions.
    j=b
    while j<len(src):
        ch=src[j]
        if quote:
            if esc: esc=False
            elif ch=='\\': esc=True
            elif ch==quote: quote=None
        else:
            if ch in "'\"`": quote=ch
            elif ch=='{': depth+=1
            elif ch=='}':
                depth-=1
                if depth==0:return src[i:j+1]
        j+=1
    return None
# compare critical nav functions against extracted RC8 backup in zip-extracted tc090 baseline not available; use previous release if exists
base_app=None
# user RC8 extraction before patch saved nowhere; recover from RC8 zip via zipfile
import zipfile
zip_path=Path('/mnt/data/Travel_Companion_Antalya_Beta_0.7.9_RC8_Final_Candidate.zip')
if zip_path.exists():
    with zipfile.ZipFile(zip_path) as z: base_app=z.read('app.js').decode()
critical=['fetchNavigationRoute','navDirection','navStepsHTML','closeNavigationSteps','showNavigationSteps','openExternalTransit','showNavigationChoice','startNavigation','renderNavBanner','endNavigation','renderNavSheet','navigationMain','drawNavigationRoute']
for n in critical:
    a=fn(app,n); b=fn(base_app,n) if base_app else None
    ck(f'Navigation regression: {n} unchanged',a is not None and b is not None and a==b)
# Summary
passed=sum(x[1] for x in checks)
for name,ok,detail in checks: print(('PASS' if ok else 'FAIL'),name,detail)
print(f'\n{passed}/{len(checks)} PASS')
if passed!=len(checks): sys.exit(1)
