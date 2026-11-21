"""Write tapestry.html: a self-contained, zoomable, hoverable version of the grid."""
import json

from cells import cell
from render import short_label

K_MAX, N_MAX = 64, 100

rows = []
for k in range(1, K_MAX + 1):
    for n in range(k + 1, N_MAX + 1):
        c = cell(k, n - k)
        rows.append([k, n, c["group"], c["status"], c["source"], c["evidence"], c["note"],
                     c["rank"] if c["rank"] != "" else -1,
                     c["torsion_order"] if c["torsion_order"] != "" else -1,
                     c["knotted"], short_label(k, n - k)])

HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Haefliger knot tapestry</title>
<style>
:root{color-scheme:light;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--line:#d9d7d0;
 --blue:#2a78d6;--orange:#eb6834;--aqua:#1baf7a;--zero:#eceae5;--unknown:#c9c7c0;--special:#f4f3ef;--hatch:#8f8d85}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--line:#3a3936;
 --blue:#3987e5;--orange:#d95926;--aqua:#199e70;--zero:#2b2b29;--unknown:#4b4a45;--special:#232322;--hatch:#7a786f}}
:root[data-theme="dark"]{color-scheme:dark;--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--line:#3a3936;
 --blue:#3987e5;--orange:#d95926;--aqua:#199e70;--zero:#2b2b29;--unknown:#4b4a45;--special:#232322;--hatch:#7a786f}
*{box-sizing:border-box}
body{margin:0;background:var(--surface);color:var(--ink);font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
header{padding:14px 16px 6px;max-width:1100px}
h1{font-size:19px;margin:0 0 4px}
p{margin:0 0 8px;color:var(--ink2)}
.bar{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:6px 16px}
.bar button,.bar select{font:inherit;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:5px 10px;cursor:pointer}
.bar button[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
#wrap{position:relative;margin:0 16px;border:1px solid var(--line);border-radius:8px;overflow:hidden;height:min(72vh,820px);touch-action:none}
svg{width:100%;height:100%;display:block;cursor:grab}
svg.drag{cursor:grabbing}
.lab{font-size:.36px;text-anchor:middle;dominant-baseline:central;pointer-events:none}
.ax{font-size:.42px;fill:var(--ink2);text-anchor:middle;dominant-baseline:central;pointer-events:none}
#tip{position:absolute;pointer-events:none;max-width:340px;background:var(--surface);color:var(--ink);border:1px solid var(--ink2);border-radius:8px;padding:8px 10px;font-size:12.5px;display:none;box-shadow:0 4px 14px rgba(0,0,0,.18)}
#tip b{font-size:13.5px}
#tip .m{color:var(--ink2)}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;padding:8px 16px;color:var(--ink)}
.legend span{display:inline-flex;align-items:center;gap:6px}
.sw{width:14px;height:14px;border-radius:3px;display:inline-block;border:1px solid var(--line)}
footer{padding:4px 16px 18px;color:var(--ink2);max-width:1100px}
a{color:inherit}
</style></head><body>
<header><h1>Haefliger knot tapestry</h1>
<p>Each cell is the group of isotopy classes of smooth embeddings S<sup>k</sup> → S<sup>n</sup> (codimension q = n − k).
Scroll or pinch to zoom, drag to pan, hover a cell for its value, status and source. Complete for k ≤ 13; beyond that only general theorems are filled in and everything else is marked unknown.</p></header>
<div class="bar" role="group" aria-label="Layer">
 <button data-layer="knot" aria-pressed="true">Knotted or not</button>
 <button data-layer="order" aria-pressed="false">Torsion order</button>
 <button data-layer="prime" aria-pressed="false">Primes</button>
 <label id="pl" style="display:none">prime <select id="prime"><option>2</option><option>3</option><option>5</option><option>7</option></select></label>
 <span style="flex:1"></span>
 <button id="zin" aria-label="Zoom in">+</button><button id="zout" aria-label="Zoom out">−</button><button id="reset">Reset view</button>
</div>
<div id="wrap"><svg id="svg" role="img" aria-label="Grid of knot groups by sphere dimension k and ambient dimension n"><defs>
<pattern id="hatch" width=".22" height=".22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width=".22" height=".22" fill="var(--unknown)"/><line x1="0" y1="0" x2="0" y2=".22" stroke="var(--hatch)" stroke-width=".05"/></pattern></defs>
<g id="cells"></g><g id="axes"></g></svg><div id="tip"></div></div>
<div class="legend" id="legend"></div>
<footer>Table view: <a href="table.csv">table.csv</a> (one row per cell, with status and source). Method and caveats: <a href="REPORT.md">REPORT.md</a>.
Label key: 12 = Z/12, 2² = Z/2 + Z/2, Z+6 = Z + Z/6, (60) = finite of order 60 with structure not determined.</footer>
<script>
const D=__DATA__;
const KM=__KM__,NM=__NM__;
const RAMPL=["#cde2fb","#b7d3f6","#86b6ef","#6da7ec","#5598e7","#3987e5","#256abf","#1c5cab","#104281","#0d366b"];
const svg=document.getElementById('svg'),gc=document.getElementById('cells'),ga=document.getElementById('axes'),tip=document.getElementById('tip');
let layer='knot',prime=2;
const NS='http://www.w3.org/2000/svg';
function dark(){const t=document.documentElement.dataset.theme;return t?t==='dark':matchMedia('(prefers-color-scheme: dark)').matches}
function ramp(o){const r=dark()?RAMPL.slice().reverse():RAMPL;const j=Math.min(9,Math.max(0,Math.round(Math.log2(o))-1));return r[j]}
function lum(h){const c=[1,3,5].map(i=>parseInt(h.substr(i,2),16)/255);return .2126*c[0]+.7152*c[1]+.0722*c[2]}
function style(c){ // returns {fill,thread,label,hole}
 const [k,n,g,st,src,ev,note,rank,ord,kn,lab]=c,q=n-k;let fill,thread=false,label=lab,hole=false;
 if(layer==='knot'){
  if(q===1){fill=k===3?'url(#hatch)':'var(--special)';label=k===3?'?':''}
  else if(q===2){fill='var(--aqua)';label=''}
  else if(st==='unknown'){fill='url(#hatch)';label='?'}
  else if(kn==='no'){fill='var(--zero)';hole=2*q<=k+3;label=hole?'0':''}
  else fill=rank===1?'var(--orange)':'var(--blue)';
 }else{
  if(q<=2){fill='var(--special)';label=''}
  else{thread=rank===1;
   if(ord<0){fill='url(#hatch)';label=thread?'':'?'}
   else if(layer==='order'){fill=ord>1?ramp(ord):'var(--zero)';if(2*q>k+3)label=''}
   else{fill=ord%prime===0?'var(--blue)':'var(--zero)';label=''}}
 }
 return {fill,thread,label,hole}}
function draw(){
 gc.textContent='';
 for(const c of D){const [k,n]=c,s=style(c),y=NM-n;
  const r=document.createElementNS(NS,'rect');r.setAttribute('x',k-.47);r.setAttribute('y',y-.47);r.setAttribute('width',.94);r.setAttribute('height',.94);
  r.setAttribute('fill',s.fill);if(s.hole){r.setAttribute('stroke','var(--ink)');r.setAttribute('stroke-width',.07)}
  r.__c=c;gc.appendChild(r);
  if(s.thread){const t=document.createElementNS(NS,'rect');t.setAttribute('x',k-.47);t.setAttribute('y',y-.5);t.setAttribute('width',.2);t.setAttribute('height',1);t.setAttribute('fill','var(--orange)');t.setAttribute('pointer-events','none');gc.appendChild(t)}
  if(s.label){const t=document.createElementNS(NS,'text');t.setAttribute('x',k+(s.thread?.1:0));t.setAttribute('y',y);t.setAttribute('class','lab');
   let ink='var(--ink)';if(s.fill[0]==='#')ink=lum(s.fill)<.42?'#fff':'#0b0b0b';else if(s.fill==='var(--blue)'||s.fill==='var(--orange)')ink=dark()?'#0b0b0b':'#fff';
   if(s.fill==='var(--orange)'&&!dark())ink='#0b0b0b';
   t.setAttribute('fill',ink);if(s.label.length>5)t.setAttribute('style','font-size:.25px');t.textContent=s.label;gc.appendChild(t)}}
 legend()}
function axes(){ga.textContent='';
 for(let k=1;k<=KM;k++){const t=document.createElementNS(NS,'text');t.setAttribute('x',k);t.setAttribute('y',NM-k+.1);t.setAttribute('class','ax');t.textContent=k;ga.appendChild(t)}
 for(let n=2;n<=NM;n++){const t=document.createElementNS(NS,'text');t.setAttribute('x',.2);t.setAttribute('y',NM-n);t.setAttribute('class','ax');t.textContent=n;ga.appendChild(t)}
 const a=document.createElementNS(NS,'text');a.setAttribute('x',12);a.setAttribute('y',NM-3);a.setAttribute('class','ax');a.setAttribute('style','font-size:.6px');a.textContent='k (sphere) → on the diagonal;  n (ambient) ↑ at the left';ga.appendChild(a)}
function legend(){const L=document.getElementById('legend');const sw=(c,t,h)=>`<span><i class="sw" style="background:${c}${h?';outline:2px solid var(--ink);outline-offset:-2px':''}"></i>${t}</span>`;
 const hatch='repeating-linear-gradient(45deg,var(--unknown),var(--unknown) 3px,var(--hatch) 3px,var(--hatch) 4px)';
 if(layer==='knot')L.innerHTML=sw('var(--blue)','knotted, finite group')+sw('var(--orange)','knotted, infinite group')+sw('var(--zero)','unknotted (0)')+sw('var(--zero)','hole: 0 inside the wedge',1)+sw(hatch,'unknown')+sw('var(--aqua)','q = 2: always knotted')+sw('var(--special)','q = 1: image unknotted');
 else if(layer==='order')L.innerHTML=sw(ramp(2),'torsion order 2')+sw(ramp(32),'32')+sw(ramp(1024),'≥ 1024 (log scale)')+sw('var(--orange)','thread: infinite group')+sw('var(--zero)','torsion trivial')+sw(hatch,'torsion unknown');
 else L.innerHTML=sw('var(--blue)','prime '+prime+' divides the torsion order')+sw('var(--zero)','it does not')+sw('var(--orange)','thread: infinite group')+sw(hatch,'torsion unknown')}
// view box: start on the determined block
let vb;function home(){const r=svg.getBoundingClientRect(),h=27,w=h*r.width/r.height;vb={x:-.6,y:NM-27.5,w:w,h:h};apply()}
function apply(){svg.setAttribute('viewBox',`${vb.x} ${vb.y} ${vb.w} ${vb.h}`)}
function zoom(f,cx,cy){const r=svg.getBoundingClientRect();const px=cx===undefined?.5:(cx-r.left)/r.width,py=cy===undefined?.5:(cy-r.top)/r.height;
 const nw=Math.min(140,Math.max(4,vb.w*f)),nh=nw*vb.h/vb.w;vb.x+=(vb.w-nw)*px;vb.y+=(vb.h-nh)*py;vb.w=nw;vb.h=nh;apply()}
function fit(){const r=svg.getBoundingClientRect();vb.h=vb.w*r.height/r.width;apply()}
svg.addEventListener('wheel',e=>{e.preventDefault();zoom(e.deltaY>0?1.15:1/1.15,e.clientX,e.clientY)},{passive:false});
let drag=null;const pts=new Map();let pinch=0;
svg.addEventListener('pointerdown',e=>{svg.setPointerCapture(e.pointerId);pts.set(e.pointerId,e);drag={x:e.clientX,y:e.clientY};svg.classList.add('drag')});
svg.addEventListener('pointermove',e=>{if(pts.has(e.pointerId))pts.set(e.pointerId,e);
 if(pts.size===2){const [a,b]=[...pts.values()],d=Math.hypot(a.clientX-b.clientX,a.clientY-b.clientY);if(pinch)zoom(pinch/d,(a.clientX+b.clientX)/2,(a.clientY+b.clientY)/2);pinch=d;return}
 if(drag&&pts.size===1){const r=svg.getBoundingClientRect();vb.x-=(e.clientX-drag.x)*vb.w/r.width;vb.y-=(e.clientY-drag.y)*vb.h/r.height;drag={x:e.clientX,y:e.clientY};apply()}
 hover(e)});
function up(e){pts.delete(e.pointerId);pinch=0;if(!pts.size){drag=null;svg.classList.remove('drag')}}
svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);svg.addEventListener('pointerleave',()=>tip.style.display='none');
function hover(e){const el=document.elementFromPoint(e.clientX,e.clientY);const c=el&&el.__c;if(!c||drag&&pts.size){if(!c)tip.style.display='none';return}
 const [k,n,g,st,src,ev,note,rank,ord]=c;
 tip.innerHTML=`<b>S<sup>${k}</sup> in S<sup>${n}</sup></b> <span class="m">(q = ${n-k})</span><br>${g}<br><span class="m">status:</span> ${st}`+(ord>0&&n-k>2?`<br><span class="m">torsion order:</span> ${ord}`:'')+(src?`<br><span class="m">source:</span> ${src}`:'')+(ev?`<br><span class="m">evidence:</span> ${ev}`:'')+(note?`<br><span class="m">note:</span> ${note}`:'');
 tip.style.display='block';const w=document.getElementById('wrap').getBoundingClientRect();let x=e.clientX-w.left+14,y=e.clientY-w.top+14;
 if(x+350>w.width)x=Math.max(4,x-370);if(y+tip.offsetHeight>w.height)y=Math.max(4,y-tip.offsetHeight-24);tip.style.left=x+'px';tip.style.top=y+'px'}
document.querySelectorAll('[data-layer]').forEach(b=>b.onclick=()=>{layer=b.dataset.layer;document.querySelectorAll('[data-layer]').forEach(x=>x.setAttribute('aria-pressed',x===b));document.getElementById('pl').style.display=layer==='prime'?'':'none';draw()});
document.getElementById('prime').onchange=e=>{prime=+e.target.value;draw()};
document.getElementById('zin').onclick=()=>zoom(1/1.4);document.getElementById('zout').onclick=()=>zoom(1.4);document.getElementById('reset').onclick=home;
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',draw);addEventListener('resize',fit);
axes();draw();home();
</script></body></html>
"""

html = (HTML.replace("__DATA__", json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
        .replace("__KM__", str(K_MAX)).replace("__NM__", str(N_MAX)))
open("tapestry.html", "w", encoding="utf-8").write(html)
print("wrote tapestry.html", len(html) // 1024, "KiB,", len(rows), "cells")
