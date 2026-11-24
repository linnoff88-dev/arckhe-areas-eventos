"""ConteÃºdo do curso Ãreas do ARCKHÉ Eventos (ediÃ§Ã£o v2). Fontes lidas em 28/09/2026."""
from conteudo import trilha1, trilha2, trilha3
TRACKS=[('Gerenciar e comandar agentes','emerald','GestÃ£o de IA, AGI-ready e IA Cultivada: o trabalho passa a ser dirigir, cultivar e avaliar agentes.'),
('Ferramentas e ambiente','blue','Claude â†’ Codex, Codex + Claude e OSWork: onde os agentes trabalham e como nÃ£o ficar preso a um sÃ³.'),
('Melhorar, decidir e abrir','purple','RSI, JEV e WebMCP: melhorar com teste, decidir com avaliaÃ§Ã£o e preparar o site para agentes.')]
MODULES=[];FIGURES={}
for t,mod in enumerate([trilha1,trilha2,trilha3]):
 for (i,j),fg in mod.FIGURES.items():FIGURES[(t*3+i,j)]=fg
 MODULES.extend(mod.MODULES)
# Nota do menu do site (shared/header.json), usada no mapa da landing.
NOTES={'gestao-ia':'2027: gerenciar agentes','agi-ready':'comandar agentes','ia-cultivada':'nÃ£o se programa, se cultiva',
'claude-codex':'migre ou fique agnÃ³stico','codex-claude':'usar os dois juntos','oswork':'do chat ao seu ambiente de agentes',
'rsi':'ciclos de melhoria em IA','jev':'decisÃµes de IA na prÃ¡tica','webmcp':'sites que conversam com agentes'}
