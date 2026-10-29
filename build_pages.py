#!/usr/bin/env python3
"""Generate BlasterTV subpages (packages, features, channels, blog, faq)
from the homepage source, and repoint homepage nav/footer to the new pages."""
import re, pathlib

SRC = pathlib.Path('/home/hatch/workspace/your_files/blastertv-new-design')
html = (SRC / 'index.html').read_text()

def section(name, end_marker):
    """Extract HTML between <!-- NAME --> and end_marker."""
    start = html.index(f'<!-- {name} -->')
    end = html.index(end_marker, start)
    return html[start:end].strip()

FEATURES = section('FEATURES', '<!-- PRICING -->')
PRICING  = section('PRICING', '<!-- CHANNELS -->')
CHANNELS = section('CHANNELS', '<!-- HOW IT WORKS -->')
HOWTO    = section('HOW IT WORKS', '<!-- ORDER / TRIAL -->')
BLOG     = section('BLOG', '<!-- FAQ -->')
FAQ      = section('FAQ', '<!-- FINAL CTA -->')
FINALCTA = section('FINAL CTA', '</main>')

HEADER = '''<header class="site"><div class="wrap nav">
<a class="logo" href="index.html">Blaster<b>TV</b></a>
<nav class="navlinks"><a href="packages.html">Packages</a><a href="features.html">Features</a><a href="channels.html">Channels</a><a href="blog.html">Blog</a><a href="faq.html">FAQ</a></nav>
<a class="btn btn-primary btn-sm" href="packages.html">Get Free Trial</a>
</div></header>'''

FOOTER = '''<footer><div class="wrap">
<div class="footgrid">
<div><div class="logo" style="margin-bottom:10px">Blaster<b>TV</b></div><p>Premium IPTV subscriptions for Firestick, Smart TV and Android — with UK support, instant activation and anti-freeze 4K streaming.</p></div>
<div><h4>Packages</h4><p><a href="packages.html">1-Month IPTV</a><br><a href="packages.html">6-Month IPTV</a><br><a href="packages.html">12-Month IPTV — Best Value</a><br><a href="https://wa.me/447877815180?text=Hi%20BlasterTV%2C%20I%27d%20like%20a%20free%2024h%20trial%20please.">Free 24h Trial</a></p></div>
<div><h4>Guides</h4><p><a href="blog.html">IPTV on Firestick Guide</a><br><a href="blog.html">Best IPTV UK Comparison</a><br><a href="blog.html">Fix IPTV Buffering</a><br><a href="blog.html">Watch Live Football</a></p></div>
<div><h4>Support</h4><p><a href="faq.html">FAQs</a><br><a href="https://wa.me/447877815180" target="_blank" rel="noopener">Contact on WhatsApp — +44 7877 815180</a><br><a href="channels.html">Channel List</a><br><a href="features.html">Setup Help</a></p></div>
</div>
<div class="keywords"><strong style="color:var(--text)">Popular searches:</strong> best IPTV UK · IPTV subscription UK · Firestick IPTV packages · buy IPTV UK · premium IPTV service · cheap IPTV UK · 4K IPTV subscription · IPTV for Firestick 4K Max · IPTV Smart TV Samsung LG · live football IPTV · IPTV free trial UK · IPTV with EPG · anti-freeze IPTV · IPTV multi-room · IPTV movies and series VOD.<br><span>© 2026 BlasterTV. Please ensure you have the right to view content in your region and use streaming services responsibly.</span></div>
</div></footer>'''

