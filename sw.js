const CACHE = 'exam-app-v2';

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll([
      './index.html',
      './manifest.json',
      './icon.svg',
      './icon-192.png',
      './icon-512.png',
      './builtin-bank.json',
      './lib/xlsx.full.min.js'
    ]))
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});

// Clean old cache
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE).map(k => caches.delete(k))
    ))
  );
});
