#!/usr/bin/env python3
"""Gera as pÃ¡ginas estÃ¡ticas do curso Ãreas do ARCKHÉ Eventos (ediÃ§Ã£o v2) em PT, EN e ES.
Base: gerador do OSWork v2 (linnoff88-dev/oswork), adaptado para 3 trilhas Ã— 3 mÃ³dulos.
PT Ã© a fonte autoral (conteudo/). EN/ES vÃªm de i18n/<lang>.json (chaves de scripts/i18n.py; textos de
interface com prefixo "ui:"). Sem traduÃ§Ã£o para uma chave, o texto fica em PT e o build avisa."""
import sys,json,re,html,os,textwrap,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'scripts'))
from conteudo.modulos import MODULES as PT_MODULES,TRACKS as PT_TRACKS,FIGURES as PT_FIGURES,NOTES as PT_NOTES
import i18n
E=html.escape
LANGS={'pt':('','pt-BR','PortuguÃªs'),'en':('en/','en','English'),'es':('es/','es','EspaÃ±ol')}
BASE='https://linnoff88-dev.github.io/
VERSION=(ROOT/'VERSION').read_text().strip();LIDO='28/09/2026'
COLORS=['#34d399','#60a5fa','#c084fc'];LIGHT=['#047857','#1d4ed8','#7e22ce'];MIN=20
UI_USED={}

