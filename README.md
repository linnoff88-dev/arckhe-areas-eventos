# Ãreas do INEMA Eventos â€” o que Ã© cada Ã¡rea

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Curso rÃ¡pido no formato INEMA v2: explica as nove Ã¡reas de assunto do [eventos.inema.pro](https://eventos.inema.pro/).
TrÃªs trilhas, nove mÃ³dulos (um por Ã¡rea), 54 tÃ³picos por idioma. PortuguÃªs, inglÃªs e espanhol.

- Curso: https://inematds.github.io/areas-eventos/ Â· English: https://inematds.github.io/areas-eventos/en/ Â· EspaÃ±ol: https://inematds.github.io/areas-eventos/es/
- VersÃ£o: ver `VERSION`

| Trilha | Ãreas |
|---|---|
| 1 Â· Gerenciar e comandar agentes | GestÃ£o de IA Â· AGI-ready Â· IA Cultivada |
| 2 Â· Ferramentas e ambiente | Claude â†’ Codex Â· Codex + Claude Â· OSWork |
| 3 Â· Melhorar, decidir e abrir | RSI Â· JEV Â· WebMCP |

## Fontes

O conteÃºdo vem sÃ³ das pÃ¡ginas das Ã¡reas (`~/projetos/inemaeventos/<slug>/index.html`, `CONTEUDO.md` quando existe) e de
`inemaeventos/shared/acesso.json`, lidas em 28/09/2026. Mapa das Ã¡reas: `~/projetos/wifi/PLANO-VIDEOS-EXPLICAVIDEOS-EVENTOS.md`.

## Editar e gerar

ConteÃºdo em `conteudo/trilha1.py`, `trilha2.py`, `trilha3.py` (esquema em `conteudo/SCHEMA.md`). Gerador em `scripts/build.py`
(adaptado do OSWork v2). Depois de editar:

```bash
python3 scripts/build.py
python3 scripts/validate.py
```

## TraduÃ§Ãµes (EN/ES)

PT Ã© a fonte. `python3 scripts/build.py pt` grava `i18n/source.json` (conteÃºdo + interface). `python3 scripts/traduzir.py en es`
traduz pelo tradutor central da assinatura (`inema-traduz`, `INEMA_TRADUCAO_*`, hoje Sonnet 5.5, sem chave de API), com cache e hash por chave em `i18n/<lang>.json`:
sÃ³ o que mudou volta para traduÃ§Ã£o. Depois `python3 scripts/build.py` gera PT/EN/ES. `en/assets/{learn,site}.js` sÃ£o as versÃµes
traduzidas do motor, reaproveitadas do OSWork v2. Progresso e notas sÃ£o separados por idioma.

Estudar localmente: `python3 -m http.server 8080` e abrir http://localhost:8080 (progresso entre pÃ¡ginas precisa de origem HTTP).

## Mais no INEMA.CLUB

- Ficha do curso: https://www.inema.club/cursos/307-areas-do-inema-eventos-o-que-e-cada-area/
- Guia: https://www.inema.club/aprender-inteligencia-artificial/
- Todos os cursos: https://www.inema.club/cursos/

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>