TAIL = '''<a class="wa-float" href="https://wa.me/447877815180?text=Hi%20BlasterTV%2C%20I%27d%20like%20a%20free%2024h%20trial%20please." target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><span class="wa-ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></span></a>
<div class="sticky-cta"><a class="btn btn-ghost" style="background:var(--card)" href="packages.html">View Plans</a><a class="btn btn-primary" href="https://wa.me/447877815180?text=Hi%20BlasterTV%2C%20I%27d%20like%20a%20free%2024h%20trial%20please.">Free Trial →</a></div>
<div class="toast" id="toast">Copied — paste it in WhatsApp or email</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>
<script>
(function(){
  try{
    var canvas=document.getElementById('bg3d');
    var renderer=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:true});
    renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
    var scene=new THREE.Scene();
    var camera=new THREE.PerspectiveCamera(60,1,0.1,100); camera.position.z=14;
    var geo=new THREE.BufferGeometry(); var N=650; var pos=new Float32Array(N*3);
    for(var i=0;i<N*3;i++){ pos[i]=(Math.random()-0.5)*30; }
    geo.setAttribute('position', new THREE.BufferAttribute(pos,3));
    var mat=new THREE.PointsMaterial({color:0xFF9F1C,size:0.09,transparent:true,opacity:0.75});
    var pts=new THREE.Points(geo,mat); scene.add(pts);
    var mat2=new THREE.PointsMaterial({color:0x22D3EE,size:0.06,transparent:true,opacity:0.6});
    var pts2=new THREE.Points(geo.clone(),mat2); pts2.rotation.z=1.2; scene.add(pts2);
    var rings=[];
    for(var r=0;r<4;r++){
      var ring=new THREE.Mesh(new THREE.TorusGeometry(2.2+r*1.15,0.025,8,80), new THREE.MeshBasicMaterial({color:r%2?0x22D3EE:0xFF9F1C,transparent:true,opacity:0.35}));
      ring.position.set(6.5-(r%2)*3, 1.5-r*0.7, -2-r); ring.rotation.x=1.1; ring.rotation.y=0.4; scene.add(ring); rings.push(ring);
    }
    var t=0;
    function resize(){ var w=canvas.clientWidth||canvas.parentElement.clientWidth; var h=canvas.clientHeight||420; renderer.setSize(w,h,false); camera.aspect=w/h; camera.updateProjectionMatrix(); }
    resize(); window.addEventListener('resize',resize);
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    (function anim(){ requestAnimationFrame(anim); if(!reduced){ t+=0.003; pts.rotation.y=t; pts2.rotation.y=-t*0.7; rings.forEach(function(rg,idx){ rg.rotation.z=t*(0.4+idx*0.12); }); } renderer.render(scene,camera); })();
  }catch(e){}
})();

function setPeriod(p){
  document.getElementById('tShort').classList.toggle('on',p==='short');
  document.getElementById('tLong').classList.toggle('on',p==='long');
  document.querySelectorAll('.price').forEach(function(el){ var v=el.getAttribute(p==='short'?'data-short':'data-long'); var suffix=el.querySelector('small')?el.querySelector('small').outerHTML:''; el.innerHTML=v+suffix; });
}
function choosePlan(plan){ var s=document.getElementById('planSel'); for(var i=0;i<s.options.length;i++){ if(s.options[i].text===plan) s.selectedIndex=i; } document.getElementById('order').scrollIntoView({behavior:'smooth'}); showToast('Plan selected: '+plan); }
function orderText(){ var p=document.getElementById('planSel').value; var d=document.getElementById('devSel').value; return 'Hi BlasterTV, I want: '+p+' for my '+d+'. Please send my free trial / payment details.'; }
function sendViaWhatsApp(){ var url='https://wa.me/447877815180?text='+encodeURIComponent(orderText()); window.open(url,'_blank'); }
function copyDetails(){ var txt=orderText(); if(navigator.clipboard){ navigator.clipboard.writeText(txt).then(function(){showToast('Copied — paste it in WhatsApp or email');}); } else { showToast(txt); } }
function showToast(msg){ var t=document.getElementById('toast'); t.textContent=msg; t.classList.add('show'); setTimeout(function(){t.classList.remove('show')},2600); }
document.querySelectorAll('#blogTools button').forEach(function(btn){ btn.addEventListener('click',function(){ document.querySelectorAll('#blogTools button').forEach(function(b){b.classList.remove('on')}); btn.classList.add('on'); var f=btn.getAttribute('data-f'); document.querySelectorAll('#blogGrid .blog-card').forEach(function(card){ card.style.display=(f==='all'||card.getAttribute('data-cat')===f)?'flex':'none'; }); }); });
</script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>'''

# Head: reuse index.html head, swapping title/description/canonical/og:url
HEAD_SRC = html[html.index('<head>'):html.index('</head>') + len('</head>')]
STYLE = html[html.index('<style>'):html.index('</style>') + len('</style>')]

PRODUCT_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"Premium IPTV UK Subscription — Firestick IPTV Package","description":"IPTV subscription for Firestick, Smart TV and Android with live UK channels, sports and VOD in HD/4K.","brand":{"@type":"Brand","name":"BlasterTV"},"offers":{"@type":"Offer","priceCurrency":"GBP","price":"49.99","availability":"https://schema.org/InStock"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"2314"}}
</script>'''
FAQ_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is the best IPTV subscription in the UK?","acceptedAnswer":{"@type":"Answer","text":"The best IPTV UK subscription offers stable 4K streams, UK/US live channels, sports coverage, a large VOD library, EPG, and support for Firestick and Smart TV with instant activation."}},{"@type":"Question","name":"Does IPTV work on Amazon Firestick?","acceptedAnswer":{"@type":"Answer","text":"Yes. IPTV works on Firestick, Fire TV, Android TV, Samsung/LG Smart TVs, Android/iOS phones, MAG boxes and Windows/Mac via popular IPTV player apps."}}]}
</script>'''

def make_head(title, desc, page, extra_ld=''):
    h = HEAD_SRC
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h, count=1)
    h = re.sub(r'<meta name="description" content=".*?"/>', f'<meta name="description" content="{desc}"/>', h, count=1)
    h = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://blastertv.vercel.app/{page}">', h, count=1)
    h = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://blastertv.vercel.app/{page}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content=".*?"/>', f'<meta property="og:title" content="{title}"/>', h, count=1)
    h = re.sub(r'<meta property="og:description" content=".*?"/>', f'<meta property="og:description" content="{desc}"/>', h, count=1)
    # strip existing JSON-LD blocks, re-add the ones we want
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', '', h, flags=re.S)
    h = h.replace('</head>', extra_ld + '\n</head>')
    return '<!doctype html>\n<html lang="en-GB">\n' + h

