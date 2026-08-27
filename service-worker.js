const CACHE='tc-antalya-081-beta2';
const CORE=[
'./','./index.html','./app.css','./app.js','./manifest.webmanifest','./version.json','./apple-touch-icon.png','./icon-192.png','./icon-512.png','./icon-maskable-192.png','./icon-maskable-512.png','./assets/logo-tr.png','./assets/app-icon-day.png','./assets/offline-map.svg',
'./assets/photos/hadrian.jpg','./assets/photos/konyaalti.jpg','./assets/photos/duden.png','./assets/photos/perge.jpg','./assets/photos/kursunlu.jpg','./assets/photos/phaselis.jpg',
'./assets/generated/hotel.jpg',
'./assets/generated/coffee.jpg',
'./assets/generated/shop.jpg',
'./assets/generated/food.jpg',
'./assets/generated/wc.jpg',
'./assets/generated/attraction.jpg',
'./assets/generated/marina.jpg',
'./assets/generated/park.jpg',
'./assets/generated/historic.jpg',
'./assets/generated/museum.jpg',
'./assets/generated/beach.jpg',
'./assets/generated/waterfall.jpg',
'./assets/generated/ancient.jpg',
'./assets/generated/bar.jpg',
'./assets/generated/generic.jpg',
'./assets/placeholders/historic.svg','./assets/placeholders/museum.svg','./assets/placeholders/beach.svg','./assets/placeholders/park.svg','./assets/placeholders/waterfall.svg','./assets/placeholders/ancient.svg','./assets/placeholders/food.svg','./assets/placeholders/coffee.svg','./assets/placeholders/bar.svg','./assets/placeholders/shop.svg','./assets/placeholders/wc.svg','./assets/placeholders/hotel.svg','./assets/placeholders/attraction.svg','./assets/placeholders/marina.svg'
];
const OPTIONAL_REMOTE=['https://unpkg.com/leaflet@1.9.4/dist/leaflet.css','https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(async c=>{await c.addAll(CORE);await Promise.all(OPTIONAL_REMOTE.map(async u=>{try{const r=await fetch(u,{mode:'cors'});if(r.ok)await c.put(u,r.clone())}catch(_){}}))}).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
 if(e.request.method!=='GET') return;
 const u=new URL(e.request.url);
 if(u.pathname.endsWith('/version.json')||u.pathname.endsWith('version.json')){e.respondWith(fetch(e.request,{cache:'no-store'}).then(r=>{const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{});return r}).catch(()=>caches.match(e.request)));return;}
 const dynamic=u.hostname.includes('basemaps.cartocdn.com')||u.hostname.includes('unpkg.com')||u.hostname.includes('wikipedia.org')||u.hostname.includes('wikimedia.org')||u.hostname.includes('routing.openstreetmap.de');
 if(dynamic){
   e.respondWith(caches.open(CACHE).then(async c=>{
     const hit=await c.match(e.request); if(hit) return hit;
     try{const r=await fetch(e.request); if(r&&(r.ok||r.type==='opaque')) c.put(e.request,r.clone()).catch(()=>{}); return r;}catch(err){return hit||Response.error();}
   })); return;
 }
 e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(r=>{const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{});return r}).catch(()=>caches.match('./index.html'))));
});
