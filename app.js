
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
(function(){var t=document.querySelector('.nav-toggle');if(!t)return;function close(){document.body.classList.remove('nav-open');t.setAttribute('aria-expanded','false');}t.addEventListener('click',function(e){e.stopPropagation();var o=document.body.classList.toggle('nav-open');t.setAttribute('aria-expanded',o);});document.querySelectorAll('.navlinks a').forEach(function(a){a.addEventListener('click',close);});document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});document.addEventListener('click',function(e){if(!e.target.closest('header.site'))close();});window.addEventListener('resize',function(){if(window.innerWidth>900)close();});})();
