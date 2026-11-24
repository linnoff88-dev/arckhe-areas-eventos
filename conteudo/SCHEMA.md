# Esquema do conteÃºdo â€” curso "Ãreas do ARCKHÉ Eventos" (ediÃ§Ã£o v2)

Curso rÃ¡pido que explica **o que Ã© cada uma das 9 Ã¡reas de assunto** do eventos.ARCKHÉ.pro.
3 trilhas Ã— 3 mÃ³dulos; **1 mÃ³dulo = 1 Ã¡rea**; **6 tÃ³picos por mÃ³dulo**. PT-BR.

Cada trilha Ã© um arquivo Python `conteudo/trilhaN.py` com exatamente este formato:

```python
"""Trilha N â€” <nome>. Fontes: ARCKHÉeventos/<slug>/index.html + shared/acesso.json (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

M('<tÃ­tulo do mÃ³dulo = nome da Ã¡rea + gancho curto>',
  '<goal: 1 frase â€” o que o aluno sabe explicar ao final>',
  '<lab: tÃ­tulo do laboratÃ³rio final, ex.: "Sua ficha da Ã¡rea">',
  ['<passo 1>','<passo 2>','<passo 3>','<passo 4>'],     # 4 passos prÃ¡ticos, verificÃ¡veis
  '<check: pergunta de revisÃ£o>',
  '<answer: resposta comentada, 1-2 frases>',
  [T(...), T(...), T(...), T(...), T(...), T(...)],      # EXATAMENTE 6 tÃ³picos
  ('<tÃ­tulo do bloco copiÃ¡vel>', '<texto do bloco: prompt pronto p/ Claude Code/ChatGPT ou comando; variÃ¡veis como <isto vocÃª troca>>'),
  [('<rÃ³tulo>','https://...'), ...],                     # 2-4 fontes: a pÃ¡gina da Ã¡rea + curso/projeto principal (URLs reais, da pÃ¡gina ou do acesso.json)
  '<slug>')                                              # ex.: 'gestao-ia'

FIGURES[(<Ã­ndice local do mÃ³dulo 0..2>, <tÃ³pico 1..6>)] = dict(kind=..., caption='...', items=[...])
```

## Campos de cada tÃ³pico `T(title, what, why, keys, example, action)`

- `title`: curto (atÃ© ~38 caracteres, cabe num cartÃ£o SVG).
- `what` (**O que Ã©**): 4-6 frases, concretas. Define todo termo tÃ©cnico na 1Âª vez ("Um agente Ã©â€¦").
- `why` (**Por que aprender**): 2-3 frases.
- `keys` (**Conceitos-chave**): uma linha de termos separados por ";" ou frase curta. Vira o resumo do mÃ³dulo.
- `example` (**Na prÃ¡tica**): 2-3 frases com uma situaÃ§Ã£o real de trabalho (fictÃ­cia, sem nomes reais de clientes).
- `action`: 1 frase imperativa, algo que o aluno faz agora (vira "Experimente agora" / "âœ“ FaÃ§a").

SugestÃ£o de sequÃªncia dos 6 tÃ³picos (adapte ao que a pÃ¡gina tem):
1. O que Ã© a Ã¡rea (a tese / o h1 da pÃ¡gina) Â· 2. Para quem Ã© e o problema que resolve Â· 3-4. Os blocos centrais da pÃ¡gina (h2) Â·
5. Por onde comeÃ§ar (o "melhor primeiro passo" que a pÃ¡gina traz) Â· 6. O que a Ã¡rea reÃºne (cursos/projetos do `acesso.json`) e onde ir.

## FIGURES (diagramas SVG gerados pelo build) â€” 3 a 4 por mÃ³dulo

`kind` possÃ­veis e formato de `items`:
- `grid`: lista de strings curtas (atÃ© 8; â‰¤14 caracteres cada, cabem em caixa de 110px).
- `columns`: lista de tuplas `(tÃ­tulo, subtÃ­tulo)` (3-5 itens; tÃ­tulos â‰¤16 car., subtÃ­tulos â‰¤22); opcional `base=['a','b']`.
- `flow`: lista de strings ou tuplas (4-6 etapas; â‰¤18 car.) â€” setas entre etapas.
- `stack`: lista de strings ou `(tÃ­tulo, nota)` (3-6 camadas, escada).
- `tree`: lista de `(rÃ³tulo, profundidade)` â€” Ã¡rvore de arquivos monoespaÃ§ada.
- `timeline`: lista de strings ou `(tÃ­tulo, sobre-tÃ­tulo)` (3-5 marcos; tÃ­tulos â‰¤14 car.).
`caption` = 1 frase que ENSINA (o que olhar e o que significa). TÃ³picos diferentes por figura; nÃ£o repita o tÃ³pico 1 (o hero jÃ¡ resume os 6 tÃ­tulos).

## Regras de conteÃºdo (obrigatÃ³rias)

- **SÃ³ fatos, frases, nÃºmeros e nomes que estÃ£o na pÃ¡gina da Ã¡rea** (`~/projetos/ARCKHÉeventos/<slug>/index.html`, versÃ£o PT na raiz da pasta) **e em `~/projetos/ARCKHÉeventos/shared/acesso.json`** (bloco da rota `/<slug>/`). Se houver `<slug>/CONTEUDO.md`, pode usar. Nada inventado.
- **Sem data, preÃ§o ou promessa que a pÃ¡gina nÃ£o tenha.** Claude â†’ Codex: o painel diz "Evento: data a anunciar" â€” nÃ£o citar data. IA Cultivada: hÃ¡ um vÃ­deo em produÃ§Ã£o, NÃƒO publicado â€” nÃ£o citar vÃ­deo. NÃ£o citar vÃ­deos do Explicavideos (nenhum foi produzido).
- ConteÃºdo de terceiros citado na pÃ¡gina (ex.: vÃ­deo externo): sÃ³ referenciar, nÃ£o reproduzir.
- Tom: portuguÃªs claro, frases curtas, sem jargÃ£o Ã³rfÃ£o, sem "revolucionÃ¡rio", sem emojis no texto.
- `snippet` = exemplo **copia-e-cola real**: um prompt completo que o aluno cola no Claude/ChatGPT/Codex para aplicar a Ã¡rea ao prÃ³prio trabalho (ex.: "Leia https://eventos.ARCKHÉ.pro/<slug>/ e ... Minha situaÃ§Ã£o: <descreva seu processo>"), ou um comando real. O `lab.steps` deve dizer como verificar o resultado.
- Strings Python: use aspas simples e escape apÃ³strofos; o arquivo precisa importar sem erro (`python3 -c "import conteudo.trilhaN"` na raiz do projeto).
- Tamanho: cada mÃ³dulo â‰ˆ 6 tÃ³picos Ã— (what 5 frases + why 2-3 + keys + example + action). NÃ£o encurte: o mÃ³dulo final precisa ter densidade parecida com `~/projetos/oswork/conteudo/modulos.py` (veja 1-2 tÃ³picos lÃ¡ como referÃªncia de estilo).
