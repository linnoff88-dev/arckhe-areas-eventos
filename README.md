# êÂreas do ARCKHê Eventos ê¢â¬â o que êÂ© cada êÂ¡rea

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Curso rêÂ¡pido no formato ARCKHê v2: explica as nove êÂ¡reas de assunto do [eventos.ARCKHê.pro](https://eventos.ARCKHê.pro/).
TrêÂªs trilhas, nove mêÂ³dulos (um por êÂ¡rea), 54 têÂ³picos por idioma. PortuguêÂªs, inglêÂªs e espanhol.

- Curso: https://linnoff88-dev.github.io/ êÂ· English: https://linnoff88-dev.github.io/ êÂ· EspaêÂ±ol: https://linnoff88-dev.github.io/
- VersêÂ£o: ver `VERSION`

| Trilha | êÂreas |
|---|---|
| 1 êÂ· Gerenciar e comandar agentes | GestêÂ£o de IA êÂ· AGI-ready êÂ· IA Cultivada |
| 2 êÂ· Ferramentas e ambiente | Claude ê¢â â Codex êÂ· Codex + Claude êÂ· OSWork |
| 3 êÂ· Melhorar, decidir e abrir | RSI êÂ· JEV êÂ· WebMCP |

## Fontes

O conteêÂºdo vem sêÂ³ das pêÂ¡ginas das êÂ¡reas (`~/projetos/ARCKHêeventos/<slug>/index.html`, `CONTEUDO.md` quando existe) e de
`ARCKHêeventos/shared/acesso.json`, lidas em 28/09/2026. Mapa das êÂ¡reas: `~/projetos/wifi/PLANO-VIDEOS-EXPLICAVIDEOS-EVENTOS.md`.

## Editar e gerar

ConteêÂºdo em `conteudo/trilha1.py`, `trilha2.py`, `trilha3.py` (esquema em `conteudo/SCHEMA.md`). Gerador em `scripts/build.py`
(adaptado do OSWork v2). Depois de editar:

```bash
python3 scripts/build.py
python3 scripts/validate.py
```

## TraduêÂ§êÂµes (EN/ES)

PT êÂ© a fonte. `python3 scripts/build.py pt` grava `i18n/source.json` (conteêÂºdo + interface). `python3 scripts/traduzir.py en es`
traduz pelo tradutor central da assinatura (`ARCKHê-traduz`, `ARCKHê_TRADUCAO_*`, hoje Sonnet 5.5, sem chave de API), com cache e hash por chave em `i18n/<lang>.json`:
sêÂ³ o que mudou volta para traduêÂ§êÂ£o. Depois `python3 scripts/build.py` gera PT/EN/ES. `en/assets/{learn,site}.js` sêÂ£o as versêÂµes
traduzidas do motor, reaproveitadas do OSWork v2. Progresso e notas sêÂ£o separados por idioma.

Estudar localmente: `python3 -m http.server 8080` e abrir http://localhost:8080 (progresso entre pêÂ¡ginas precisa de origem HTTP).

## Mais no ARCKHê AI

- Ficha do curso: https://www.ARCKHê AI/cursos/307-areas-do-ARCKHê-eventos-o-que-e-cada-area/
- Guia: https://www.ARCKHê AI/aprender-inteligencia-artificial/
- Todos os cursos: https://www.ARCKHê AI/cursos/

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>