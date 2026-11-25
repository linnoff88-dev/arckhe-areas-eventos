"""Trilha 3 ê¢â¬â Melhorar, decidir e abrir para agentes. Fontes: ARCKHêeventos/{rsi,jev,webmcp}/index.html + shared/acesso.json + rsi/CONTEUDO.md + jev/CONTEUDO.md (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

# ---------------------------------------------------------------- 0 êÂ· RSI
M('RSI: a IA que ajuda a melhorar a IA',
  'Explicar os trêÂªs nêÂ­veis de melhoria em IA e transformar uma ideia de melhoria num teste verificêÂ¡vel, com versêÂ£o registrada e caminho de volta.',
  'Seu primeiro ciclo de melhoria no papel',
  ['Escolha uma tarefa pequena do seu trabalho, como extrair aêÂ§êÂµes de notas de reuniêÂ£o, e escreva qual seria a resposta correta para trêÂªs exemplos fictêÂ­cios.',
   'Separe esses exemplos em dois grupos: dois para desenvolver a mudanêÂ§a e um reservado, que vocêÂª sêÂ³ usa na validaêÂ§êÂ£o.',
   'Registre a versêÂ£o inicial da instruêÂ§êÂ£o, proponha UMA mudanêÂ§a e rode as duas versêÂµes nos mesmos exemplos, anotando acertos, erros, custo e tempo de revisêÂ£o.',
   'Confira no exemplo reservado se a mudanêÂ§a se sustenta; sêÂ³ entêÂ£o adote, e anote quem decidiu e como voltar êÂ  versêÂ£o anterior.'],
  'Depois de dez tentativas, a nova instruêÂ§êÂ£o tirou nota maior no mesmo conjunto que vocêÂª usou para ajustêÂ¡-la. Isso prova que ela êÂ© melhor?',
  'NêÂ£o. Uma avaliaêÂ§êÂ£o conhecida pode ser explorada; a mudanêÂ§a precisa se sustentar em casos reservados, com os mesmos critêÂ©rios. Mais tentativas ou uma nota maior nêÂ£o demonstram crescimento ilimitado.',
  [T('O que êÂ© RSI',
     'RSI êÂ© a sigla em inglêÂªs para automelhoria recursiva: a ideia de uma IA que ajuda a melhorar a prêÂ³pria IA. A pergunta central da êÂ¡rea êÂ© prêÂ¡tica: como um sistema propêÂµe mudanêÂ§as, testa resultados e conserva o que funciona? A pêÂ¡gina trata o tema como êÂ¡rea de estudo e acervo aberto, com referêÂªncias, exemplos e critêÂ©rios para avaliar as promessas. O ponto de partida êÂ© uma distinêÂ§êÂ£o: melhorar uma resposta, melhorar um agente e melhorar a capacidade de criar novos agentes sêÂ£o coisas diferentes. Um agente, aqui, êÂ© um sistema de IA que recebe um objetivo e executa etapas com instruêÂ§êÂµes, memêÂ³ria e ferramentas.',
     'Promessas de IA que se melhora sozinha aparecem com frequêÂªncia e costumam misturar esses trêÂªs nêÂ­veis. Quem entende a diferenêÂ§a consegue perguntar o que exatamente melhorou e qual evidêÂªncia sustenta isso.',
     'automelhoria recursiva; propor, testar, conservar; trêÂªs nêÂ­veis diferentes; acervo aberto; critêÂ©rios para avaliar promessas',
     'Um fornecedor diz que seu assistente "aprende sozinho". A gestora pergunta: ele refaz a resposta, muda as prêÂ³prias instruêÂ§êÂµes ou produz melhorias futuras? E como isso foi medido? A resposta define se o produto estêÂ¡ no primeiro, no segundo ou no terceiro nêÂ­vel.',
     'Escreva em uma frase uma promessa de melhoria automêÂ¡tica que vocêÂª jêÂ¡ ouviu e marque qual dos trêÂªs nêÂ­veis ela realmente descreve.'),
   T('TrêÂªs nêÂ­veis que nêÂ£o se confundem',
     'O primeiro nêÂ­vel êÂ© revisar a resposta: o modelo critica e refaz uma saêÂ­da. Isso pode melhorar uma tarefa sem alterar seus parêÂ¢metros, os valores internos aprendidos no treino, nem seu processo de desenvolvimento. O segundo nêÂ­vel êÂ© melhorar o sistema: mudam as instruêÂ§êÂµes, a memêÂ³ria, as ferramentas ou o cêÂ³digo do agente, e as versêÂµes precisam ser comparadas com tarefas reservadas, preservando a possibilidade de voltar atrêÂ¡s. O terceiro êÂ© investigar a recursêÂ£o: a melhoria passa a ajudar a produzir melhorias futuras. Esse mecanismo precisa de evidêÂªncia, porque mais tentativas ou uma nota maior nêÂ£o demonstram crescimento ilimitado.',
     'Cada nêÂ­vel exige um tipo de controle diferente. Revisar uma resposta êÂ© barato e reversêÂ­vel; mudar o sistema pede registro de versêÂµes e testes; afirmar recursêÂ£o pede evidêÂªncia forte. Confundir os nêÂ­veis leva a aceitar garantias que ninguêÂ©m mediu.',
     'revisar a resposta; melhorar o sistema; investigar a recursêÂ£o; parêÂ¢metros; tarefas reservadas; possibilidade de voltar atrêÂ¡s',
     'Uma equipe pede ao modelo que revise o prêÂ³prio resumo antes de entregar: isso êÂ© nêÂ­vel 1. Depois reescreve a instruêÂ§êÂ£o do agente de atendimento e compara as duas versêÂµes em casos separados: nêÂ­vel 2. Nenhuma das duas coisas, sozinha, êÂ© uma IA criando IAs melhores.',
     'Classifique trêÂªs melhorias que vocêÂª jêÂ¡ fez em prompts ou agentes nos trêÂªs nêÂ­veis da pêÂ¡gina e anote se alguma delas tinha caminho de volta.'),
   T('Da ideia a um teste verificêÂ¡vel',
     'A pêÂ¡gina propêÂµe comeêÂ§ar com uma tarefa pequena: responder com base numa polêÂ­tica, criar questêÂµes a partir de um texto ou extrair aêÂ§êÂµes de notas. Primeiro defina a tarefa, a referêÂªncia correta e os limites de dados, gasto e aêÂ§êÂµes. Depois registre a versêÂ£o inicial e separe casos de desenvolvimento de casos reservados para validaêÂ§êÂ£o. Proponha uma mudanêÂ§a por vez e compare com os mesmos critêÂ©rios, incluindo erros, custo e esforêÂ§o de revisêÂ£o. Por fim, valide antes de adotar: guarde resultados e versêÂµes, defina quem decide e mantenha um caminho de reversêÂ£o.',
     'Uma avaliaêÂ§êÂ£o conhecida pode ser explorada, e a pêÂ¡gina alerta para isso. Preservar a independêÂªncia dos testes, conferir dados inventados e olhar resultados fora da amostra evita confundir ganho local com autonomia geral.',
     'tarefa pequena; referêÂªncia correta; casos reservados; uma mudanêÂ§a por vez; mesmos critêÂ©rios; validar antes de adotar; reversêÂ£o',
     'Uma escola testa uma instruêÂ§êÂ£o que cria questêÂµes a partir de um texto. Usa quatro textos para ajustar e guarda dois que ninguêÂ©m viu. A versêÂ£o nova acerta mais nos quatro, mas erra num dos reservados; a coordenaêÂ§êÂ£o decide manter a versêÂ£o antiga atêÂ© entender o erro.',
     'Escolha uma tarefa sua e escreva as quatro linhas: tarefa e referêÂªncia; versêÂ£o inicial e casos reservados; a êÂºnica mudanêÂ§a; quem decide e como voltar.'),
   T('LOOP-R: o ciclo com freios',
     'LOOP-R êÂ© o framework do projeto para organizar melhorias: Executar, Medir, Criticar, Propor, Testar, Validar, Promover e Repetir. A pêÂ¡gina o descreve como pronto para usar no Claude Code, com nove assistentes de funêÂ§êÂµes separadas, registro de cada versêÂ£o, teto de custo e comando para reverter. A regra de seguranêÂ§a êÂ© explêÂ­cita: nenhuma versêÂ£o pior substitui a atual por decisêÂ£o do sistema. No curso RSI, o LOOP-R aparece como uma proposta conceitual do projeto. HêÂ¡ tambêÂ©m um curso LOOP-R com cinco trilhas e 21 aulas para donos e gestores sem base têÂ©cnica.',
     'Um ciclo de melhoria sem freios pode trocar uma versêÂ£o boa por uma pior sem ninguêÂ©m perceber. Teto de custo, registro de versêÂµes e reversêÂ£o tornam o ciclo auditêÂ¡vel e seguro de repetir.',
     'Executar; Medir; Criticar; Propor; Testar; Validar; Promover; Repetir; nove assistentes; teto de custo; reverter',
     'Um gestor usa o ciclo para melhorar a instruêÂ§êÂ£o que classifica pedidos de clientes. Cada rodada gera uma versêÂ£o registrada; quando a nova versêÂ£o piora num teste, ela nêÂ£o êÂ© promovida e a atual continua valendo.',
     'Abra o guia do LOOP-R e anote em qual das oito etapas o seu processo atual de ajuste de prompts costuma parar.'),
   T('Por onde comeêÂ§ar: curso e guia',
     'A seêÂ§êÂ£o "Comece por aqui" traz dois materiais. O curso RSI v6.2 tem 18 aulas em seis mêÂ³dulos, com exercêÂ­cios, revisêÂ£o e materiais para aplicar o LOOP-R e registrar conhecimento aprovado, em portuguêÂªs, inglêÂªs e espanhol. O Guia RSI êÂ© um mapa do tema, com mecanismos, aplicaêÂ§êÂµes e limites, tambêÂ©m em trêÂªs idiomas. A pêÂ¡gina faz uma ressalva importante: o projeto reêÂºne pesquisa e conteêÂºdo educativo, e nêÂ£o êÂ© um sistema RSI autêÂ´nomo pronto para executar. O cêÂ³digo e os materiais ficam no repositêÂ³rio rsi no GitHub.',
     'ComeêÂ§ar pelo guia dêÂ¡ o vocabulêÂ¡rio e os limites; o curso transforma isso em prêÂ¡tica com exercêÂ­cios. Saber que o projeto êÂ© educativo evita esperar dele uma ferramenta que melhora sozinha.',
     'RSI v6.2; 18 aulas; seis mêÂ³dulos; Guia RSI; PT / EN / ES; conteêÂºdo educativo, nêÂ£o sistema autêÂ´nomo',
     'Uma consultora quer explicar RSI para uma diretoria. Usa o Guia RSI para montar o mapa dos trêÂªs nêÂ­veis e indica o curso RSI v6.2 para a pessoa do time que vai conduzir os testes de melhoria.',
     'Abra o Guia RSI, leia a parte de limites e anote uma frase que vocêÂª usaria para responder a quem promete IA que se melhora sozinha.'),
   T('O acervo: Copiloto, Dream-RSI, 2028',
     'AlêÂ©m do guia e do curso, o acervo reêÂºne trêÂªs materiais com ressalvas claras. O RSI Copiloto êÂ© um assistente local com IA, memêÂ³ria, tarefas e rotinas, que compara instruêÂ§êÂµes, pede revisêÂ£o humana e permite reverter mudanêÂ§as; a demonstraêÂ§êÂ£o pêÂºblica usa exemplos programados, sem IA, e a IA real fica sêÂ³ na versêÂ£o local. O Dream-RSI êÂ© um guia educativo independente, nêÂ£o afiliado ao Google, sobre aprender com histêÂ³ricos de experimentos; o laboratêÂ³rio e os oito encontros sêÂ£o planos futuros, nêÂ£o uma implementaêÂ§êÂ£o do artigo. O Alerta IA 2028 êÂ© um curso em trêÂªs trilhas, sobre o ciclo de melhoria, as evidêÂªncias e os limites da avaliaêÂ§êÂ£o, e trata os cenêÂ¡rios de 2028 como hipêÂ³teses, sem calendêÂ¡rio garantido. A pêÂ¡gina ainda lista referêÂªncias como Self-Refine, Reflexion, Darwin GêÂ¶del Machine e AlphaEvolve, consultadas em 25 de setembro de 2026, cujos resultados nêÂ£o foram reproduzidos no projeto.',
     'Cada material diz o que jêÂ¡ estêÂ¡ disponêÂ­vel e o que ainda êÂ© plano. Ler essas ressalvas êÂ© o prêÂ³prio exercêÂ­cio da êÂ¡rea: separar evidêÂªncia de promessa.',
     'RSI Copiloto; demonstraêÂ§êÂ£o sem IA; Dream-RSI independente; Alerta IA 2028; cenêÂ¡rios como hipêÂ³teses; referêÂªncias originais em inglêÂªs',
     'Um analista experimenta a demonstraêÂ§êÂ£o do Copiloto e percebe que as respostas sêÂ£o programadas. Em vez de concluir que "a IA acertou tudo", registra que precisa da versêÂ£o local para testar de verdade.',
     'Escolha um dos trêÂªs materiais e escreva o que ele jêÂ¡ entrega e o que a pêÂ¡gina diz que ainda êÂ© plano ou exemplo programado.')],
  ('Prompt: meu primeiro teste de melhoria (RSI)',
   'Leia https://eventos.ARCKHê.pro/rsi/ e o guia https://linnoff88-dev.github.io/
   'Quero testar uma melhoria numa tarefa do meu trabalho, sem prometer mais do que consigo medir.\n'
   'Minha tarefa: <descreva a tarefa, ex.: extrair aêÂ§êÂµes de notas de reuniêÂ£o>.\n'
   'Minha instruêÂ§êÂ£o atual: <cole a instruêÂ§êÂ£o ou prompt que vocêÂª usa hoje>.\n'
   '1. Diga em qual dos trêÂªs nêÂ­veis (revisar a resposta, melhorar o sistema, investigar a recursêÂ£o) a minha ideia se encaixa.\n'
   '2. Monte o teste: referêÂªncia correta, limites de dados/gasto/aêÂ§êÂµes, casos de desenvolvimento e casos reservados.\n'
   '3. Proponha UMA êÂºnica mudanêÂ§a na instruêÂ§êÂ£o e a tabela para comparar as duas versêÂµes (erros, custo, esforêÂ§o de revisêÂ£o).\n'
   '4. Diga quem deve decidir a adoêÂ§êÂ£o e como voltar êÂ  versêÂ£o anterior.\n'
   'NêÂ£o invente resultados: deixe os campos de resultado em branco para eu preencher.'),
  [('êÂrea RSI êÂ· eventos.ARCKHê.pro','https://eventos.ARCKHê.pro/rsi/'),
   ('Curso RSI v6.2','https://linnoff88-dev.github.io/
   ('Guia RSI','https://linnoff88-dev.github.io/
   ('Framework LOOP-R','https://linnoff88-dev.github.io/
  'rsi')

FIGURES[(0,2)] = dict(kind='timeline',
  caption='Os trêÂªs nêÂ­veis sobem em ambiêÂ§êÂ£o e em exigêÂªncia de prova: revisar uma resposta nêÂ£o altera o sistema, e sêÂ³ o terceiro nêÂ­vel fala em melhorias que geram melhorias.',
  items=[('Revisar','nêÂ­vel 1'),('Sistema','nêÂ­vel 2'),('RecursêÂ£o','nêÂ­vel 3')])
FIGURES[(0,3)] = dict(kind='flow',
  caption='Um teste verificêÂ¡vel separa ajuste de validaêÂ§êÂ£o: a mudanêÂ§a sêÂ³ êÂ© adotada depois de passar nos casos reservados, com reversêÂ£o possêÂ­vel.',
  items=['Definir tarefa','VersêÂ£o inicial','Uma mudanêÂ§a','Mesmos critêÂ©rios','Validar e decidir'])
FIGURES[(0,4)] = dict(kind='grid',
  caption='As oito etapas do LOOP-R repetem o ciclo, mas Validar e Promover funcionam como portêÂµes: versêÂ£o pior nêÂ£o substitui a atual.',
  items=['Executar','Medir','Criticar','Propor','Testar','Validar','Promover','Repetir'])
FIGURES[(0,6)] = dict(kind='columns',
  caption='Cada material do acervo traz sua ressalva: leia o subtêÂ­tulo antes de tirar conclusêÂµes sobre o que ele entrega.',
  items=[('RSI Copiloto','demo sem IA'),('Dream-RSI','independente'),('Alerta IA 2028','cenêÂ¡rios = hipêÂ³teses'),('LOOP-R','versêÂ£o pior nêÂ£o entra')])

# ---------------------------------------------------------------- 1 êÂ· JEV
M('JEV: decisêÂµes de IA na prêÂ¡tica',
  'Explicar o que êÂ© uma decisêÂ£o estruturada com Jev, escolher entre Choice, Noul e Score e separar o que jêÂ¡ foi observado do que ainda falta medir.',
  'Sua decisêÂ£o estruturada, do caso ao piloto',
  ['Abra o laboratêÂ³rio pêÂºblico do JEV, escolha um dos 20 casos e anote contexto, pergunta, critêÂ©rios e a resposta simulada.',
   'Escreva uma decisêÂ£o parecida do seu trabalho e indique se ela êÂ© Choice, Noul ou Score, justificando pelo tipo de resposta de que vocêÂª precisa.',
   'Defina a polêÂ­tica: com que confianêÂ§a a sugestêÂ£o segue, quando o sistema se abstêÂ©m e quando vai para revisêÂ£o humana.',
   'Confira sua ficha contra a seêÂ§êÂ£o "O que jêÂ¡ foi observado e o que falta medir": marque o que vocêÂª conseguiria medir com dados prêÂ³prios e referêÂªncia humana.'],
  'O laboratêÂ³rio pêÂºblico mostrou respostas corretas em todos os casos que vocêÂª abriu. Isso mede a qualidade do Jev?',
  'NêÂ£o. Os 20 casos pêÂºblicos e o replay sêÂ£o autorais e simulados; servem para estudar formulaêÂ§êÂ£o, polêÂ­ticas e erros. Qualidade em portuguêÂªs e calibraêÂ§êÂ£o ainda precisam de dados independentes e referêÂªncia humana.',
  [T('O que êÂ© o JEV',
     'Jev êÂ© o modelo de decisêÂµes estruturadas da TypeSafe. Uma decisêÂ£o estruturada êÂ© uma pergunta fechada, com contexto e critêÂ©rios, cuja resposta êÂ© uma escolha, uma probabilidade ou um nêÂ­vel, e nêÂ£o um texto livre. O Jev Decision Lab êÂ© o projeto educacional do ARCKHê para formular perguntas, comparar respostas e entender quando uma decisêÂ£o precisa de revisêÂ£o. O modelo recebe contexto e critêÂ©rios; o seu sistema continua responsêÂ¡vel pelas aêÂ§êÂµes. O laboratêÂ³rio separa essa escolha da geraêÂ§êÂ£o de texto e da execuêÂ§êÂ£o de ferramentas.',
     'Muitas tarefas de IA no trabalho nêÂ£o pedem um texto, pedem uma decisêÂ£o: para qual fila vai este chamado, este trecho sustenta a afirmaêÂ§êÂ£o. Separar decidir, gerar e executar deixa claro quem responde por cada parte e facilita medir o acerto.',
     'modelo de decisêÂµes estruturadas; TypeSafe; Jev Decision Lab; contexto e critêÂ©rios; o sistema responde pelas aêÂ§êÂµes',
     'Uma equipe de suporte quer que a IA encaminhe chamados. Em vez de pedir um parêÂ¡grafo, ela usa o Jev para escolher a fila entre opêÂ§êÂµes fixas; o sistema da empresa êÂ© quem move o chamado, e casos duvidosos vêÂ£o para uma pessoa.',
     'Liste duas decisêÂµes repetitivas do seu trabalho que hoje viram texto livre e reescreva cada uma como pergunta fechada com opêÂ§êÂµes.'),
   T('Choice, Noul e Score',
     'A pêÂ¡gina apresenta trêÂªs formas de perguntar. Choice escolhe entre alternativas explêÂ­citas, como qual fila ou qual agente. Noul estima a probabilidade de uma resposta afirmativa, como a chance de um trecho apoiar uma afirmaêÂ§êÂ£o. Score avalia uma rubrica com nêÂ­veis ordenados, como baixo, mêÂ©dio e alto. O curso dedica um mêÂ³dulo a distinguir as trêÂªs a partir do tipo de resposta necessêÂ¡rio, e outro a confianêÂ§a e erro: usar incerteza sem transformêÂ¡-la em autorizaêÂ§êÂ£o automêÂ¡tica.',
     'Escolher a forma errada produz respostas difêÂ­ceis de usar: uma nota quando vocêÂª precisava de uma fila, ou um sim quando havia vêÂ¡rios nêÂ­veis. A forma da pergunta define como vocêÂª vai medir e qual polêÂ­tica aplicar.',
     'Choice: alternativas explêÂ­citas; Noul: probabilidade de sim; Score: nêÂ­veis ordenados; confianêÂ§a nêÂ£o êÂ© autorizaêÂ§êÂ£o',
     'Na triagem de reuniêÂµes, "a ata tem responsêÂ¡vel e prazo?" êÂ© Noul; "qual equipe cuida disto?" êÂ© Choice; "qual a prioridade do log, de 1 a 4?" êÂ© Score. A mesma reuniêÂ£o pode gerar as trêÂªs perguntas.',
     'Pegue uma das decisêÂµes que vocêÂª listou e escreva-a nas trêÂªs formas; fique com a que devolve a resposta que o seu processo consegue usar.'),
   T('20 casos no laboratêÂ³rio pêÂºblico',
     'O laboratêÂ³rio abre no navegador, nêÂ£o pede chave e nêÂ£o consulta nenhuma API: as respostas sêÂ£o simuladas. Cada um dos 20 casos inclui contexto, perguntas, critêÂ©rios, resposta simulada, explicaêÂ§êÂ£o e prêÂ³ximo passo, como triagem de atendimento, checklist de contratos, roteamento de agentes e revisêÂ£o semêÂ¢ntica de diff. VocêÂª pode editar as perguntas, importar uma requisiêÂ§êÂ£o, exportar o resultado ou abrir um relatêÂ³rio; alterar um caso invalida sua resposta simulada anterior. Para ir alêÂ©m, êÂ© possêÂ­vel clonar o projeto e rodar o servidor local com Python 3.10 ou superior. O nêÂºcleo usa sêÂ³ a biblioteca padrêÂ£o.',
     'O laboratêÂ³rio permite errar sem custo e sem risco: vocêÂª aprende a formular o contexto, as opêÂ§êÂµes e a polêÂ­tica antes de gastar crêÂ©dito ou tocar num sistema real.',
     'laboratêÂ³rio sem chave; respostas simuladas; 20 casos; contexto, perguntas, critêÂ©rios; servidor local em Python',
     'Um coordenador abre o caso "IntenêÂ§êÂµes simultêÂ¢neas" e vêÂª que uma conversa pode conter vendas e agendamento ao mesmo tempo. Ele percebe que a pergunta da sua empresa, com uma êÂºnica opêÂ§êÂ£o por mensagem, precisa mudar.',
     'Abra https://linnoff88-dev.github.io/ escolha o caso mais prêÂ³ximo do seu trabalho e reescreva uma das perguntas dele com os seus critêÂ©rios.'),
   T('O curso: 3 trilhas, 36 aulas',
     'O curso "Jev na prêÂ¡tica" tem trêÂªs trilhas, 12 mêÂ³dulos e 36 aulas com teoria, exemplos, exercêÂ­cios e respostas. A trilha Entender cobre onde o Jev entra, os trêÂªs tipos de pergunta, confianêÂ§a e erro, e custo; Aplicar trata atendimento, documentos, modelos e agentes, e navegador; Construir e avaliar cobre integraêÂ§êÂ£o, mediêÂ§êÂ£o de qualidade, operaêÂ§êÂ£o e o projeto final. Os mêÂ³dulos 1 a 8 sêÂ£o conceituais; os mêÂ³dulos 9 a 12 usam JSON, terminal e Python, e a estimativa êÂ© de 18 horas. SêÂ£o 12 laboratêÂ³rios com dados fictêÂ­cios e gabaritos, e o projeto final pede concluir se hêÂ¡ evidêÂªncia para adotar, coletar mais dados ou nêÂ£o automatizar. O curso HTML v2 estêÂ¡ em portuguêÂªs, com progresso, dêÂºvidas e anotaêÂ§êÂµes.',
     'O curso leva de "entender a ideia" a "decidir a adoêÂ§êÂ£o" com rubrica. O projeto final aceita a resposta "nêÂ£o automatizar", o que treina julgamento em vez de entusiasmo.',
     'Entender; Aplicar; Construir e avaliar; 12 mêÂ³dulos; 36 aulas; 12 laboratêÂ³rios; projeto final; 18 horas',
     'Uma analista sem programaêÂ§êÂ£o faz os mêÂ³dulos 1 a 8 e resolve os laboratêÂ³rios de atendimento e evidêÂªncias. O colega que programa segue para os mêÂ³dulos 9 a 12 e monta a requisiêÂ§êÂ£o real.',
     'Abra o curso em https://linnoff88-dev.github.io/ e escolha o mêÂ³dulo que corresponde êÂ  decisêÂ£o que vocêÂª listou.'),
   T('17 pacotes e caminhos de uso',
     'Um pacote êÂ© um kit por êÂ¡rea com contexto, critêÂ©rios, requisiêÂ§êÂ£o, fixture (um exemplo pronto para teste) e instruêÂ§êÂµes. O acervo atual reêÂºne 17, de atendimento e vendas a comentêÂ¡rios do YouTube, reuniêÂµes, cortes e curadoria. Todos compartilham o executor e o nêÂºcleo Python: sem a opêÂ§êÂ£o --live o pacote usa a fixture simulada; com ela, faz uma consulta real, que requer chave no backend e pode consumir crêÂ©ditos. HêÂ¡ tambêÂ©m execuêÂ§êÂ£o em lotes com retomada, a skill jev-decidir para Codex e Claude Code e o jev-gw, um gateway com teto de gasto diêÂ¡rio, cache, registro de custo e falha conservadora que devolve revisêÂ£o humana. Os pacotes estêÂ£o no repositêÂ³rio; ainda nêÂ£o hêÂ¡ distribuiêÂ§êÂ£o PyPI, instalador universal ou conector pronto para n8n.',
     'O caminho êÂ© gradual: comeêÂ§ar offline, entender a saêÂ­da e sêÂ³ depois pagar por consultas reais. O gateway mostra como proteger quem chama o Jev quando algo falha.',
     'pacote por êÂ¡rea; fixture; --live; lotes e retomada; skill jev-decidir; jev-gw; falha conservadora',
     'Uma equipe de conteêÂºdo usa o pacote de comentêÂ¡rios do YouTube primeiro com a fixture. Quando a saêÂ­da faz sentido, configura a consulta real no servidor e coloca o jev-gw na frente, para que um teto estourado mande o caso para revisêÂ£o em vez de quebrar o sistema.',
     'Escolha, entre os 17 pacotes da pêÂ¡gina, o que mais se parece com o seu trabalho e anote em que ponto do seu processo ele entraria.'),
   T('O que foi observado e o que falta',
     'A pêÂ¡gina separa quatro situaêÂ§êÂµes. SimulaêÂ§êÂ£o para aprender: os 20 casos e o replay sêÂ£o autorais e simulados, nêÂ£o medem a qualidade do modelo. Baseline de regras: 20 acertos em 24 tickets fictêÂ­cios (83,33%), resultado das regras, nêÂ£o do Jev. IntegraêÂ§êÂ£o real testada: em 19/09/2026 os dez pacotes originais receberam respostas pelo OpenRouter com as classificaêÂ§êÂµes esperadas nos exemplos fictêÂ­cios, o que confirma integraêÂ§êÂ£o, nêÂ£o benchmark; os sete pacotes novos sêÂ³ têÂªm testes controlados. AvaliaêÂ§êÂ£o ainda necessêÂ¡ria: qualidade em portuguêÂªs, calibraêÂ§êÂ£o e uso operacional pedem dados independentes e referêÂªncia humana. O Laya, alternativa local em avaliaêÂ§êÂ£o, teve 14 testes da aplicaêÂ§êÂ£o aprovados e 13 acertos em 16 exemplos sintêÂ©ticos, o que nêÂ£o comprova superioridade.',
     'Essa separaêÂ§êÂ£o êÂ© o que torna a êÂ¡rea confiêÂ¡vel: cada nêÂºmero vem com o que ele prova e o que nêÂ£o prova. Repetir esses nêÂºmeros fora de contexto seria inflar o resultado.',
     'simulaêÂ§êÂ£o; baseline de regras; integraêÂ§êÂ£o real; avaliaêÂ§êÂ£o necessêÂ¡ria; Laya em avaliaêÂ§êÂ£o; nêÂ£o êÂ© benchmark',
     'Um gestor lêÂª "dez consultas reais sem falhas" e quase aprova a adoêÂ§êÂ£o. Ao ler a seêÂ§êÂ£o inteira, vêÂª que o teste confirma que a integraêÂ§êÂ£o funciona, nêÂ£o que o Jev acerta com os dados da empresa, e pede um piloto com referêÂªncia humana.',
     'Para a sua decisêÂ£o, escreva uma linha em cada coluna: o que vocêÂª jêÂ¡ observou e o que falta medir antes de automatizar.')],
  ('Prompt: minha decisêÂ£o estruturada com JEV',
   'Leia https://eventos.ARCKHê.pro/jev/ e o guia https://linnoff88-dev.github.io/
   'Quero transformar uma decisêÂ£o repetitiva do meu trabalho numa decisêÂ£o estruturada, sem prometer qualidade que eu nêÂ£o medi.\n'
   'Minha decisêÂ£o: <descreva, ex.: para qual equipe vai cada e-mail de cliente>.\n'
   'OpêÂ§êÂµes ou nêÂ­veis possêÂ­veis: <liste>.\n'
   '1. Diga se a pergunta êÂ© Choice, Noul ou Score e por quêÂª.\n'
   '2. Escreva o contexto mêÂ­nimo, os critêÂ©rios e a pergunta.\n'
   '3. Proponha a polêÂ­tica: quando seguir a sugestêÂ£o, quando se abster e quando mandar para revisêÂ£o humana.\n'
   '4. Indique qual dos 20 casos do laboratêÂ³rio e qual dos 17 pacotes da pêÂ¡gina mais se parecem com a minha decisêÂ£o.\n'
   '5. Monte a lista "jêÂ¡ observado x falta medir" para o meu caso. NêÂ£o trate simulaêÂ§êÂ£o como medida de qualidade.'),
  [('êÂrea JEV êÂ· eventos.ARCKHê.pro','https://eventos.ARCKHê.pro/jev/'),
   ('LaboratêÂ³rio JEV','https://linnoff88-dev.github.io/
   ('Curso JEV','https://linnoff88-dev.github.io/
   ('Guia do jev-gw','https://linnoff88-dev.github.io/
  'jev')

FIGURES[(1,2)] = dict(kind='columns',
  caption='A forma da pergunta vem do tipo de resposta que o seu processo precisa usar: uma opêÂ§êÂ£o, uma chance de sim ou um nêÂ­vel.',
  items=[('Choice','uma alternativa'),('Noul','probabilidade de sim'),('Score','nêÂ­veis ordenados')])
FIGURES[(1,4)] = dict(kind='timeline',
  caption='As trêÂªs trilhas vêÂ£o do conceito ao projeto final; os mêÂ³dulos 9 a 12 sêÂ£o os êÂºnicos que pedem JSON, terminal e Python.',
  items=[('Entender','mêÂ³dulos 1-4'),('Aplicar','mêÂ³dulos 5-8'),('Construir','mêÂ³dulos 9-12'),('Projeto final','adotar ou nêÂ£o')])
FIGURES[(1,5)] = dict(kind='flow',
  caption='Comece simples e avance quando precisar: a consulta real sêÂ³ entra depois do teste offline, e o gateway protege quem chama.',
  items=['Navegador','Servidor local','Pacote offline','Consulta --live','Lotes','jev-gw'])
FIGURES[(1,6)] = dict(kind='columns',
  caption='Cada evidêÂªncia tem um alcance: sêÂ³ a êÂºltima coluna mediria qualidade real, e ela ainda estêÂ¡ por fazer.',
  items=[('SimulaêÂ§êÂ£o','para aprender'),('Baseline','regras, nêÂ£o Jev'),('IntegraêÂ§êÂ£o','funciona, nêÂ£o mede'),('AvaliaêÂ§êÂ£o','ainda necessêÂ¡ria')])

# ---------------------------------------------------------------- 2 êÂ· WebMCP
M('WebMCP: seu site conversando com agentes',
  'Explicar o que muda quando agentes visitam sites, o que êÂ© WebMCP e qual êÂ© o primeiro passo concreto: diagnosticar o prêÂ³prio site e corrigir o bêÂ¡sico.',
  'O diagnêÂ³stico do seu site',
  ['Rode o WebMCP Readiness em webmcp.ARCKHê.pro com a URL do seu site e anote a nota geral e as quatro notas (WebMCP, SEO, GEO, AEO).',
   'Liste os bloqueadores que aparecem primeiro no plano de correêÂ§êÂ£o e confira se robots.txt, sitemap.xml e llms.txt existem no seu domêÂ­nio.',
   'Corrija um item das seis dicas da pêÂ¡gina, como title, description ou JSON-LD, sem mexer em nada perigoso.',
   'Rode o scan de novo e compare as notas com a linha de base; registre o que subiu e o que ainda depende de revisêÂ£o humana.'],
  'O scanner encontrou uma ferramenta declarada num script do seu site. Isso garante que ela estêÂ¡ protegida e funciona para todo visitante?',
  'NêÂ£o. O scanner prova o que êÂ© observêÂ¡vel; autorizaêÂ§êÂ£o real no backend, idempotêÂªncia, correspondêÂªncia entre descriêÂ§êÂ£o e efeito e se a definiêÂ§êÂ£o estêÂ¡ registrada para todo visitante exigem revisêÂ£o humana.',
  [T('O que êÂ© WebMCP',
     'WebMCP êÂ© uma forma de a prêÂ³pria pêÂ¡gina descrever o que sabe fazer para agentes de IA. Sem WebMCP, o agente precisa localizar campos, clicar, digitar e interpretar a tela, e isso quebra quando o layout muda. Com WebMCP, a pêÂ¡gina expêÂµe ferramentas com nome, descriêÂ§êÂ£o, schema de argumentos e resposta, e o agente chama a ferramenta certa pelo nome. HêÂ¡ dois caminhos: a ferramenta declarativa, em que um formulêÂ¡rio que jêÂ¡ existe ganha um toolname e uma descriêÂ§êÂ£o, e a imperativa, em que JavaScript registra capacidades com JSON Schema, tratando estado, erros, cancelamento e fallback. êâ° uma tecnologia experimental, hoje atrêÂ¡s de Origin Trial no navegador, ou seja, liberada em carêÂ¡ter de teste.',
     'êâ° a diferenêÂ§a entre o agente adivinhar e o site dizer. O site passa a decidir o que êÂ© permitido, o que precisa de confirmaêÂ§êÂ£o e o que pode ser cancelado.',
     'operar pixels x conversar com capacidades; ferramenta declarativa; ferramenta imperativa; JSON Schema; Origin Trial',
     'Sem WebMCP, o agente digita o nome do curso, clica no botêÂ£o azul e "acha que deu certo". Com WebMCP, o site expêÂµe verificar_vagas e iniciar_inscricao; o agente chama a primeira, confirma que hêÂ¡ vaga, e a segunda exige confirmaêÂ§êÂ£o humana antes de concluir.',
     'Escolha um formulêÂ¡rio do seu site e escreva o nome e a descriêÂ§êÂ£o de uma linha que ele teria como ferramenta.'),
   T('O prêÂ³ximo visitante êÂ© um agente',
     'A pêÂ¡gina lista seis mudanêÂ§as. Do lado de quem visita: agentes jêÂ¡ operam o navegador, preenchendo formulêÂ¡rios e concluindo tarefas; buscar virou perguntar a um assistente, o que cria o problema de GEO e AEO; e o padrêÂ£o estêÂ¡ nascendo agora. Do lado de quem publica: o site deixa de ser sêÂ³ uma tela e ganha um catêÂ¡logo de capacidades por cima da jornada humana; descoberta vira requisito, com robots.txt, sitemap.xml, llms.txt, JSON-LD, Open Graph e uma identidade clara; e a seguranêÂ§a fica com o site, nêÂ£o com o modelo. GEO e AEO sêÂ£o as prêÂ¡ticas de aparecer e ser citado nas respostas de assistentes de IA, e nêÂ£o sêÂ³ em buscadores.',
     'Se vocêÂª êÂ© dono do site, as trêÂªs êÂºltimas mudanêÂ§as sêÂ£o a sua lista de trabalho. Quem entende as limitaêÂ§êÂµes cedo aprende com custo baixo.',
     'agentes no navegador; buscar virou perguntar; GEO e AEO; catêÂ¡logo de capacidades; descoberta; seguranêÂ§a no site',
     'Uma escola percebe que alunos perguntam a um assistente "qual curso de agentes comeêÂ§a este mêÂªs" em vez de buscar no site. A resposta depende do que o modelo consegue extrair das pêÂ¡ginas dela, e o SEO clêÂ¡ssico sozinho nêÂ£o resolve.',
     'Escreva quais das trêÂªs mudanêÂ§as do lado de quem publica o seu site ainda nêÂ£o atende.'),
   T('DiagnêÂ³stico gratuito: Readiness',
     'O WebMCP Readiness, em webmcp.ARCKHê.pro, abre a URL num navegador descartêÂ¡vel, reêÂºne sinais observêÂ¡veis e transforma o scan num plano de correêÂ§êÂ£o. êâ° um scanner passivo: consulta robots.txt, sitemap.xml e llms.txt e nêÂ£o executa nenhuma ferramenta do site. VocêÂª recebe nota geral e quatro notas independentes, WebMCP, SEO, GEO e AEO, com evidêÂªncias, alertas, bloqueadores, atêÂ© 12 correêÂ§êÂµes priorizadas e os cursos indicados para cada lacuna, num relatêÂ³rio em JSON. O scan aprofunda sêÂ³ a URL informada; o sitemap êÂ© inventariado, mas suas pêÂ¡ginas nêÂ£o sêÂ£o rastreadas. Os scanners avanêÂ§ados por fase aparecem no relatêÂ³rio como planejados, nêÂ£o como prontos.',
     'ComeêÂ§ar pelo diagnêÂ³stico mostra onde o seu site estêÂ¡ antes de estudar. E a pêÂ¡gina deixa claro o limite: indexaêÂ§êÂ£o, ranking ou citaêÂ§êÂ£o por IA, o scanner nêÂ£o promete nada disso.',
     'scanner passivo; navegador descartêÂ¡vel; nota geral + quatro notas; atêÂ© 12 correêÂ§êÂµes; relatêÂ³rio JSON; o que exige revisêÂ£o humana',
     'Uma agêÂªncia roda o scan na pêÂ¡gina de contato de um cliente e recebe o bloqueador "sem llms.txt" no topo do plano. Ela corrige, roda de novo e usa as duas notas para mostrar o avanêÂ§o, sem prometer ranking.',
     'Rode o scan em https://webmcp.ARCKHê.pro/ com a pêÂ¡gina principal do seu site e salve o relatêÂ³rio JSON como linha de base.'),
   T('Oito camadas de um site pronto',
     'A pêÂ¡gina organiza a arquitetura em oito camadas, na ordem em que a formaêÂ§êÂ£o constrêÂ³i. As quatro primeiras sêÂ£o o site se descrevendo: descoberta (o agente acha o site?), ferramentas (o que o site sabe fazer?), contrato (como se chama e o que volta?) e estado e erros (e quando dêÂ¡ errado?). As quatro êÂºltimas sêÂ£o o site se protegendo: controle (quem confirma?), permissêÂµes (quem pode chamar?), backend e MCP (onde mora a verdade?) e evals e observabilidade (estêÂ¡ funcionando mesmo?). A regra que atravessa todas: a LLM escolhe a ferramenta; o site decide se ela pode rodar. O diagnêÂ³stico jêÂ¡ mede a camada 1 inteira e os sinais observêÂ¡veis das camadas 2 e 5.',
     'As camadas mostram que expor uma ferramenta êÂ© sêÂ³ o comeêÂ§o. Sem confirmaêÂ§êÂ£o, permissêÂµes e autorizaêÂ§êÂ£o no backend, um agente pode acionar algo que nêÂ£o deveria.',
     'descoberta; ferramentas; contrato; estado e erros; controle; permissêÂµes; backend e MCP; evals',
     'Uma loja expêÂµe a ferramenta de consulta de pedido. A descriêÂ§êÂ£o diz "sêÂ³ consulta", o backend confere se quem chama pode ver aquele pedido, e qualquer alteraêÂ§êÂ£o exige confirmaêÂ§êÂ£o humana. Logs mostram depois se a ferramenta fez o que dizia.',
     'Marque, para o seu site, quais das oito camadas vocêÂª jêÂ¡ cobre e qual pergunta de camada vocêÂª nêÂ£o saberia responder hoje.'),
   T('Seis correêÂ§êÂµes para esta semana',
     'Antes de qualquer fase da formaêÂ§êÂ£o, a pêÂ¡gina traz seis correêÂ§êÂµes que o dono do site faz, cada uma ligada a um item que o scanner verifica. Primeiro, rode o scan e anote as notas como linha de base. Segundo, publique os trêÂªs arquivos pêÂºblicos: robots.txt, sitemap.xml atualizado e um llms.txt que apresenta o site para modelos de IA. Terceiro, arrume o bêÂ¡sico de SEO que o agente tambêÂ©m lêÂª: title, description, canonical, headings em ordem, alt nas imagens, Open Graph e JSON-LD. Quarto, escreva para quem responde perguntas, com respostas diretas, definiêÂ§êÂµes, listas e tabelas; quinto, mostre quem estêÂ¡ por trêÂ¡s, com entidade, autoria, data de atualizaêÂ§êÂ£o e evidêÂªncias. Sexto, escolha como primeira ferramenta um formulêÂ¡rio que nêÂ£o muda nada perigoso, como uma busca ou consulta de status.',
     'SêÂ£o correêÂ§êÂµes que nêÂ£o exigem programar ferramentas e jêÂ¡ sobem as notas. A pêÂ¡gina resume o mêÂ©todo: corrija, rode de novo, veja a nota subir.',
     'linha de base; robots.txt, sitemap.xml, llms.txt; SEO bêÂ¡sico; AEO: respostas diretas; GEO: autoria e evidêÂªncias; primeira ferramenta segura',
     'Um consultor autêÂ´nomo publica o llms.txt, acrescenta data de atualizaêÂ§êÂ£o e autoria nos artigos e cria uma seêÂ§êÂ£o de perguntas frequentes com respostas curtas. Na semana seguinte, as notas de GEO e AEO do scan sobem, sem nenhuma linha de JavaScript nova.',
     'FaêÂ§a hoje a dica 2: confira se seu domêÂ­nio responde em /robots.txt, /sitemap.xml e /llms.txt e anote o que falta.'),
   T('A formaêÂ§êÂ£o e onde continuar',
     'A FormaêÂ§êÂ£o WebMCP tem uma visêÂ£o geral e quatro fases, todas abertas e em portuguêÂªs: Builder (construir), Integrator (integrar), Agent Developer (orquestrar) e Expert (operar). Cada fase tem quatro mêÂ³dulos de seis têÂ³picos e usa JavaScript; quem nêÂ£o programa comeêÂ§a pela visêÂ£o geral e pelo diagnêÂ³stico e leva as fases para o time. As camadas 1 e 2 sêÂ£o ensinadas no Builder, 3 e 4 no Integrator, 5 e 6 no Agent Developer, e 7 e 8 no Expert. Ao lado, a pêÂ¡gina indica o AIV 2026 para AEO e GEO, o curso de Computer Use com o GPT-6 Astra e o Super-Agentes, alêÂ©m de projetos como o Kit do Arquiteto de Agentes, o ARCKHêCCBOT e o os-agentes. O convite final êÂ© direto: o melhor primeiro mêÂ³dulo êÂ© o seu prêÂ³prio site.',
     'Saber em qual fase cada camada êÂ© ensinada permite entrar na formaêÂ§êÂ£o pelo ponto do seu papel, em vez de comeêÂ§ar tudo do zero.',
     'visêÂ£o geral; Builder; Integrator; Agent Developer; Expert; quatro mêÂ³dulos de seis têÂ³picos; cursos ao lado',
     'Uma dona de loja virtual faz o diagnêÂ³stico e a visêÂ£o geral. O desenvolvedor da equipe comeêÂ§a pelo Builder para transformar a busca de produtos em ferramenta declarativa, e a parte de permissêÂµes fica para quando ele chegar ao Agent Developer.',
     'Abra a visêÂ£o geral em https://linnoff88-dev.github.io/ e escolha a fase que corresponde ao seu papel.')],
  ('Prompt: plano WebMCP para o meu site',
   'Leia https://eventos.ARCKHê.pro/webmcp/.\n'
   'Rodei o diagnêÂ³stico em https://webmcp.ARCKHê.pro/ para o meu site: <URL do seu site>.\n'
   'Resultado do scan (cole o JSON ou as notas e bloqueadores): <cole aqui>.\n'
   '1. Explique cada bloqueador em linguagem simples e diga a qual das oito camadas ele pertence.\n'
   '2. Monte a lista desta semana usando as seis correêÂ§êÂµes da pêÂ¡gina, na ordem certa para o meu caso.\n'
   '3. Sugira UMA primeira ferramenta declarativa a partir de um formulêÂ¡rio meu que nêÂ£o muda nada perigoso: nome, descriêÂ§êÂ£o e argumentos.\n'
   '4. Separe o que o scanner consegue provar do que exige revisêÂ£o humana (autorizaêÂ§êÂ£o no backend, idempotêÂªncia, descriêÂ§êÂ£o x efeito real).\n'
   '5. Indique a fase da FormaêÂ§êÂ£o WebMCP por onde eu ou meu time devemos comeêÂ§ar.\n'
   'NêÂ£o prometa ranking, indexaêÂ§êÂ£o ou citaêÂ§êÂ£o por IA.'),
  [('êÂrea WebMCP êÂ· eventos.ARCKHê.pro','https://eventos.ARCKHê.pro/webmcp/'),
   ('WebMCP Readiness','https://webmcp.ARCKHê.pro/'),
   ('FormaêÂ§êÂ£o WebMCP','https://linnoff88-dev.github.io/
   ('WebMCP Builder','https://linnoff88-dev.github.io/
  'webmcp')

FIGURES[(2,2)] = dict(kind='grid',
  caption='As trêÂªs primeiras mudanêÂ§as acontecem com quem visita; as trêÂªs êÂºltimas sêÂ£o a lista de trabalho de quem publica o site.',
  items=['Agente navega','Perguntar','PadrêÂ£o novo','CatêÂ¡logo','Descoberta','SeguranêÂ§a site'])
FIGURES[(2,3)] = dict(kind='columns',
  caption='O Readiness devolve quatro notas independentes: WebMCP mede ferramentas; SEO, GEO e AEO medem se o site êÂ© achado e citado.',
  items=[('WebMCP','ferramentas e schemas'),('SEO','title, canonical'),('GEO','entidade e autoria'),('AEO','respostas diretas')])
FIGURES[(2,4)] = dict(kind='stack',
  caption='As quatro camadas de baixo descrevem o site; as quatro de cima o protegem. Expor ferramenta sem as de cima êÂ© experimento, nêÂ£o operaêÂ§êÂ£o.',
  items=[('Descoberta','o agente acha?'),('Ferramentas','o que faz?'),('Contrato','o que volta?'),('Estado e erros','e se falhar?'),('Controle e permissêÂµes','quem confirma e chama?'),('Backend, MCP, evals','onde mora a verdade?')])
FIGURES[(2,6)] = dict(kind='timeline',
  caption='A formaêÂ§êÂ£o sobe do diagnêÂ³stico êÂ  produêÂ§êÂ£o: cada fase ensina duas das oito camadas.',
  items=[('VisêÂ£o geral','comece aqui'),('Builder','camadas 1-2'),('Integrator','camadas 3-4'),('Agent Dev.','camadas 5-6'),('Expert','camadas 7-8')])
