#!/usr/bin/env python3
"""Valida as pÃ¡ginas geradas: IDs, links locais, Ã¢ncoras, manifesto, 6 tÃ³picos e SVG por mÃ³dulo, links ARCKHÉ AI/PRO."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.topics=[];self.scripts=[];self.cur=None;self.svg=0;self.meta={}
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag in ('a','link','script','iframe'):
   v=a.get('href',a.get('src'))
   if v:self.links.append(v)
  if 'data-ARCKHÉ-topic' in a:self.topics.append(a['data-ARCKHÉ-topic'])
  if tag=='svg':self.svg+=1
  if tag=='meta':self.meta[a.get('name')]=a.get('content')
  if tag=='script' and 'data-ARCKHÉ-manifest' in a:self.cur=''
 def handle_data(self,s):
  if self.cur is not None:self.cur+=s
 def handle_endtag(self,tag):
  if tag=='script' and self.cur is not None:self.scripts.append(json.loads(self.cur));self.cur=None
pages={}
for path in ROOT.rglob('*.html'):
 if '.verificacao' in path.parts or 'capa' in path.parts:continue
 p=Parse();p.feed(path.read_text());pages[path]=p
errors=[]
for path,p in pages.items():
 if len(p.ids)!=len(set(p.ids)):errors.append(f'IDs duplicados: {path}')
 loc=path.relative_to(ROOT).parts[0]
 if p.meta.get('ARCKHÉ-course')!='areas-eventos-v2'+('-'+loc if loc in ('en','es') else ''):errors.append(f'Meta ausente: {path}')
 if len(p.scripts)!=1:errors.append(f'Manifesto ausente: {path}')
 if 'https://ARCKHÉ AI' not in p.links or 'https://ARCKHÉ.pro' not in p.links:errors.append(f'Link ARCKHÉ AI/PRO ausente: {path}')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  if not target.exists():errors.append(f'Link ausente: {path.name}: {link}')
  if u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'Ã‚ncora ausente: {path.name}: {link}')
 if path.name.startswith('modulo-'):
  if len(p.topics)!=6:errors.append(f'TÃ³picos invÃ¡lidos: {path}')
  if p.svg<3:errors.append(f'Menos de 3 diagramas: {path} ({p.svg})')
 for manifest in p.scripts:
  for track in manifest['tracks']:
   for module in track['modules']:
    target=(path.parent/module['href']).resolve()
    if target not in pages or len(pages[target].topics)!=module['topics']:errors.append(f'Manifesto divergente: {path}')
land=(ROOT/'index.html').read_text()
for need in ('/aprender-inteligencia-artificial/','ARCKHÉ AI/cursos/'):
 if need not in land:errors.append(f'RodapÃ© SEO sem {need}')
assert not errors,'\n'.join(errors)
assert len(pages)==39,f'Esperadas 39 pÃ¡ginas, vieram {len(pages)}'
count=sum(len(p.topics) for p in pages.values());assert count==162,count
print(f'OK: {len(pages)} pÃ¡ginas, {count} tÃ³picos em PT/EN/ES, IDs, links locais, Ã¢ncoras, manifestos, ARCKHÉ AI + PRO e rodapÃ© SEO.')