TOPBAR = '<div class="topbar">🔥 Limited Offer: 12-Month Plan — Extra 2 Months Free + Free Setup <span>· Ends soon</span></div>'

PAGES = {
    'packages.html': dict(
        title='IPTV Packages UK — Plans from £12.99 | BlasterTV',
        desc='BlasterTV IPTV packages UK: 1, 3, 6 and 12-month plans from £12.99. 28,000+ channels, 80,000+ VOD, anti-freeze 4K, WhatsApp support, free 24h trial.',
        ld=PRODUCT_LD,
        body=PRICING + '\n\n' + FINALCTA),
    'features.html': dict(
        title='BlasterTV Features — Anti-Freeze 4K IPTV, EPG & Catch-Up',
        desc='Why BlasterTV: anti-freeze UK servers, full EPG & catch-up, 80,000+ movies & series, VPN-friendly, multi-room options and 7-day UK WhatsApp support.',
        ld='',
        body=FEATURES + '\n\n' + HOWTO + '\n\n' + FINALCTA),
    'channels.html': dict(
        title='Channels — 28,000+ Live Channels & 80,000+ Movies | BlasterTV',
        desc='BlasterTV channel list: live Premier League & football, UK & US TV, movies & box sets, kids, news and international channels in HD/4K.',
        ld='',
        body=CHANNELS + '\n\n' + FINALCTA),
    'blog.html': dict(
        title='IPTV Blog & Guides — Firestick Tips & Comparisons | BlasterTV',
        desc='BlasterTV guides: install IPTV on Firestick, best IPTV UK comparisons, fix buffering, watch live football, IPTV legality UK and Smart TV setup.',
        ld='',
        body=BLOG + '\n\n' + FINALCTA),
    'faq.html': dict(
        title='IPTV FAQs — UK Firestick & Smart TV Questions | BlasterTV',
        desc='BlasterTV FAQs: devices, activation speed, free trial, internet speed, multi-room viewing and contracts — answered for UK IPTV viewers.',
        ld=FAQ_LD,
        body=FAQ + '\n\n' + FINALCTA),
}

for fname, cfg in PAGES.items():
    page = (make_head(cfg['title'], cfg['desc'], fname, cfg['ld'])
            + '\n<body>\n' + TOPBAR + '\n\n' + HEADER
            + '\n\n<main id="top">\n' + cfg['body'] + '\n</main>\n\n'
            + FOOTER + '\n\n' + TAIL)
    (SRC / fname).write_text(page)
    print('wrote', fname, len(page), 'bytes')

# --- patch index.html: nav/footer/CTA links -> pages ---
idx = html
idx = idx.replace('<nav class="navlinks"><a href="#packages">Packages</a><a href="#features">Features</a><a href="#channels">Channels</a><a href="#blog">Blog</a><a href="#faq">FAQ</a></nav>',
                  '<nav class="navlinks"><a href="packages.html">Packages</a><a href="features.html">Features</a><a href="channels.html">Channels</a><a href="blog.html">Blog</a><a href="faq.html">FAQ</a></nav>')
idx = idx.replace('<a class="btn btn-primary btn-sm" href="#packages">Get Free Trial</a>',
                  '<a class="btn btn-primary btn-sm" href="packages.html">Get Free Trial</a>')
idx = idx.replace('<a class="btn btn-primary" href="#packages">View IPTV Packages →</a>',
                  '<a class="btn btn-primary" href="packages.html">View IPTV Packages →</a>')
idx = idx.replace('<a class="btn btn-ghost" href="#blog">Setup Guides</a>',
                  '<a class="btn btn-ghost" href="blog.html">Setup Guides</a>')
idx = idx.replace('<div class="sticky-cta"><a class="btn btn-ghost" style="background:var(--card)" href="#packages">View Plans</a>',
                  '<div class="sticky-cta"><a class="btn btn-ghost" style="background:var(--card)" href="packages.html">View Plans</a>')
# footer links
for anchor, page in [('#packages', 'packages.html'), ('#features', 'features.html'),
                     ('#channels', 'channels.html'), ('#blog', 'blog.html'), ('#faq', 'faq.html')]:
    idx = idx.replace(f'href="{anchor}"', f'href="{page}"')
(SRC / 'index.html').write_text(idx)
print('patched index.html')

# --- sitemap ---
sm = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://blastertv.vercel.app/</loc>
    <lastmod>2026-10-13</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
'''
for fname in PAGES:
    sm += f'''  <url>
    <loc>https://blastertv.vercel.app/{fname}</loc>
    <lastmod>2026-10-13</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
sm += '</urlset>\n'
(SRC / 'sitemap.xml').write_text(sm)
print('wrote sitemap.xml')