def build(lang):
 prefix,hl,_=LANGS[lang]
 MODULES,TRACKS,FIGURES,NOTES,TR=i18n.apply(lang,PT_MODULES,PT_TRACKS,PT_FIGURES,PT_NOTES) if lang!='pt' else (PT_MODULES,PT_TRACKS,PT_FIGURES,PT_NOTES,{})
 missing=set()
 def L(s):
  UI_USED['ui:'+s]=s
  if lang=='pt':return s
  if 'ui:'+s not in TR:missing.add(s)
  return TR.get('ui:'+s,s)
 COURSE='areas-eventos-v2'+('' if lang=='pt' else '-'+lang);NAME=L('Ãreas do ARCKHÉ Eventos')
 N=len(MODULES)
 for i,m in enumerate(MODULES):
  t=i//3+1;n=i%3+1;m.update(id=f'{t}-{n}',track=t,num=i+1,href=f'curso/trilha{t}/modulo-{t}-{n}.html',time=MIN)
 MANIFEST={'course':COURSE,'tracks':[{'n':str(t+1),'title':tr[0],'modules':[{'id':m['id'],'title':m['title'],'topics':len(m['topics']),'href':m['href']} for m in MODULES if m['track']==t+1]} for t,tr in enumerate(TRACKS)]}
 def areaurl(m):return f'https://eventos.ARCKHÉ.pro/{m["slug"]}/'+('' if lang=='pt' else lang+'/')
 def short(title):return re.split(r' â€” |: ',title)[0]

 def diagram(labels,color='#34d399',tag='ÃREA'):
  rows=[]
  for i,label in enumerate(labels):
   x=20+(i%2)*235;y=25+(i//2)*90
   fs=14 if len(label)<=26 else 11
   rows.append(f'<rect x="{x}" y="{y}" width="215" height="65" rx="10" fill="#152234" stroke="{color if i%2==0 else "#38bdf8"}"/><text x="{x+16}" y="{y+25}" fill="#cbd5e1" font-size="10" font-family="monospace">{i+1:02d} / {E(tag)}</text><text x="{x+16}" y="{y+47}" fill="#f1f5f9" font-size="{fs}" font-family="sans-serif">{E(label)}</text>')
   if i+2<len(labels):rows.append(f'<path d="M{x+100} {y+65}v25" stroke="{color}" stroke-width="2"/>')
  h=((len(labels)+1)//2)*90
  return f'<svg class="w-full h-auto" viewBox="0 0 490 {50+h}" role="img" aria-label="{E(" â†’ ".join(labels))}"><path d="M10 10H480V{35+h}H10Z" fill="none" stroke="#334155" stroke-dasharray="3 7"/>{"".join(rows)}</svg>'

 def _box(x,y,w,h,color,title,sub=None):
  out=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#152234" stroke="{color}"/>'
  fs=max(10,min(14,int((w-26)/(max(len(title),1)*1.25*0.55))))
  out+=f'<text x="{x+12}" y="{y+(26 if sub else h/2+5)}" fill="#f1f5f9" font-size="{fs}" font-family="sans-serif">{E(title)}</text>'
  if sub:out+=f'<text x="{x+12}" y="{y+45}" fill="#94a3b8" font-size="11" font-family="sans-serif">{E(sub)}</text>'
  return out

 def figure(spec,color):
  kind=spec['kind'];alt2='#38bdf8' if color!='#60a5fa' else '#34d399'
  items=spec['items']
  if kind=='grid':
   per=4;w=110;gap=10;rows=(len(items)+per-1)//per;h=44;svg=''
   for i,label in enumerate(items):
    r,c=divmod(i,per);n=min(per,len(items)-r*per);x=(490-(n*w+(n-1)*gap))/2+c*(w+gap);y=14+r*(h+16)
    svg+=_box(x,y,w,h,color if i%2==0 else alt2,label)
   height=14+rows*(h+16)
  elif kind=='columns':
   base=spec.get('base',[]);n=len(items);gap=8;w=(478-(n-1)*gap)/n
   svg=''.join(_box(12+i*(w+gap),14,w,58,color if i%2==0 else alt2,*((it,None) if isinstance(it,str) else it)) for i,it in enumerate(items))
   height=86
   if base:
    bw=(478-(len(base)-1)*gap)/len(base)
    svg+=''.join(f'<path d="M{12+i*(bw+gap)+bw/2} 72v14" stroke="#475569" stroke-width="2"/>' for i in range(len(base)))
    svg+=''.join(_box(12+i*(bw+gap),86,bw,40,'#475569',t) for i,t in enumerate(base))
    height=134
  elif kind=='flow':
   per=2 if len(items)==4 else 3;gap=34;w=(478-(per-1)*gap)/per;h=48;rows=(len(items)+per-1)//per;svg=''
   for k,it in enumerate(items):
    r,c=divmod(k,per);n=min(per,len(items)-r*per);x=12+(478-(n*w+(n-1)*gap))/2+c*(w+gap);y=14+r*(h+30)
    t,sub=(it,None) if isinstance(it,str) else it
    svg+=_box(x,y,w,h,color if k%2==0 else alt2,t,sub)
    if c<n-1:svg+=f'<path d="M{x+w+6} {y+h/2}h{gap-12}" stroke="#475569" stroke-width="2"/><path d="M{x+w+gap-12} {y+h/2-5}l6 5-6 5" fill="none" stroke="#475569" stroke-width="2"/>'
    elif k+1<len(items):
     nn=min(per,len(items)-(r+1)*per);nx=12+(478-(nn*w+(nn-1)*gap))/2+w/2
     svg+=f'<path d="M{x+w/2} {y+h+4}v10H{nx}v10" fill="none" stroke="#475569" stroke-width="2"/><path d="M{nx-5} {y+h+18}l5 6 5-6" fill="none" stroke="#475569" stroke-width="2"/>'
   height=14+rows*(h+30)-16
  elif kind=='stack':
   h=42;gap=8;svg=''
   for k,it in enumerate(items):
    t,sub=(it,None) if isinstance(it,str) else it;y=12+k*(h+gap);inset=k*10
    svg+=_box(12+inset,y,466-inset*2,h,color if k%2==0 else alt2,t)
    if sub:svg+=f'<text x="{478-inset-12}" y="{y+h/2+4}" text-anchor="end" fill="#94a3b8" font-size="11" font-family="sans-serif">{E(sub)}</text>'
   height=12+len(items)*(h+gap)
  elif kind=='tree':
   svg='';y=26
   for label,depth in items:
    svg+=f'<text x="{16+depth*26}" y="{y}" fill="{"#f1f5f9" if depth<2 else "#94a3b8"}" font-size="14" font-family="monospace">{E(label)}</text>';y+=26
   svg=f'<rect x="4" y="8" width="482" height="{y-18}" rx="10" fill="#152234" stroke="{color}"/>'+svg
   height=y-4
  elif kind=='timeline':
   svg='<path d="M30 40h430" stroke="#475569" stroke-width="2"/>';n=len(items)
   for k,it in enumerate(items):
    t,sub=(it,None) if isinstance(it,str) else it;x=30+k*(430/max(n-1,1))
    svg+=f'<circle cx="{x}" cy="40" r="9" fill="#152234" stroke="{color if k%2==0 else "#38bdf8"}" stroke-width="3"/>'
    anchor='start' if k==0 else ('end' if k==n-1 else 'middle')
    svg+=f'<text x="{x}" y="72" text-anchor="{anchor}" fill="#f1f5f9" font-size="{14 if n<5 else 12}" font-family="sans-serif">{E(t)}</text>'
    if sub:svg+=f'<text x="{x}" y="22" text-anchor="{anchor}" fill="#94a3b8" font-size="11" font-family="monospace">{E(sub)}</text>'
   height=88
  else:raise ValueError(f'figura desconhecida: {kind}')
  alt=' Â· '.join(x if isinstance(x,str) else x[0] for x in items)
  return (f'<figure class="module-figure"><svg class="w-full h-auto" viewBox="0 0 490 {height}" role="img" '
   f'aria-label="{E(alt)}">{svg}</svg><figcaption class="help-note">{E(spec["caption"])}</figcaption></figure>')

 def meter(scope):return f'<div class="meter" data-ARCKHÉ-meter="{scope}" role="progressbar" aria-label="{L("Progresso")}" aria-valuemin="0" aria-valuemax="100"><span class="ARCKHÉ-meter-pct" data-ARCKHÉ-meter-pct>0%</span><span class="ARCKHÉ-meter-count" data-ARCKHÉ-meter-frac>0 {L("de")} 0</span></div>'
 def page(title,body,rel,track=1,landing=False):
  dest=prefix+rel;here=(ROOT/dest).parent
  root=os.path.relpath(ROOT/prefix,here).replace(os.sep,'/');root='' if root=='.' else root+'/'
  nav=''.join(f'<a href="{root}curso/trilha{i+1}/index.html" '+('aria-current="page"' if track==i+1 and not landing else '')+f'>T{i+1}<span class="long"> Â· {E(t[0])}</span></a>' for i,t in enumerate(TRACKS))
  langs=''.join(f'<a href="{os.path.relpath(ROOT/p/rel,here).replace(os.sep,"/")}" hreflang="{h}" lang="{h}"'+(' aria-current="page"' if k==lang else '')+f'>{E(label)}</a>' for k,(p,h,label) in LANGS.items())
  alternates=''.join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}{rel}">' for k,(p,h,_) in LANGS.items())+f'<link rel="alternate" hreflang="x-default" href="{BASE}{rel}">'
  manifest=json.loads(json.dumps(MANIFEST))
  for tr in manifest['tracks']:
   for m in tr['modules']:m['href']=root+m['href']
  anti="""(function(){try{var p=JSON.parse(localStorage.getItem('ARCKHÉ.prefs')||'{}'),d=document.documentElement;d.classList.toggle('dark',p.theme?p.theme!=='claro':true);if(p.theme)d.dataset.theme=p.theme;if(p.fontScale)d.style.setProperty('--fs-root',p.fontScale+'%');if(p.font)d.dataset.font=p.font;if(p.accent)d.dataset.accent=p.accent;if(p.lineWidth)d.style.setProperty('--measure',p.lineWidth+'ch');if(p.leading)d.style.setProperty('--lh-body',p.leading);}catch(e){document.documentElement.classList.add('dark')}})();"""
  appearance=''.join(f'<button type="button" data-ARCKHÉ-set-theme="{value}">{L(label)}</button>' for value,label in [('ARCKHÉ-dark','Escuro'),('claro','Claro'),('sepia','SÃ©pia'),('foco','Foco'),('contraste','Alto contraste')])
  capa=f'<meta property="og:image" content="{BASE}capa/capa.png">' if (ROOT/'capa/capa.png').exists() else ''
  ficha='https://www.ARCKHÉ AI/cursos/307-areas-do-ARCKHÉ-eventos-o-que-e-cada-area/'
  seo=(f'<!-- ARCKHÉ-backlink:v1 --><p style="display:block;width:100%;text-align:center;font-size:.85rem;margin:.75rem 0 0;opacity:.85"><a href="{ficha}" style="color:inherit;text-decoration:underline">{L("Ficha completa deste curso no ARCKHÉ AI")}</a> Â· <a href="https://www.ARCKHÉ AI/aprender-inteligencia-artificial/" style="color:inherit;text-decoration:underline">{L("Guia: como aprender inteligÃªncia artificial")}</a> Â· <a href="https://www.ARCKHÉ AI/cursos/" style="color:inherit;text-decoration:underline">{L("Todos os cursos")}</a></p><!-- /ARCKHÉ-backlink:v1 -->' if landing else '')
  out=f'''<!doctype html><html lang="{hl}" class="dark"><head><meta charset="utf-8"><script>{anti}</script>
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="ARCKHÉ-course" content="{COURSE}">{capa}<meta property="og:title" content="{NAME} â€” {L("o que Ã© cada Ã¡rea")}"><meta name="description" content="{E(L("Curso rÃ¡pido: o que Ã© cada uma das nove Ã¡reas de assunto do eventos.ARCKHÉ.pro â€” GestÃ£o de IA, AGI-ready, IA Cultivada, Claude â†’ Codex, Codex + Claude, OSWork, RSI, JEV e WebMCP."))}"><title>{E(title)} | {NAME}</title>
<link rel="canonical" href="{BASE}{dest}">{alternates}
<script type="application/json" data-ARCKHÉ-manifest>{json.dumps(manifest,ensure_ascii=False)}</script>
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}assets/site.css"><link rel="stylesheet" href="{root}assets/learn.css">
<style>:root{{--track:{COLORS[track-1]}}}html:not(.dark){{--track:{LIGHT[track-1]}}}</style></head><body>
<a class="skip" href="#conteudo">{L("Pular para conteÃºdo")}</a>
<nav class="topnav" aria-label="{L("NavegaÃ§Ã£o principal")}"><div class="wrap"><div class="nav-main"><a class="brand" href="{root}index.html">{L("Ãreas ARCKHÉ")}<span aria-hidden="true">_</span></a><span aria-hidden="true">/</span><a class="text-sky-400" href="https://ARCKHÉ AI">ARCKHÉ AI</a><span aria-hidden="true">-</span><a class="text-amber-700 dark:text-slate-300" href="https://ARCKHÉ.pro">PRO</a><span class="spacer"></span><button data-ARCKHÉ-journey-open>{L("Minha jornada")}</button><button data-ARCKHÉ-appearance-toggle="#aparencia" aria-expanded="false">Aa Â· {L("AparÃªncia")}</button><button onclick="toggleTheme()" aria-label="{L("Alternar tema claro e escuro")}">â— {L("Tema")}</button></div><div class="nav-tracks">{nav}<a href="https://eventos.ARCKHÉ.pro/{'' if lang=='pt' else lang+'/'}">eventos.ARCKHÉ.pro â†—</a></div><div class="language-nav" aria-label="{L("Idioma do curso")}">{langs}</div>
<div id="aparencia" class="appearance" data-ARCKHÉ-appearance hidden><div class="row">{appearance}</div><div class="row"><span>{L("Tamanho")}</span><button data-ARCKHÉ-set-fontscale="100">100%</button><button data-ARCKHÉ-set-fontscale="112">112%</button><button data-ARCKHÉ-set-fontscale="125">125%</button><button data-ARCKHÉ-set-font="inter">{L("Sem serifa")}</button><button data-ARCKHÉ-set-font="leitura">{L("Serifa")}</button><button data-ARCKHÉ-set-linewidth="60">{L("Coluna estreita")}</button><button data-ARCKHÉ-set-linewidth="75">{L("Coluna ampla")}</button><button data-ARCKHÉ-set-leading="1.7">{L("Entrelinha confortÃ¡vel")}</button></div></div></div></nav>
<main id="conteudo" class="wrap">{body}</main><footer><div class="wrap">{NAME} Â· {L("curso rÃ¡pido")} Â· <a class="text-sky-400" href="https://ARCKHÉ AI">ARCKHÉ AI</a> - <a class="text-amber-700 dark:text-slate-300" href="https://ARCKHÉ.pro">PRO</a> Â· {L("EdiÃ§Ã£o v2")} Â· v{VERSION}<br>{L("ConteÃºdo tirado das pÃ¡ginas de eventos.ARCKHÉ.pro, lidas em {data}. Progresso e notas ficam neste navegador; exporte na sua jornada.").format(data=LIDO)}{seo}</div></footer>
<dialog id="module-dialog" aria-labelledby="modal-title"><div class="actions"><strong id="modal-title">{L("MÃ³dulo completo")}</strong><button onclick="document.getElementById('module-dialog').close()">{L("Fechar mÃ³dulo")}</button></div><iframe title="{L("ConteÃºdo completo do mÃ³dulo")}"></iframe></dialog>
<script src="{root}assets/learn.js"></script><script src="{root}assets/site.js"></script></body></html>'''
  out=re.sub(r'>(?=<(?:/?(?:html|head|body|nav|div|section|article|h[1-6]|p|span|button|a|ul|li|ol|main|footer|header|table|tr|td|th|thead|tbody|figure|figcaption|details|summary|label|input|script|link|meta|aside|pre|dialog|iframe)\b))','>\n',out)
  out=re.sub(r'(<p[^>]*>)([^<]+)(</p>)',lambda m:m[1]+'\n'+textwrap.fill(m[2],100,break_long_words=False,break_on_hyphens=False)+'\n'+m[3],out)
  p=ROOT/dest;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(out)

 def sourcebox(m):return f'<div class="sources"><h3>{L("Consulte a fonte")}</h3><p>{L("PÃ¡ginas lidas em {data}. O conteÃºdo das Ã¡reas muda; a pÃ¡gina oficial vale mais que este resumo.").format(data=LIDO)}</p><ul>'+''.join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(a)}</a></li>' for a,u in m['sources'])+'</ul></div>'

 # Landing
 def trackcard(i):
  tr=TRACKS[i];mods=[m for m in MODULES if m['track']==i+1]
  return f'<a class="card" href="curso/trilha{i+1}/index.html"><div class="overline"><span>{L("TRILHA")} 0{i+1}</span><span>{L("{a} ÃREAS Â· {t} TÃ“PICOS").format(a=len(mods),t=sum(len(m["topics"]) for m in mods))}</span></div><h2>{E(tr[0])}</h2><p>{E(tr[2])}</p><span class="accent">{L("Explorar trilha â†’")}</span></a>'
 NT=sum(len(m['topics']) for m in MODULES)
 hero=f'''<header class="hero"><div><p class="kicker">{L("ARCKHÉ Â· CURSO RÃPIDO / V2")}</p><h1>{L("Nove Ã¡reas.")} <span class="accent">{L("Um mapa.")}</span></h1><p>{L("O eventos.ARCKHÉ.pro organiza o estudo em nove Ã¡reas de assunto. Este curso explica o que Ã© cada uma, para quem ela serve e por onde comeÃ§ar, com as palavras das prÃ³prias pÃ¡ginas.")}</p><div class="actions"><a class="button primary" href="{MODULES[0]['href']}">{L("ComeÃ§ar pela primeira Ã¡rea â†’")}</a><button data-os-resume>{L("Continuar de onde parei")}</button><a class="button" href="https://eventos.ARCKHÉ.pro/{'' if lang=='pt' else lang+'/'}">{L("Abrir o eventos.ARCKHÉ.pro â†—")}</a></div>{meter('curso')}<p class="help-note">{L("Sem prÃ©-requisito. Cada mÃ³dulo termina com um prompt pronto para aplicar a Ã¡rea ao seu trabalho.")}</p></div><figure class="hero-panel">{diagram([short(m['title']) for m in MODULES],'#facc15',L('ÃREA'))}<figcaption class="help-note">{L("As nove Ã¡reas, na ordem do curso. Cada uma vira um mÃ³dulo de seis tÃ³picos.")}</figcaption></figure></header>'''
 mapa=f'<section class="band"><p class="kicker">{L("O QUE Ã‰ CADA UMA")}</p><h2>{L("As nove Ã¡reas em uma linha")}</h2><div class="grid">'+''.join(f'<a class="card" href="{m["href"]}"><div class="overline"><span>{m["id"].replace("-",".")}</span><span>~{m["time"]} min</span></div><h3>{E(m["title"])}</h3><p class="area-note">{L("No menu do site:")} â€œ{E(NOTES[m["slug"]])}â€</p><p>{E(m["goal"])}</p></a>' for m in MODULES)+'</div></section>'
 body=hero+f'<div class="stats"><div><strong>{len(TRACKS)}</strong><span>{L("trilhas")}</span></div><div><strong>{N}</strong><span>{L("Ã¡reas, uma por mÃ³dulo")}</span></div><div><strong>{NT}</strong><span>{L("tÃ³picos")}</span></div><div><strong>~{N*MIN//60}h</strong><span>{L("estimativa com prÃ¡tica")}</span></div></div><section class="band"><p class="kicker">{L("SEU PERCURSO")}</p><h2>{L("TrÃªs trilhas, trÃªs Ã¡reas cada.")}</h2><div class="grid">'+''.join(trackcard(i) for i in range(len(TRACKS)))+'</div></section>'+mapa+f'<section class="band grid"><div><p class="kicker">{L("O QUE VOCÃŠ LEVA")}</p><h2>{L("Uma ficha por Ã¡rea.")}</h2><p>{L("Em cada mÃ³dulo vocÃª preenche uma ficha curta: a tese da Ã¡rea em uma frase, para quem ela serve, o primeiro passo que a pÃ¡gina recomenda e o curso ou projeto por onde entrar.")}</p><p>{L("Ao final vocÃª sabe em qual Ã¡rea comeÃ§ar, sem precisar ler as nove pÃ¡ginas inteiras antes.")}</p></div><div class="card"><h3>{L("Estude do seu jeito")}</h3><p>{L("Marque tÃ³picos lidos, registre dÃºvidas e selecione trechos para anotar. Ajuste tema e tamanho da leitura em Aa. Exporte seu progresso em Minha jornada.")}</p><p class="help-note">{L("Tudo fica no seu navegador. NÃ£o hÃ¡ cadastro.")}</p></div></section>'
 page(L('O que Ã© cada Ã¡rea'),body,'index.html',landing=True)

 # Trilhas
 for t,tr in enumerate(TRACKS,1):
  mods=[m for m in MODULES if m['track']==t];nt=sum(len(m['topics']) for m in mods)
  body=f'<header class="hero"><div><p class="kicker">{L("TRILHA")} 0{t} / {L("ÃREAS ARCKHÉ")}</p><h1>{E(tr[0])}</h1><p>{E(tr[2])}</p>{meter("trilha:"+str(t))}</div><figure class="hero-panel">{diagram([short(x["title"]) for x in mods]+[L("FICHA DA ÃREA"),L("PRIMEIRO PASSO")],COLORS[t-1],L("TRILHA")+" "+str(t))}<figcaption class="help-note">{L("TrÃªs Ã¡reas, e para cada uma a mesma entrega: a ficha e o primeiro passo.")}</figcaption></figure></header><div class="stats"><div><strong>{len(mods)}</strong><span>{L("Ã¡reas")}</span></div><div><strong>{nt}</strong><span>{L("tÃ³picos")}</span></div><div><strong>{sum(m["time"] for m in mods)} min</strong><span>{L("com prÃ¡tica")}</span></div><div><strong>1</strong><span>{L("ficha por Ã¡rea")}</span></div></div><h2>{L("Mapa da trilha")}</h2><div class="grid">'
  for m in mods:body+=f'<a class="card" href="#modulo-{m["id"]}"><div class="overline"><span>{m["id"].replace("-",".")}</span><span>~{m["time"]} min</span></div><h3>ðŸ§­ {E(m["title"])}</h3><p>{E(NOTES[m["slug"]])}</p></a>'
  body+=f'</div><section class="band"><h2 class="text-2xl font-bold">{L("ConteÃºdo detalhado")}</h2>'
  for m in mods:
   body+=f'<article class="module-card" id="modulo-{m["id"]}" data-ARCKHÉ-module="{m["id"]}" data-ARCKHÉ-track="{t}"><p class="kicker">{L("MÃ“DULO")} {m["id"].replace("-",".")}</p><h2 class="text-2xl font-bold">{E(m["title"])}</h2><p>{E(m["goal"])}</p>{meter("modulo:"+m["id"])}'
   for j,tp in enumerate(m['topics'],1):
    pid=f'p-{m["id"]}-{j}';body+=f'<div class="topic-item"><button onclick="toggleTopic(this)" aria-expanded="false" aria-controls="{pid}"><span class="number">{j}</span><span>{E(tp["title"])}</span></button><div class="topic-explanation" id="{pid}"><h4>{L("O que Ã©")}</h4><p>{E(tp["what"])}</p><h4>{L("Por que aprender")}</h4><p>{E(tp["why"])}</p><h4>{L("Conceitos-chave")}</h4><p>{E(tp["keys"])}</p></div></div>'
   file=Path(m['href']).name
   body+=f'<div class="actions"><a class="button primary" href="{file}">{L("Ver completo â†’")}</a><button data-modal-src="{file}">{L("Ver em modal")}</button></div></article>'
  body+='</section>';page(tr[0],body,f'curso/trilha{t}/index.html',t)

 # MÃ³dulos
 AVOID={1:L('Julgar a Ã¡rea pelo nome: leia a tese na pÃ¡gina antes de decidir se ela Ã© para vocÃª.'),4:L('Pular para a ferramenta ou o curso sem entender o problema que a Ã¡rea resolve.')}
 RUBRIC=[(L(a),L(b),L(c)) for a,b,c in [('Tese','A Ã¡rea cabe em uma frase sua, fiel Ã  pÃ¡gina.','Releia o topo da pÃ¡gina e o tÃ³pico 1.'),('PÃºblico','VocÃª sabe dizer para quem a Ã¡rea Ã© e para quem nÃ£o Ã©.','Volte ao tÃ³pico 2 e escreva um exemplo do seu trabalho.'),('Blocos','VocÃª nomeia as partes centrais da Ã¡rea.','Use o diagrama do mÃ³dulo como roteiro.'),('Primeiro passo','VocÃª escolheu um passo concreto e pequeno.','Copie o primeiro passo que a prÃ³pria pÃ¡gina recomenda.'),('Porta de entrada','VocÃª sabe qual curso, kit ou projeto abrir primeiro.','Consulte o tÃ³pico 6 e a faixa de acesso da pÃ¡gina.'),('Fonte','Cada afirmaÃ§Ã£o da ficha tem origem na pÃ¡gina.','Troque o que vocÃª supÃ´s pelo que a pÃ¡gina diz.')]]
 for i,m in enumerate(MODULES):
  t=m['track'];mid=m['id'];topics=m['topics'];nt=len(topics);au=areaurl(m)
  body=f'<div class="breadcrumbs"><a href="../../index.html">{L("InÃ­cio")}</a> / <a href="index.html">{E(TRACKS[t-1][0])}</a> / {L("MÃ³dulo")} {mid.replace("-",".")}</div><article id="modulo-{mid}" data-ARCKHÉ-module="{mid}" data-ARCKHÉ-track="{t}"><header class="hero"><div><p class="kicker">{L("MÃ“DULO {id} / {num} DE {n}").format(id=mid.replace("-","."),num=m["num"],n=N)}</p><h1>{E(m["title"])}</h1><p>{E(m["goal"])}</p><p class="area-note">{L("PÃ¡gina da Ã¡rea:")} <a href="{au}">{au.replace("https://","")}</a> Â· {L("no menu:")} â€œ{E(NOTES[m["slug"]])}â€</p>{meter("modulo:"+mid)}</div><figure class="hero-panel">{diagram([tp["title"] for tp in topics],COLORS[t-1],m["slug"].upper())}<figcaption class="help-note">{L("Os {n} tÃ³picos deste mÃ³dulo. No fim, vocÃª preenche a ficha da Ã¡rea.").format(n=nt)}</figcaption></figure></header><div class="stats"><div><strong>{nt}</strong><span>{L("tÃ³picos")}</span></div><div><strong>~{m["time"]} min</strong><span>{L("leitura e prÃ¡tica")}</span></div><div><strong>1</strong><span>{L("ficha da Ã¡rea")}</span></div><div><strong>1</strong><span>{L("prompt pronto")}</span></div></div><div class="reading-layout"><div>'
  for j,tp in enumerate(topics,1):
   body+=f'<section class="topic ARCKHÉ-prose" id="topico-{j}" data-ARCKHÉ-topic="modulo-{mid}#topico-{j}"><h2><span class="number">{j}</span>{E(tp["title"])}</h2><h3>{L("O que Ã©")}</h3><p data-ARCKHÉ-block="m{mid}-t{j}-p1">{E(tp["what"])}</p><h3>{L("Por que aprender")}</h3><p data-ARCKHÉ-block="m{mid}-t{j}-p2">{E(tp["why"])}</p><h3>{L("Conceitos-chave")}</h3><p data-ARCKHÉ-block="m{mid}-t{j}-p3">{E(tp["keys"])}</p><div class="example"><h4>{L("Na prÃ¡tica")}</h4><p data-ARCKHÉ-block="m{mid}-t{j}-ex">{E(tp["example"])}</p></div>'
   if j in AVOID:body+=f'<div class="compare"><div><h4>âœ“ {L("FaÃ§a")}</h4><p>{E(tp["action"])}</p></div><div><h4>âœ— {L("Evite")}</h4><p>{E(AVOID[j])}</p></div></div>'
   elif j==3:body+=f'<h4>{L("SequÃªncia para experimentar")}</h4><ol class="timeline"><li>{L("Abra a pÃ¡gina da Ã¡rea ao lado desta aula.")}</li><li>{E(tp["action"])}</li><li>{L("Anote em uma frase o que mudou no seu entendimento.")}</li></ol>'
   else:body+=f'<aside class="tip"><h4>{L("Experimente agora")}</h4><p>{E(tp["action"])}</p></aside>'
   fg=FIGURES.get((i,j))
   if fg:body+=figure(fg,COLORS[t-1])
   body+=f'<div class="actions"><button type="button" data-ARCKHÉ-read-toggle aria-pressed="false"><span class="ARCKHÉ-read-icon" aria-hidden="true">â—‹</span><span class="ARCKHÉ-read-label" data-ARCKHÉ-read-label>{L("Marcar como lido")}</span></button><button type="button" data-ARCKHÉ-doubt-toggle aria-pressed="false">? {L("Tenho dÃºvida")}</button></div></section>'
  body+=f'</div><nav class="toc" data-ARCKHÉ-toc aria-label="{L("TÃ³picos deste mÃ³dulo")}"><p class="kicker">{L("NESTA AULA")}</p><ul>'+''.join(f'<li><a class="ARCKHÉ-toc-link" href="#topico-{j}">{j}. {E(tp["title"])}</a></li>' for j,tp in enumerate(topics,1))+f'</ul><a href="#laboratorio">{L("LaboratÃ³rio final â†“")}</a></nav></div>'
  body+=f'<section class="band"><h2>{L("CritÃ©rios para revisar sua ficha")}</h2><p>{L("Use esta rubrica depois do laboratÃ³rio. Cada linha pede uma evidÃªncia; marcar leitura nÃ£o significa que a ficha foi feita.")}</p><div class="table-scroll"><table><thead><tr><th>{L("CritÃ©rio")}</th><th>{L("EvidÃªncia esperada")}</th><th>{L("Se nÃ£o passou")}</th></tr></thead><tbody>'
  for row in RUBRIC:body+='<tr>'+''.join('<td>'+E(cell)+'</td>' for cell in row)+'</tr>'
  body+='</tbody></table></div></section>'
  body+=f'<section class="lab" id="laboratorio"><p class="kicker">{L("MÃƒO NA MASSA / ~10 MIN")}</p><h2>{E(m["lab"])}</h2><p>{L("Deixe a pÃ¡gina da Ã¡rea aberta:")} <a href="{au}">{au}</a>. {L("Use um exemplo do seu trabalho, sem dados pessoais ou de clientes.")}</p><ol class="checklist">'
  for j,step in enumerate(m['steps'],1):body+=f'<li><label><input type="checkbox" data-task="{mid}-{j}"><span>{E(step)}</span></label></li>'
  body+=f'</ol><h3>{E(m["snippet"][0])}</h3><p>{E(L("Cole no Claude, no ChatGPT ou no Codex. Troque o que estiver entre < e > pela sua situaÃ§Ã£o."))}</p><pre><code>{E(m["snippet"][1])}</code></pre><button data-copy-prev>{L("Copiar bloco")}</button><h3>{L("CritÃ©rio de pronto")}</h3><p>{E(m["goal"])} {L("Guarde a ficha com a tese, o pÃºblico, o primeiro passo e a porta de entrada.")}</p><a class="button" href="{au}">{L("Abrir a pÃ¡gina da Ã¡rea â†—")}</a></section><section class="band"><h2>{L("Confira o que ficou")}</h2><p>{E(m["check"])}</p><details><summary>{L("Ver resposta comentada")}</summary><p>{E(m["answer"])}</p><p>{L("Se sua resposta foi diferente, volte ao tÃ³pico correspondente e escreva a diferenÃ§a em uma frase. A checagem nÃ£o bloqueia seu estudo.")}</p></details><h3>{L("Resumo do mÃ³dulo")}</h3><ul>'+''.join(f'<li>{E(tp["keys"])}</li>' for tp in topics)+'</ul></section>'+sourcebox(m)
  prev='../../'+MODULES[i-1]['href'] if i else '../../index.html';nxt='../../'+MODULES[i+1]['href'] if i<N-1 else '../../index.html'
  body+=f'<div class="actions"><a class="button" href="{prev}">{L("â† Anterior")}</a><a class="button" href="index.html">{L("Voltar Ã  trilha")}</a><a class="button primary" href="{nxt}">{L("PrÃ³xima Ã¡rea â†’") if i<N-1 else L("Concluir: voltar ao mapa â†’")}</a></div></article>'
  page(m['title'],body,m['href'],t)
 if lang!='pt':
  for f in ('site.css','learn.css','favicon.svg'):shutil.copy(ROOT/'assets'/f,ROOT/prefix/'assets'/f)
  miss=[k for k in i18n.content_units(PT_MODULES,PT_TRACKS,PT_FIGURES,PT_NOTES) if k not in TR]
  if miss or missing:print(f'  AVISO {lang}: {len(miss)} unidades de conteÃºdo e {len(missing)} textos de interface sem traduÃ§Ã£o (ficaram em PT).')
 print(f'{lang}: {1+len(TRACKS)+N} pÃ¡ginas.')

langs=sys.argv[1:] or ['pt','en','es']
for lg in (['pt']+[x for x in langs if x!='pt'] if 'pt' in langs else langs):build(lg)
# CatÃ¡logo-fonte para traduÃ§Ã£o: conteÃºdo + interface (PT)
if 'pt' in langs:
 (ROOT/'i18n').mkdir(exist_ok=True)
 src=i18n.content_units(PT_MODULES,PT_TRACKS,PT_FIGURES,PT_NOTES);src.update(UI_USED)
 (ROOT/'i18n/source.json').write_text(json.dumps(src,ensure_ascii=False,indent=1))
