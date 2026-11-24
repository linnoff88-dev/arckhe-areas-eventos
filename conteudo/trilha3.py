"""Trilha 3 â€” Melhorar, decidir e abrir para agentes. Fontes: ARCKHÉeventos/{rsi,jev,webmcp}/index.html + shared/acesso.json + rsi/CONTEUDO.md + jev/CONTEUDO.md (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

# ---------------------------------------------------------------- 0 Â· RSI
M('RSI: a IA que ajuda a melhorar a IA',
  'Explicar os trÃªs nÃ­veis de melhoria em IA e transformar uma ideia de melhoria num teste verificÃ¡vel, com versÃ£o registrada e caminho de volta.',
  'Seu primeiro ciclo de melhoria no papel',
  ['Escolha uma tarefa pequena do seu trabalho, como extrair aÃ§Ãµes de notas de reuniÃ£o, e escreva qual seria a resposta correta para trÃªs exemplos fictÃ­cios.',
   'Separe esses exemplos em dois grupos: dois para desenvolver a mudanÃ§a e um reservado, que vocÃª sÃ³ usa na validaÃ§Ã£o.',
   'Registre a versÃ£o inicial da instruÃ§Ã£o, proponha UMA mudanÃ§a e rode as duas versÃµes nos mesmos exemplos, anotando acertos, erros, custo e tempo de revisÃ£o.',
   'Confira no exemplo reservado se a mudanÃ§a se sustenta; sÃ³ entÃ£o adote, e anote quem decidiu e como voltar Ã  versÃ£o anterior.'],
  'Depois de dez tentativas, a nova instruÃ§Ã£o tirou nota maior no mesmo conjunto que vocÃª usou para ajustÃ¡-la. Isso prova que ela Ã© melhor?',
  'NÃ£o. Uma avaliaÃ§Ã£o conhecida pode ser explorada; a mudanÃ§a precisa se sustentar em casos reservados, com os mesmos critÃ©rios. Mais tentativas ou uma nota maior nÃ£o demonstram crescimento ilimitado.',
  [T('O que Ã© RSI',
     'RSI Ã© a sigla em inglÃªs para automelhoria recursiva: a ideia de uma IA que ajuda a melhorar a prÃ³pria IA. A pergunta central da Ã¡rea Ã© prÃ¡tica: como um sistema propÃµe mudanÃ§as, testa resultados e conserva o que funciona? A pÃ¡gina trata o tema como Ã¡rea de estudo e acervo aberto, com referÃªncias, exemplos e critÃ©rios para avaliar as promessas. O ponto de partida Ã© uma distinÃ§Ã£o: melhorar uma resposta, melhorar um agente e melhorar a capacidade de criar novos agentes sÃ£o coisas diferentes. Um agente, aqui, Ã© um sistema de IA que recebe um objetivo e executa etapas com instruÃ§Ãµes, memÃ³ria e ferramentas.',
     'Promessas de IA que se melhora sozinha aparecem com frequÃªncia e costumam misturar esses trÃªs nÃ­veis. Quem entende a diferenÃ§a consegue perguntar o que exatamente melhorou e qual evidÃªncia sustenta isso.',
     'automelhoria recursiva; propor, testar, conservar; trÃªs nÃ­veis diferentes; acervo aberto; critÃ©rios para avaliar promessas',
     'Um fornecedor diz que seu assistente "aprende sozinho". A gestora pergunta: ele refaz a resposta, muda as prÃ³prias instruÃ§Ãµes ou produz melhorias futuras? E como isso foi medido? A resposta define se o produto estÃ¡ no primeiro, no segundo ou no terceiro nÃ­vel.',
     'Escreva em uma frase uma promessa de melhoria automÃ¡tica que vocÃª jÃ¡ ouviu e marque qual dos trÃªs nÃ­veis ela realmente descreve.'),
   T('TrÃªs nÃ­veis que nÃ£o se confundem',
     'O primeiro nÃ­vel Ã© revisar a resposta: o modelo critica e refaz uma saÃ­da. Isso pode melhorar uma tarefa sem alterar seus parÃ¢metros, os valores internos aprendidos no treino, nem seu processo de desenvolvimento. O segundo nÃ­vel Ã© melhorar o sistema: mudam as instruÃ§Ãµes, a memÃ³ria, as ferramentas ou o cÃ³digo do agente, e as versÃµes precisam ser comparadas com tarefas reservadas, preservando a possibilidade de voltar atrÃ¡s. O terceiro Ã© investigar a recursÃ£o: a melhoria passa a ajudar a produzir melhorias futuras. Esse mecanismo precisa de evidÃªncia, porque mais tentativas ou uma nota maior nÃ£o demonstram crescimento ilimitado.',
     'Cada nÃ­vel exige um tipo de controle diferente. Revisar uma resposta Ã© barato e reversÃ­vel; mudar o sistema pede registro de versÃµes e testes; afirmar recursÃ£o pede evidÃªncia forte. Confundir os nÃ­veis leva a aceitar garantias que ninguÃ©m mediu.',
     'revisar a resposta; melhorar o sistema; investigar a recursÃ£o; parÃ¢metros; tarefas reservadas; possibilidade de voltar atrÃ¡s',
     'Uma equipe pede ao modelo que revise o prÃ³prio resumo antes de entregar: isso Ã© nÃ­vel 1. Depois reescreve a instruÃ§Ã£o do agente de atendimento e compara as duas versÃµes em casos separados: nÃ­vel 2. Nenhuma das duas coisas, sozinha, Ã© uma IA criando IAs melhores.',
     'Classifique trÃªs melhorias que vocÃª jÃ¡ fez em prompts ou agentes nos trÃªs nÃ­veis da pÃ¡gina e anote se alguma delas tinha caminho de volta.'),
   T('Da ideia a um teste verificÃ¡vel',
     'A pÃ¡gina propÃµe comeÃ§ar com uma tarefa pequena: responder com base numa polÃ­tica, criar questÃµes a partir de um texto ou extrair aÃ§Ãµes de notas. Primeiro defina a tarefa, a referÃªncia correta e os limites de dados, gasto e aÃ§Ãµes. Depois registre a versÃ£o inicial e separe casos de desenvolvimento de casos reservados para validaÃ§Ã£o. Proponha uma mudanÃ§a por vez e compare com os mesmos critÃ©rios, incluindo erros, custo e esforÃ§o de revisÃ£o. Por fim, valide antes de adotar: guarde resultados e versÃµes, defina quem decide e mantenha um caminho de reversÃ£o.',
     'Uma avaliaÃ§Ã£o conhecida pode ser explorada, e a pÃ¡gina alerta para isso. Preservar a independÃªncia dos testes, conferir dados inventados e olhar resultados fora da amostra evita confundir ganho local com autonomia geral.',
     'tarefa pequena; referÃªncia correta; casos reservados; uma mudanÃ§a por vez; mesmos critÃ©rios; validar antes de adotar; reversÃ£o',
     'Uma escola testa uma instruÃ§Ã£o que cria questÃµes a partir de um texto. Usa quatro textos para ajustar e guarda dois que ninguÃ©m viu. A versÃ£o nova acerta mais nos quatro, mas erra num dos reservados; a coordenaÃ§Ã£o decide manter a versÃ£o antiga atÃ© entender o erro.',
     'Escolha uma tarefa sua e escreva as quatro linhas: tarefa e referÃªncia; versÃ£o inicial e casos reservados; a Ãºnica mudanÃ§a; quem decide e como voltar.'),
   T('LOOP-R: o ciclo com freios',
     'LOOP-R Ã© o framework do projeto para organizar melhorias: Executar, Medir, Criticar, Propor, Testar, Validar, Promover e Repetir. A pÃ¡gina o descreve como pronto para usar no Claude Code, com nove assistentes de funÃ§Ãµes separadas, registro de cada versÃ£o, teto de custo e comando para reverter. A regra de seguranÃ§a Ã© explÃ­cita: nenhuma versÃ£o pior substitui a atual por decisÃ£o do sistema. No curso RSI, o LOOP-R aparece como uma proposta conceitual do projeto. HÃ¡ tambÃ©m um curso LOOP-R com cinco trilhas e 21 aulas para donos e gestores sem base tÃ©cnica.',
     'Um ciclo de melhoria sem freios pode trocar uma versÃ£o boa por uma pior sem ninguÃ©m perceber. Teto de custo, registro de versÃµes e reversÃ£o tornam o ciclo auditÃ¡vel e seguro de repetir.',
     'Executar; Medir; Criticar; Propor; Testar; Validar; Promover; Repetir; nove assistentes; teto de custo; reverter',
     'Um gestor usa o ciclo para melhorar a instruÃ§Ã£o que classifica pedidos de clientes. Cada rodada gera uma versÃ£o registrada; quando a nova versÃ£o piora num teste, ela nÃ£o Ã© promovida e a atual continua valendo.',
     'Abra o guia do LOOP-R e anote em qual das oito etapas o seu processo atual de ajuste de prompts costuma parar.'),
   T('Por onde comeÃ§ar: curso e guia',
     'A seÃ§Ã£o "Comece por aqui" traz dois materiais. O curso RSI v6.2 tem 18 aulas em seis mÃ³dulos, com exercÃ­cios, revisÃ£o e materiais para aplicar o LOOP-R e registrar conhecimento aprovado, em portuguÃªs, inglÃªs e espanhol. O Guia RSI Ã© um mapa do tema, com mecanismos, aplicaÃ§Ãµes e limites, tambÃ©m em trÃªs idiomas. A pÃ¡gina faz uma ressalva importante: o projeto reÃºne pesquisa e conteÃºdo educativo, e nÃ£o Ã© um sistema RSI autÃ´nomo pronto para executar. O cÃ³digo e os materiais ficam no repositÃ³rio rsi no GitHub.',
     'ComeÃ§ar pelo guia dÃ¡ o vocabulÃ¡rio e os limites; o curso transforma isso em prÃ¡tica com exercÃ­cios. Saber que o projeto Ã© educativo evita esperar dele uma ferramenta que melhora sozinha.',
     'RSI v6.2; 18 aulas; seis mÃ³dulos; Guia RSI; PT / EN / ES; conteÃºdo educativo, nÃ£o sistema autÃ´nomo',
     'Uma consultora quer explicar RSI para uma diretoria. Usa o Guia RSI para montar o mapa dos trÃªs nÃ­veis e indica o curso RSI v6.2 para a pessoa do time que vai conduzir os testes de melhoria.',
     'Abra o Guia RSI, leia a parte de limites e anote uma frase que vocÃª usaria para responder a quem promete IA que se melhora sozinha.'),
   T('O acervo: Copiloto, Dream-RSI, 2028',
     'AlÃ©m do guia e do curso, o acervo reÃºne trÃªs materiais com ressalvas claras. O RSI Copiloto Ã© um assistente local com IA, memÃ³ria, tarefas e rotinas, que compara instruÃ§Ãµes, pede revisÃ£o humana e permite reverter mudanÃ§as; a demonstraÃ§Ã£o pÃºblica usa exemplos programados, sem IA, e a IA real fica sÃ³ na versÃ£o local. O Dream-RSI Ã© um guia educativo independente, nÃ£o afiliado ao Google, sobre aprender com histÃ³ricos de experimentos; o laboratÃ³rio e os oito encontros sÃ£o planos futuros, nÃ£o uma implementaÃ§Ã£o do artigo. O Alerta IA 2028 Ã© um curso em trÃªs trilhas, sobre o ciclo de melhoria, as evidÃªncias e os limites da avaliaÃ§Ã£o, e trata os cenÃ¡rios de 2028 como hipÃ³teses, sem calendÃ¡rio garantido. A pÃ¡gina ainda lista referÃªncias como Self-Refine, Reflexion, Darwin GÃ¶del Machine e AlphaEvolve, consultadas em 25 de setembro de 2026, cujos resultados nÃ£o foram reproduzidos no projeto.',
     'Cada material diz o que jÃ¡ estÃ¡ disponÃ­vel e o que ainda Ã© plano. Ler essas ressalvas Ã© o prÃ³prio exercÃ­cio da Ã¡rea: separar evidÃªncia de promessa.',
     'RSI Copiloto; demonstraÃ§Ã£o sem IA; Dream-RSI independente; Alerta IA 2028; cenÃ¡rios como hipÃ³teses; referÃªncias originais em inglÃªs',
     'Um analista experimenta a demonstraÃ§Ã£o do Copiloto e percebe que as respostas sÃ£o programadas. Em vez de concluir que "a IA acertou tudo", registra que precisa da versÃ£o local para testar de verdade.',
     'Escolha um dos trÃªs materiais e escreva o que ele jÃ¡ entrega e o que a pÃ¡gina diz que ainda Ã© plano ou exemplo programado.')],
  ('Prompt: meu primeiro teste de melhoria (RSI)',
   'Leia https://eventos.ARCKHÉ.pro/rsi/ e o guia https://linnoff88-dev.github.io/
   'Quero testar uma melhoria numa tarefa do meu trabalho, sem prometer mais do que consigo medir.\n'
   'Minha tarefa: <descreva a tarefa, ex.: extrair aÃ§Ãµes de notas de reuniÃ£o>.\n'
   'Minha instruÃ§Ã£o atual: <cole a instruÃ§Ã£o ou prompt que vocÃª usa hoje>.\n'
   '1. Diga em qual dos trÃªs nÃ­veis (revisar a resposta, melhorar o sistema, investigar a recursÃ£o) a minha ideia se encaixa.\n'
   '2. Monte o teste: referÃªncia correta, limites de dados/gasto/aÃ§Ãµes, casos de desenvolvimento e casos reservados.\n'
   '3. Proponha UMA Ãºnica mudanÃ§a na instruÃ§Ã£o e a tabela para comparar as duas versÃµes (erros, custo, esforÃ§o de revisÃ£o).\n'
   '4. Diga quem deve decidir a adoÃ§Ã£o e como voltar Ã  versÃ£o anterior.\n'
   'NÃ£o invente resultados: deixe os campos de resultado em branco para eu preencher.'),
  [('Ãrea RSI Â· eventos.ARCKHÉ.pro','https://eventos.ARCKHÉ.pro/rsi/'),
   ('Curso RSI v6.2','https://linnoff88-dev.github.io/
   ('Guia RSI','https://linnoff88-dev.github.io/
   ('Framework LOOP-R','https://linnoff88-dev.github.io/
  'rsi')

FIGURES[(0,2)] = dict(kind='timeline',
  caption='Os trÃªs nÃ­veis sobem em ambiÃ§Ã£o e em exigÃªncia de prova: revisar uma resposta nÃ£o altera o sistema, e sÃ³ o terceiro nÃ­vel fala em melhorias que geram melhorias.',
  items=[('Revisar','nÃ­vel 1'),('Sistema','nÃ­vel 2'),('RecursÃ£o','nÃ­vel 3')])
FIGURES[(0,3)] = dict(kind='flow',
  caption='Um teste verificÃ¡vel separa ajuste de validaÃ§Ã£o: a mudanÃ§a sÃ³ Ã© adotada depois de passar nos casos reservados, com reversÃ£o possÃ­vel.',
  items=['Definir tarefa','VersÃ£o inicial','Uma mudanÃ§a','Mesmos critÃ©rios','Validar e decidir'])
FIGURES[(0,4)] = dict(kind='grid',
  caption='As oito etapas do LOOP-R repetem o ciclo, mas Validar e Promover funcionam como portÃµes: versÃ£o pior nÃ£o substitui a atual.',
  items=['Executar','Medir','Criticar','Propor','Testar','Validar','Promover','Repetir'])
FIGURES[(0,6)] = dict(kind='columns',
  caption='Cada material do acervo traz sua ressalva: leia o subtÃ­tulo antes de tirar conclusÃµes sobre o que ele entrega.',
  items=[('RSI Copiloto','demo sem IA'),('Dream-RSI','independente'),('Alerta IA 2028','cenÃ¡rios = hipÃ³teses'),('LOOP-R','versÃ£o pior nÃ£o entra')])

# ---------------------------------------------------------------- 1 Â· JEV
M('JEV: decisÃµes de IA na prÃ¡tica',
  'Explicar o que Ã© uma decisÃ£o estruturada com Jev, escolher entre Choice, Noul e Score e separar o que jÃ¡ foi observado do que ainda falta medir.',
  'Sua decisÃ£o estruturada, do caso ao piloto',
  ['Abra o laboratÃ³rio pÃºblico do JEV, escolha um dos 20 casos e anote contexto, pergunta, critÃ©rios e a resposta simulada.',
   'Escreva uma decisÃ£o parecida do seu trabalho e indique se ela Ã© Choice, Noul ou Score, justificando pelo tipo de resposta de que vocÃª precisa.',
   'Defina a polÃ­tica: com que confianÃ§a a sugestÃ£o segue, quando o sistema se abstÃ©m e quando vai para revisÃ£o humana.',
   'Confira sua ficha contra a seÃ§Ã£o "O que jÃ¡ foi observado e o que falta medir": marque o que vocÃª conseguiria medir com dados prÃ³prios e referÃªncia humana.'],
  'O laboratÃ³rio pÃºblico mostrou respostas corretas em todos os casos que vocÃª abriu. Isso mede a qualidade do Jev?',
  'NÃ£o. Os 20 casos pÃºblicos e o replay sÃ£o autorais e simulados; servem para estudar formulaÃ§Ã£o, polÃ­ticas e erros. Qualidade em portuguÃªs e calibraÃ§Ã£o ainda precisam de dados independentes e referÃªncia humana.',
  [T('O que Ã© o JEV',
     'Jev Ã© o modelo de decisÃµes estruturadas da TypeSafe. Uma decisÃ£o estruturada Ã© uma pergunta fechada, com contexto e critÃ©rios, cuja resposta Ã© uma escolha, uma probabilidade ou um nÃ­vel, e nÃ£o um texto livre. O Jev Decision Lab Ã© o projeto educacional do ARCKHÉ para formular perguntas, comparar respostas e entender quando uma decisÃ£o precisa de revisÃ£o. O modelo recebe contexto e critÃ©rios; o seu sistema continua responsÃ¡vel pelas aÃ§Ãµes. O laboratÃ³rio separa essa escolha da geraÃ§Ã£o de texto e da execuÃ§Ã£o de ferramentas.',
     'Muitas tarefas de IA no trabalho nÃ£o pedem um texto, pedem uma decisÃ£o: para qual fila vai este chamado, este trecho sustenta a afirmaÃ§Ã£o. Separar decidir, gerar e executar deixa claro quem responde por cada parte e facilita medir o acerto.',
     'modelo de decisÃµes estruturadas; TypeSafe; Jev Decision Lab; contexto e critÃ©rios; o sistema responde pelas aÃ§Ãµes',
     'Uma equipe de suporte quer que a IA encaminhe chamados. Em vez de pedir um parÃ¡grafo, ela usa o Jev para escolher a fila entre opÃ§Ãµes fixas; o sistema da empresa Ã© quem move o chamado, e casos duvidosos vÃ£o para uma pessoa.',
     'Liste duas decisÃµes repetitivas do seu trabalho que hoje viram texto livre e reescreva cada uma como pergunta fechada com opÃ§Ãµes.'),
   T('Choice, Noul e Score',
     'A pÃ¡gina apresenta trÃªs formas de perguntar. Choice escolhe entre alternativas explÃ­citas, como qual fila ou qual agente. Noul estima a probabilidade de uma resposta afirmativa, como a chance de um trecho apoiar uma afirmaÃ§Ã£o. Score avalia uma rubrica com nÃ­veis ordenados, como baixo, mÃ©dio e alto. O curso dedica um mÃ³dulo a distinguir as trÃªs a partir do tipo de resposta necessÃ¡rio, e outro a confianÃ§a e erro: usar incerteza sem transformÃ¡-la em autorizaÃ§Ã£o automÃ¡tica.',
     'Escolher a forma errada produz respostas difÃ­ceis de usar: uma nota quando vocÃª precisava de uma fila, ou um sim quando havia vÃ¡rios nÃ­veis. A forma da pergunta define como vocÃª vai medir e qual polÃ­tica aplicar.',
     'Choice: alternativas explÃ­citas; Noul: probabilidade de sim; Score: nÃ­veis ordenados; confianÃ§a nÃ£o Ã© autorizaÃ§Ã£o',
     'Na triagem de reuniÃµes, "a ata tem responsÃ¡vel e prazo?" Ã© Noul; "qual equipe cuida disto?" Ã© Choice; "qual a prioridade do log, de 1 a 4?" Ã© Score. A mesma reuniÃ£o pode gerar as trÃªs perguntas.',
     'Pegue uma das decisÃµes que vocÃª listou e escreva-a nas trÃªs formas; fique com a que devolve a resposta que o seu processo consegue usar.'),
   T('20 casos no laboratÃ³rio pÃºblico',
     'O laboratÃ³rio abre no navegador, nÃ£o pede chave e nÃ£o consulta nenhuma API: as respostas sÃ£o simuladas. Cada um dos 20 casos inclui contexto, perguntas, critÃ©rios, resposta simulada, explicaÃ§Ã£o e prÃ³ximo passo, como triagem de atendimento, checklist de contratos, roteamento de agentes e revisÃ£o semÃ¢ntica de diff. VocÃª pode editar as perguntas, importar uma requisiÃ§Ã£o, exportar o resultado ou abrir um relatÃ³rio; alterar um caso invalida sua resposta simulada anterior. Para ir alÃ©m, Ã© possÃ­vel clonar o projeto e rodar o servidor local com Python 3.10 ou superior. O nÃºcleo usa sÃ³ a biblioteca padrÃ£o.',
     'O laboratÃ³rio permite errar sem custo e sem risco: vocÃª aprende a formular o contexto, as opÃ§Ãµes e a polÃ­tica antes de gastar crÃ©dito ou tocar num sistema real.',
     'laboratÃ³rio sem chave; respostas simuladas; 20 casos; contexto, perguntas, critÃ©rios; servidor local em Python',
     'Um coordenador abre o caso "IntenÃ§Ãµes simultÃ¢neas" e vÃª que uma conversa pode conter vendas e agendamento ao mesmo tempo. Ele percebe que a pergunta da sua empresa, com uma Ãºnica opÃ§Ã£o por mensagem, precisa mudar.',
     'Abra https://linnoff88-dev.github.io/ escolha o caso mais prÃ³ximo do seu trabalho e reescreva uma das perguntas dele com os seus critÃ©rios.'),
   T('O curso: 3 trilhas, 36 aulas',
     'O curso "Jev na prÃ¡tica" tem trÃªs trilhas, 12 mÃ³dulos e 36 aulas com teoria, exemplos, exercÃ­cios e respostas. A trilha Entender cobre onde o Jev entra, os trÃªs tipos de pergunta, confianÃ§a e erro, e custo; Aplicar trata atendimento, documentos, modelos e agentes, e navegador; Construir e avaliar cobre integraÃ§Ã£o, mediÃ§Ã£o de qualidade, operaÃ§Ã£o e o projeto final. Os mÃ³dulos 1 a 8 sÃ£o conceituais; os mÃ³dulos 9 a 12 usam JSON, terminal e Python, e a estimativa Ã© de 18 horas. SÃ£o 12 laboratÃ³rios com dados fictÃ­cios e gabaritos, e o projeto final pede concluir se hÃ¡ evidÃªncia para adotar, coletar mais dados ou nÃ£o automatizar. O curso HTML v2 estÃ¡ em portuguÃªs, com progresso, dÃºvidas e anotaÃ§Ãµes.',
     'O curso leva de "entender a ideia" a "decidir a adoÃ§Ã£o" com rubrica. O projeto final aceita a resposta "nÃ£o automatizar", o que treina julgamento em vez de entusiasmo.',
     'Entender; Aplicar; Construir e avaliar; 12 mÃ³dulos; 36 aulas; 12 laboratÃ³rios; projeto final; 18 horas',
     'Uma analista sem programaÃ§Ã£o faz os mÃ³dulos 1 a 8 e resolve os laboratÃ³rios de atendimento e evidÃªncias. O colega que programa segue para os mÃ³dulos 9 a 12 e monta a requisiÃ§Ã£o real.',
     'Abra o curso em https://linnoff88-dev.github.io/ e escolha o mÃ³dulo que corresponde Ã  decisÃ£o que vocÃª listou.'),
   T('17 pacotes e caminhos de uso',
     'Um pacote Ã© um kit por Ã¡rea com contexto, critÃ©rios, requisiÃ§Ã£o, fixture (um exemplo pronto para teste) e instruÃ§Ãµes. O acervo atual reÃºne 17, de atendimento e vendas a comentÃ¡rios do YouTube, reuniÃµes, cortes e curadoria. Todos compartilham o executor e o nÃºcleo Python: sem a opÃ§Ã£o --live o pacote usa a fixture simulada; com ela, faz uma consulta real, que requer chave no backend e pode consumir crÃ©ditos. HÃ¡ tambÃ©m execuÃ§Ã£o em lotes com retomada, a skill jev-decidir para Codex e Claude Code e o jev-gw, um gateway com teto de gasto diÃ¡rio, cache, registro de custo e falha conservadora que devolve revisÃ£o humana. Os pacotes estÃ£o no repositÃ³rio; ainda nÃ£o hÃ¡ distribuiÃ§Ã£o PyPI, instalador universal ou conector pronto para n8n.',
     'O caminho Ã© gradual: comeÃ§ar offline, entender a saÃ­da e sÃ³ depois pagar por consultas reais. O gateway mostra como proteger quem chama o Jev quando algo falha.',
     'pacote por Ã¡rea; fixture; --live; lotes e retomada; skill jev-decidir; jev-gw; falha conservadora',
     'Uma equipe de conteÃºdo usa o pacote de comentÃ¡rios do YouTube primeiro com a fixture. Quando a saÃ­da faz sentido, configura a consulta real no servidor e coloca o jev-gw na frente, para que um teto estourado mande o caso para revisÃ£o em vez de quebrar o sistema.',
     'Escolha, entre os 17 pacotes da pÃ¡gina, o que mais se parece com o seu trabalho e anote em que ponto do seu processo ele entraria.'),
   T('O que foi observado e o que falta',
     'A pÃ¡gina separa quatro situaÃ§Ãµes. SimulaÃ§Ã£o para aprender: os 20 casos e o replay sÃ£o autorais e simulados, nÃ£o medem a qualidade do modelo. Baseline de regras: 20 acertos em 24 tickets fictÃ­cios (83,33%), resultado das regras, nÃ£o do Jev. IntegraÃ§Ã£o real testada: em 19/09/2026 os dez pacotes originais receberam respostas pelo OpenRouter com as classificaÃ§Ãµes esperadas nos exemplos fictÃ­cios, o que confirma integraÃ§Ã£o, nÃ£o benchmark; os sete pacotes novos sÃ³ tÃªm testes controlados. AvaliaÃ§Ã£o ainda necessÃ¡ria: qualidade em portuguÃªs, calibraÃ§Ã£o e uso operacional pedem dados independentes e referÃªncia humana. O Laya, alternativa local em avaliaÃ§Ã£o, teve 14 testes da aplicaÃ§Ã£o aprovados e 13 acertos em 16 exemplos sintÃ©ticos, o que nÃ£o comprova superioridade.',
     'Essa separaÃ§Ã£o Ã© o que torna a Ã¡rea confiÃ¡vel: cada nÃºmero vem com o que ele prova e o que nÃ£o prova. Repetir esses nÃºmeros fora de contexto seria inflar o resultado.',
     'simulaÃ§Ã£o; baseline de regras; integraÃ§Ã£o real; avaliaÃ§Ã£o necessÃ¡ria; Laya em avaliaÃ§Ã£o; nÃ£o Ã© benchmark',
     'Um gestor lÃª "dez consultas reais sem falhas" e quase aprova a adoÃ§Ã£o. Ao ler a seÃ§Ã£o inteira, vÃª que o teste confirma que a integraÃ§Ã£o funciona, nÃ£o que o Jev acerta com os dados da empresa, e pede um piloto com referÃªncia humana.',
     'Para a sua decisÃ£o, escreva uma linha em cada coluna: o que vocÃª jÃ¡ observou e o que falta medir antes de automatizar.')],
  ('Prompt: minha decisÃ£o estruturada com JEV',
   'Leia https://eventos.ARCKHÉ.pro/jev/ e o guia https://linnoff88-dev.github.io/
   'Quero transformar uma decisÃ£o repetitiva do meu trabalho numa decisÃ£o estruturada, sem prometer qualidade que eu nÃ£o medi.\n'
   'Minha decisÃ£o: <descreva, ex.: para qual equipe vai cada e-mail de cliente>.\n'
   'OpÃ§Ãµes ou nÃ­veis possÃ­veis: <liste>.\n'
   '1. Diga se a pergunta Ã© Choice, Noul ou Score e por quÃª.\n'
   '2. Escreva o contexto mÃ­nimo, os critÃ©rios e a pergunta.\n'
   '3. Proponha a polÃ­tica: quando seguir a sugestÃ£o, quando se abster e quando mandar para revisÃ£o humana.\n'
   '4. Indique qual dos 20 casos do laboratÃ³rio e qual dos 17 pacotes da pÃ¡gina mais se parecem com a minha decisÃ£o.\n'
   '5. Monte a lista "jÃ¡ observado x falta medir" para o meu caso. NÃ£o trate simulaÃ§Ã£o como medida de qualidade.'),
  [('Ãrea JEV Â· eventos.ARCKHÉ.pro','https://eventos.ARCKHÉ.pro/jev/'),
   ('LaboratÃ³rio JEV','https://linnoff88-dev.github.io/
   ('Curso JEV','https://linnoff88-dev.github.io/
   ('Guia do jev-gw','https://linnoff88-dev.github.io/
  'jev')

FIGURES[(1,2)] = dict(kind='columns',
  caption='A forma da pergunta vem do tipo de resposta que o seu processo precisa usar: uma opÃ§Ã£o, uma chance de sim ou um nÃ­vel.',
  items=[('Choice','uma alternativa'),('Noul','probabilidade de sim'),('Score','nÃ­veis ordenados')])
FIGURES[(1,4)] = dict(kind='timeline',
  caption='As trÃªs trilhas vÃ£o do conceito ao projeto final; os mÃ³dulos 9 a 12 sÃ£o os Ãºnicos que pedem JSON, terminal e Python.',
  items=[('Entender','mÃ³dulos 1-4'),('Aplicar','mÃ³dulos 5-8'),('Construir','mÃ³dulos 9-12'),('Projeto final','adotar ou nÃ£o')])
FIGURES[(1,5)] = dict(kind='flow',
  caption='Comece simples e avance quando precisar: a consulta real sÃ³ entra depois do teste offline, e o gateway protege quem chama.',
  items=['Navegador','Servidor local','Pacote offline','Consulta --live','Lotes','jev-gw'])
FIGURES[(1,6)] = dict(kind='columns',
  caption='Cada evidÃªncia tem um alcance: sÃ³ a Ãºltima coluna mediria qualidade real, e ela ainda estÃ¡ por fazer.',
  items=[('SimulaÃ§Ã£o','para aprender'),('Baseline','regras, nÃ£o Jev'),('IntegraÃ§Ã£o','funciona, nÃ£o mede'),('AvaliaÃ§Ã£o','ainda necessÃ¡ria')])

# ---------------------------------------------------------------- 2 Â· WebMCP
M('WebMCP: seu site conversando com agentes',
  'Explicar o que muda quando agentes visitam sites, o que Ã© WebMCP e qual Ã© o primeiro passo concreto: diagnosticar o prÃ³prio site e corrigir o bÃ¡sico.',
  'O diagnÃ³stico do seu site',
  ['Rode o WebMCP Readiness em webmcp.ARCKHÉ.pro com a URL do seu site e anote a nota geral e as quatro notas (WebMCP, SEO, GEO, AEO).',
   'Liste os bloqueadores que aparecem primeiro no plano de correÃ§Ã£o e confira se robots.txt, sitemap.xml e llms.txt existem no seu domÃ­nio.',
   'Corrija um item das seis dicas da pÃ¡gina, como title, description ou JSON-LD, sem mexer em nada perigoso.',
   'Rode o scan de novo e compare as notas com a linha de base; registre o que subiu e o que ainda depende de revisÃ£o humana.'],
  'O scanner encontrou uma ferramenta declarada num script do seu site. Isso garante que ela estÃ¡ protegida e funciona para todo visitante?',
  'NÃ£o. O scanner prova o que Ã© observÃ¡vel; autorizaÃ§Ã£o real no backend, idempotÃªncia, correspondÃªncia entre descriÃ§Ã£o e efeito e se a definiÃ§Ã£o estÃ¡ registrada para todo visitante exigem revisÃ£o humana.',
  [T('O que Ã© WebMCP',
     'WebMCP Ã© uma forma de a prÃ³pria pÃ¡gina descrever o que sabe fazer para agentes de IA. Sem WebMCP, o agente precisa localizar campos, clicar, digitar e interpretar a tela, e isso quebra quando o layout muda. Com WebMCP, a pÃ¡gina expÃµe ferramentas com nome, descriÃ§Ã£o, schema de argumentos e resposta, e o agente chama a ferramenta certa pelo nome. HÃ¡ dois caminhos: a ferramenta declarativa, em que um formulÃ¡rio que jÃ¡ existe ganha um toolname e uma descriÃ§Ã£o, e a imperativa, em que JavaScript registra capacidades com JSON Schema, tratando estado, erros, cancelamento e fallback. Ã‰ uma tecnologia experimental, hoje atrÃ¡s de Origin Trial no navegador, ou seja, liberada em carÃ¡ter de teste.',
     'Ã‰ a diferenÃ§a entre o agente adivinhar e o site dizer. O site passa a decidir o que Ã© permitido, o que precisa de confirmaÃ§Ã£o e o que pode ser cancelado.',
     'operar pixels x conversar com capacidades; ferramenta declarativa; ferramenta imperativa; JSON Schema; Origin Trial',
     'Sem WebMCP, o agente digita o nome do curso, clica no botÃ£o azul e "acha que deu certo". Com WebMCP, o site expÃµe verificar_vagas e iniciar_inscricao; o agente chama a primeira, confirma que hÃ¡ vaga, e a segunda exige confirmaÃ§Ã£o humana antes de concluir.',
     'Escolha um formulÃ¡rio do seu site e escreva o nome e a descriÃ§Ã£o de uma linha que ele teria como ferramenta.'),
   T('O prÃ³ximo visitante Ã© um agente',
     'A pÃ¡gina lista seis mudanÃ§as. Do lado de quem visita: agentes jÃ¡ operam o navegador, preenchendo formulÃ¡rios e concluindo tarefas; buscar virou perguntar a um assistente, o que cria o problema de GEO e AEO; e o padrÃ£o estÃ¡ nascendo agora. Do lado de quem publica: o site deixa de ser sÃ³ uma tela e ganha um catÃ¡logo de capacidades por cima da jornada humana; descoberta vira requisito, com robots.txt, sitemap.xml, llms.txt, JSON-LD, Open Graph e uma identidade clara; e a seguranÃ§a fica com o site, nÃ£o com o modelo. GEO e AEO sÃ£o as prÃ¡ticas de aparecer e ser citado nas respostas de assistentes de IA, e nÃ£o sÃ³ em buscadores.',
     'Se vocÃª Ã© dono do site, as trÃªs Ãºltimas mudanÃ§as sÃ£o a sua lista de trabalho. Quem entende as limitaÃ§Ãµes cedo aprende com custo baixo.',
     'agentes no navegador; buscar virou perguntar; GEO e AEO; catÃ¡logo de capacidades; descoberta; seguranÃ§a no site',
     'Uma escola percebe que alunos perguntam a um assistente "qual curso de agentes comeÃ§a este mÃªs" em vez de buscar no site. A resposta depende do que o modelo consegue extrair das pÃ¡ginas dela, e o SEO clÃ¡ssico sozinho nÃ£o resolve.',
     'Escreva quais das trÃªs mudanÃ§as do lado de quem publica o seu site ainda nÃ£o atende.'),
   T('DiagnÃ³stico gratuito: Readiness',
     'O WebMCP Readiness, em webmcp.ARCKHÉ.pro, abre a URL num navegador descartÃ¡vel, reÃºne sinais observÃ¡veis e transforma o scan num plano de correÃ§Ã£o. Ã‰ um scanner passivo: consulta robots.txt, sitemap.xml e llms.txt e nÃ£o executa nenhuma ferramenta do site. VocÃª recebe nota geral e quatro notas independentes, WebMCP, SEO, GEO e AEO, com evidÃªncias, alertas, bloqueadores, atÃ© 12 correÃ§Ãµes priorizadas e os cursos indicados para cada lacuna, num relatÃ³rio em JSON. O scan aprofunda sÃ³ a URL informada; o sitemap Ã© inventariado, mas suas pÃ¡ginas nÃ£o sÃ£o rastreadas. Os scanners avanÃ§ados por fase aparecem no relatÃ³rio como planejados, nÃ£o como prontos.',
     'ComeÃ§ar pelo diagnÃ³stico mostra onde o seu site estÃ¡ antes de estudar. E a pÃ¡gina deixa claro o limite: indexaÃ§Ã£o, ranking ou citaÃ§Ã£o por IA, o scanner nÃ£o promete nada disso.',
     'scanner passivo; navegador descartÃ¡vel; nota geral + quatro notas; atÃ© 12 correÃ§Ãµes; relatÃ³rio JSON; o que exige revisÃ£o humana',
     'Uma agÃªncia roda o scan na pÃ¡gina de contato de um cliente e recebe o bloqueador "sem llms.txt" no topo do plano. Ela corrige, roda de novo e usa as duas notas para mostrar o avanÃ§o, sem prometer ranking.',
     'Rode o scan em https://webmcp.ARCKHÉ.pro/ com a pÃ¡gina principal do seu site e salve o relatÃ³rio JSON como linha de base.'),
   T('Oito camadas de um site pronto',
     'A pÃ¡gina organiza a arquitetura em oito camadas, na ordem em que a formaÃ§Ã£o constrÃ³i. As quatro primeiras sÃ£o o site se descrevendo: descoberta (o agente acha o site?), ferramentas (o que o site sabe fazer?), contrato (como se chama e o que volta?) e estado e erros (e quando dÃ¡ errado?). As quatro Ãºltimas sÃ£o o site se protegendo: controle (quem confirma?), permissÃµes (quem pode chamar?), backend e MCP (onde mora a verdade?) e evals e observabilidade (estÃ¡ funcionando mesmo?). A regra que atravessa todas: a LLM escolhe a ferramenta; o site decide se ela pode rodar. O diagnÃ³stico jÃ¡ mede a camada 1 inteira e os sinais observÃ¡veis das camadas 2 e 5.',
     'As camadas mostram que expor uma ferramenta Ã© sÃ³ o comeÃ§o. Sem confirmaÃ§Ã£o, permissÃµes e autorizaÃ§Ã£o no backend, um agente pode acionar algo que nÃ£o deveria.',
     'descoberta; ferramentas; contrato; estado e erros; controle; permissÃµes; backend e MCP; evals',
     'Uma loja expÃµe a ferramenta de consulta de pedido. A descriÃ§Ã£o diz "sÃ³ consulta", o backend confere se quem chama pode ver aquele pedido, e qualquer alteraÃ§Ã£o exige confirmaÃ§Ã£o humana. Logs mostram depois se a ferramenta fez o que dizia.',
     'Marque, para o seu site, quais das oito camadas vocÃª jÃ¡ cobre e qual pergunta de camada vocÃª nÃ£o saberia responder hoje.'),
   T('Seis correÃ§Ãµes para esta semana',
     'Antes de qualquer fase da formaÃ§Ã£o, a pÃ¡gina traz seis correÃ§Ãµes que o dono do site faz, cada uma ligada a um item que o scanner verifica. Primeiro, rode o scan e anote as notas como linha de base. Segundo, publique os trÃªs arquivos pÃºblicos: robots.txt, sitemap.xml atualizado e um llms.txt que apresenta o site para modelos de IA. Terceiro, arrume o bÃ¡sico de SEO que o agente tambÃ©m lÃª: title, description, canonical, headings em ordem, alt nas imagens, Open Graph e JSON-LD. Quarto, escreva para quem responde perguntas, com respostas diretas, definiÃ§Ãµes, listas e tabelas; quinto, mostre quem estÃ¡ por trÃ¡s, com entidade, autoria, data de atualizaÃ§Ã£o e evidÃªncias. Sexto, escolha como primeira ferramenta um formulÃ¡rio que nÃ£o muda nada perigoso, como uma busca ou consulta de status.',
     'SÃ£o correÃ§Ãµes que nÃ£o exigem programar ferramentas e jÃ¡ sobem as notas. A pÃ¡gina resume o mÃ©todo: corrija, rode de novo, veja a nota subir.',
     'linha de base; robots.txt, sitemap.xml, llms.txt; SEO bÃ¡sico; AEO: respostas diretas; GEO: autoria e evidÃªncias; primeira ferramenta segura',
     'Um consultor autÃ´nomo publica o llms.txt, acrescenta data de atualizaÃ§Ã£o e autoria nos artigos e cria uma seÃ§Ã£o de perguntas frequentes com respostas curtas. Na semana seguinte, as notas de GEO e AEO do scan sobem, sem nenhuma linha de JavaScript nova.',
     'FaÃ§a hoje a dica 2: confira se seu domÃ­nio responde em /robots.txt, /sitemap.xml e /llms.txt e anote o que falta.'),
   T('A formaÃ§Ã£o e onde continuar',
     'A FormaÃ§Ã£o WebMCP tem uma visÃ£o geral e quatro fases, todas abertas e em portuguÃªs: Builder (construir), Integrator (integrar), Agent Developer (orquestrar) e Expert (operar). Cada fase tem quatro mÃ³dulos de seis tÃ³picos e usa JavaScript; quem nÃ£o programa comeÃ§a pela visÃ£o geral e pelo diagnÃ³stico e leva as fases para o time. As camadas 1 e 2 sÃ£o ensinadas no Builder, 3 e 4 no Integrator, 5 e 6 no Agent Developer, e 7 e 8 no Expert. Ao lado, a pÃ¡gina indica o AIV 2026 para AEO e GEO, o curso de Computer Use com o GPT-6 Astra e o Super-Agentes, alÃ©m de projetos como o Kit do Arquiteto de Agentes, o ARCKHÉCCBOT e o os-agentes. O convite final Ã© direto: o melhor primeiro mÃ³dulo Ã© o seu prÃ³prio site.',
     'Saber em qual fase cada camada Ã© ensinada permite entrar na formaÃ§Ã£o pelo ponto do seu papel, em vez de comeÃ§ar tudo do zero.',
     'visÃ£o geral; Builder; Integrator; Agent Developer; Expert; quatro mÃ³dulos de seis tÃ³picos; cursos ao lado',
     'Uma dona de loja virtual faz o diagnÃ³stico e a visÃ£o geral. O desenvolvedor da equipe comeÃ§a pelo Builder para transformar a busca de produtos em ferramenta declarativa, e a parte de permissÃµes fica para quando ele chegar ao Agent Developer.',
     'Abra a visÃ£o geral em https://linnoff88-dev.github.io/ e escolha a fase que corresponde ao seu papel.')],
  ('Prompt: plano WebMCP para o meu site',
   'Leia https://eventos.ARCKHÉ.pro/webmcp/.\n'
   'Rodei o diagnÃ³stico em https://webmcp.ARCKHÉ.pro/ para o meu site: <URL do seu site>.\n'
   'Resultado do scan (cole o JSON ou as notas e bloqueadores): <cole aqui>.\n'
   '1. Explique cada bloqueador em linguagem simples e diga a qual das oito camadas ele pertence.\n'
   '2. Monte a lista desta semana usando as seis correÃ§Ãµes da pÃ¡gina, na ordem certa para o meu caso.\n'
   '3. Sugira UMA primeira ferramenta declarativa a partir de um formulÃ¡rio meu que nÃ£o muda nada perigoso: nome, descriÃ§Ã£o e argumentos.\n'
   '4. Separe o que o scanner consegue provar do que exige revisÃ£o humana (autorizaÃ§Ã£o no backend, idempotÃªncia, descriÃ§Ã£o x efeito real).\n'
   '5. Indique a fase da FormaÃ§Ã£o WebMCP por onde eu ou meu time devemos comeÃ§ar.\n'
   'NÃ£o prometa ranking, indexaÃ§Ã£o ou citaÃ§Ã£o por IA.'),
  [('Ãrea WebMCP Â· eventos.ARCKHÉ.pro','https://eventos.ARCKHÉ.pro/webmcp/'),
   ('WebMCP Readiness','https://webmcp.ARCKHÉ.pro/'),
   ('FormaÃ§Ã£o WebMCP','https://linnoff88-dev.github.io/
   ('WebMCP Builder','https://linnoff88-dev.github.io/
  'webmcp')

FIGURES[(2,2)] = dict(kind='grid',
  caption='As trÃªs primeiras mudanÃ§as acontecem com quem visita; as trÃªs Ãºltimas sÃ£o a lista de trabalho de quem publica o site.',
  items=['Agente navega','Perguntar','PadrÃ£o novo','CatÃ¡logo','Descoberta','SeguranÃ§a site'])
FIGURES[(2,3)] = dict(kind='columns',
  caption='O Readiness devolve quatro notas independentes: WebMCP mede ferramentas; SEO, GEO e AEO medem se o site Ã© achado e citado.',
  items=[('WebMCP','ferramentas e schemas'),('SEO','title, canonical'),('GEO','entidade e autoria'),('AEO','respostas diretas')])
FIGURES[(2,4)] = dict(kind='stack',
  caption='As quatro camadas de baixo descrevem o site; as quatro de cima o protegem. Expor ferramenta sem as de cima Ã© experimento, nÃ£o operaÃ§Ã£o.',
  items=[('Descoberta','o agente acha?'),('Ferramentas','o que faz?'),('Contrato','o que volta?'),('Estado e erros','e se falhar?'),('Controle e permissÃµes','quem confirma e chama?'),('Backend, MCP, evals','onde mora a verdade?')])
FIGURES[(2,6)] = dict(kind='timeline',
  caption='A formaÃ§Ã£o sobe do diagnÃ³stico Ã  produÃ§Ã£o: cada fase ensina duas das oito camadas.',
  items=[('VisÃ£o geral','comece aqui'),('Builder','camadas 1-2'),('Integrator','camadas 3-4'),('Agent Dev.','camadas 5-6'),('Expert','camadas 7-8')])
