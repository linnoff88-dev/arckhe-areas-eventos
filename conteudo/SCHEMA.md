# Esquema do conteêÂºdo ê¢â¬â curso "êÂreas do ARCKHê Eventos" (ediêÂ§êÂ£o v2)

Curso rêÂ¡pido que explica **o que êÂ© cada uma das 9 êÂ¡reas de assunto** do eventos.ARCKHê.pro.
3 trilhas êâ 3 mêÂ³dulos; **1 mêÂ³dulo = 1 êÂ¡rea**; **6 têÂ³picos por mêÂ³dulo**. PT-BR.

Cada trilha êÂ© um arquivo Python `conteudo/trilhaN.py` com exatamente este formato:

```python
"""Trilha N ê¢â¬â <nome>. Fontes: ARCKHêeventos/<slug>/index.html + shared/acesso.json (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

M('<têÂ­tulo do mêÂ³dulo = nome da êÂ¡rea + gancho curto>',
  '<goal: 1 frase ê¢â¬â o que o aluno sabe explicar ao final>',
  '<lab: têÂ­tulo do laboratêÂ³rio final, ex.: "Sua ficha da êÂ¡rea">',
  ['<passo 1>','<passo 2>','<passo 3>','<passo 4>'],     # 4 passos prêÂ¡ticos, verificêÂ¡veis
  '<check: pergunta de revisêÂ£o>',
  '<answer: resposta comentada, 1-2 frases>',
  [T(...), T(...), T(...), T(...), T(...), T(...)],      # EXATAMENTE 6 têÂ³picos
  ('<têÂ­tulo do bloco copiêÂ¡vel>', '<texto do bloco: prompt pronto p/ Claude Code/ChatGPT ou comando; variêÂ¡veis como <isto vocêÂª troca>>'),
  [('<rêÂ³tulo>','https://...'), ...],                     # 2-4 fontes: a pêÂ¡gina da êÂ¡rea + curso/projeto principal (URLs reais, da pêÂ¡gina ou do acesso.json)
  '<slug>')                                              # ex.: 'gestao-ia'

FIGURES[(<êÂ­ndice local do mêÂ³dulo 0..2>, <têÂ³pico 1..6>)] = dict(kind=..., caption='...', items=[...])
```

## Campos de cada têÂ³pico `T(title, what, why, keys, example, action)`

- `title`: curto (atêÂ© ~38 caracteres, cabe num cartêÂ£o SVG).
- `what` (**O que êÂ©**): 4-6 frases, concretas. Define todo termo têÂ©cnico na 1êÂª vez ("Um agente êÂ©ê¢â¬Â¦").
- `why` (**Por que aprender**): 2-3 frases.
- `keys` (**Conceitos-chave**): uma linha de termos separados por ";" ou frase curta. Vira o resumo do mêÂ³dulo.
- `example` (**Na prêÂ¡tica**): 2-3 frases com uma situaêÂ§êÂ£o real de trabalho (fictêÂ­cia, sem nomes reais de clientes).
- `action`: 1 frase imperativa, algo que o aluno faz agora (vira "Experimente agora" / "ê¢Åâ FaêÂ§a").

SugestêÂ£o de sequêÂªncia dos 6 têÂ³picos (adapte ao que a pêÂ¡gina tem):
1. O que êÂ© a êÂ¡rea (a tese / o h1 da pêÂ¡gina) êÂ· 2. Para quem êÂ© e o problema que resolve êÂ· 3-4. Os blocos centrais da pêÂ¡gina (h2) êÂ·
5. Por onde comeêÂ§ar (o "melhor primeiro passo" que a pêÂ¡gina traz) êÂ· 6. O que a êÂ¡rea reêÂºne (cursos/projetos do `acesso.json`) e onde ir.

## FIGURES (diagramas SVG gerados pelo build) ê¢â¬â 3 a 4 por mêÂ³dulo

`kind` possêÂ­veis e formato de `items`:
- `grid`: lista de strings curtas (atêÂ© 8; ê¢â°Â¤14 caracteres cada, cabem em caixa de 110px).
- `columns`: lista de tuplas `(têÂ­tulo, subtêÂ­tulo)` (3-5 itens; têÂ­tulos ê¢â°Â¤16 car., subtêÂ­tulos ê¢â°Â¤22); opcional `base=['a','b']`.
- `flow`: lista de strings ou tuplas (4-6 etapas; ê¢â°Â¤18 car.) ê¢â¬â setas entre etapas.
- `stack`: lista de strings ou `(têÂ­tulo, nota)` (3-6 camadas, escada).
- `tree`: lista de `(rêÂ³tulo, profundidade)` ê¢â¬â êÂ¡rvore de arquivos monoespaêÂ§ada.
- `timeline`: lista de strings ou `(têÂ­tulo, sobre-têÂ­tulo)` (3-5 marcos; têÂ­tulos ê¢â°Â¤14 car.).
`caption` = 1 frase que ENSINA (o que olhar e o que significa). TêÂ³picos diferentes por figura; nêÂ£o repita o têÂ³pico 1 (o hero jêÂ¡ resume os 6 têÂ­tulos).

## Regras de conteêÂºdo (obrigatêÂ³rias)

- **SêÂ³ fatos, frases, nêÂºmeros e nomes que estêÂ£o na pêÂ¡gina da êÂ¡rea** (`~/projetos/ARCKHêeventos/<slug>/index.html`, versêÂ£o PT na raiz da pasta) **e em `~/projetos/ARCKHêeventos/shared/acesso.json`** (bloco da rota `/<slug>/`). Se houver `<slug>/CONTEUDO.md`, pode usar. Nada inventado.
- **Sem data, preêÂ§o ou promessa que a pêÂ¡gina nêÂ£o tenha.** Claude ê¢â â Codex: o painel diz "Evento: data a anunciar" ê¢â¬â nêÂ£o citar data. IA Cultivada: hêÂ¡ um vêÂ­deo em produêÂ§êÂ£o, NêÆO publicado ê¢â¬â nêÂ£o citar vêÂ­deo. NêÂ£o citar vêÂ­deos do Explicavideos (nenhum foi produzido).
- ConteêÂºdo de terceiros citado na pêÂ¡gina (ex.: vêÂ­deo externo): sêÂ³ referenciar, nêÂ£o reproduzir.
- Tom: portuguêÂªs claro, frases curtas, sem jargêÂ£o êÂ³rfêÂ£o, sem "revolucionêÂ¡rio", sem emojis no texto.
- `snippet` = exemplo **copia-e-cola real**: um prompt completo que o aluno cola no Claude/ChatGPT/Codex para aplicar a êÂ¡rea ao prêÂ³prio trabalho (ex.: "Leia https://eventos.ARCKHê.pro/<slug>/ e ... Minha situaêÂ§êÂ£o: <descreva seu processo>"), ou um comando real. O `lab.steps` deve dizer como verificar o resultado.
- Strings Python: use aspas simples e escape apêÂ³strofos; o arquivo precisa importar sem erro (`python3 -c "import conteudo.trilhaN"` na raiz do projeto).
- Tamanho: cada mêÂ³dulo ê¢â°Ë 6 têÂ³picos êâ (what 5 frases + why 2-3 + keys + example + action). NêÂ£o encurte: o mêÂ³dulo final precisa ter densidade parecida com `~/projetos/oswork/conteudo/modulos.py` (veja 1-2 têÂ³picos lêÂ¡ como referêÂªncia de estilo).
