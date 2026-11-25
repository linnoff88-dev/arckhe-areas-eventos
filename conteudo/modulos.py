"""ConteêÂºdo do curso êÂreas do ARCKHê Eventos (ediêÂ§êÂ£o v2). Fontes lidas em 28/09/2026."""
from conteudo import trilha1, trilha2, trilha3
TRACKS=[('Gerenciar e comandar agentes','emerald','GestêÂ£o de IA, AGI-ready e IA Cultivada: o trabalho passa a ser dirigir, cultivar e avaliar agentes.'),
('Ferramentas e ambiente','blue','Claude ê¢â â Codex, Codex + Claude e OSWork: onde os agentes trabalham e como nêÂ£o ficar preso a um sêÂ³.'),
('Melhorar, decidir e abrir','purple','RSI, JEV e WebMCP: melhorar com teste, decidir com avaliaêÂ§êÂ£o e preparar o site para agentes.')]
MODULES=[];FIGURES={}
for t,mod in enumerate([trilha1,trilha2,trilha3]):
 for (i,j),fg in mod.FIGURES.items():FIGURES[(t*3+i,j)]=fg
 MODULES.extend(mod.MODULES)
# Nota do menu do site (shared/header.json), usada no mapa da landing.
NOTES={'gestao-ia':'2027: gerenciar agentes','agi-ready':'comandar agentes','ia-cultivada':'nêÂ£o se programa, se cultiva',
'claude-codex':'migre ou fique agnêÂ³stico','codex-claude':'usar os dois juntos','oswork':'do chat ao seu ambiente de agentes',
'rsi':'ciclos de melhoria em IA','jev':'decisêÂµes de IA na prêÂ¡tica','webmcp':'sites que conversam com agentes'}
