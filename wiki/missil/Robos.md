[Início](README.md) › Robôs

# Robôs (3.0.0)

Quatro robôs que trabalham sozinhos e moram numa **Estação de Robôs**. Cada um parece um jogador com a skin de robô; em cima dele aparece o nome e, embaixo, o que ele está fazendo e a bateria ("⛏ minerando · ⚡ 64%").

| Robô | O que faz |
|---|---|
| **Defesa** | guarda a estação, um ponto, uma rota ou você, e ataca os inimigos |
| **Minerador** | desce em escada e minera sozinho até o objetivo |
| **Explorador** | explora, acha estruturas e saqueia os baús delas |
| **Trabalhador** | leva itens entre baús, limpa áreas, conserta equipamentos, reabastece e resgata robôs |

Receitas: [Robôs](Receitas.md#robôs-300).

---

## A estação

1. Coloque a **Estação de Robôs** (uma mesa de ferraria).
2. Clique direito nela **com um robô na mão**: ele fica guardado.
3. Clique direito nela **sem robô**: abre o menu da estação.

No menu da estação:

- **os robôs dela**, com o estado, a vida, a bateria, a tarefa e o último relatório (clique para abrir o robô);
- **Suprimentos**: ponha ferramentas, armas, armadura, tochas, pedregulho, Kits de Reparo e Baterias Reserva. Antes de sair, cada robô pega o que o tipo dele usa;
- **Carga**: o que os robôs trazem. O que não cabe vai para o **Depósito de Munição ligado** (clique no botão e depois no depósito com a Ferramenta de Link).

Guardado, o robô **carrega a bateria** (cheia em 5 minutos) e recupera a vida devagar. Com menos de metade da vida, a estação gasta um Kit de Reparo dos suprimentos nele.

## Cada robô

Abra pelo menu da estação, por `/sam robos` ou clicando direito no robô:

- **Enviar** (sai da estação e faz a tarefa) ou **Chamar de volta**;
- **Ver pela câmera** (agachar sai);
- **Tarefa**: o que ele faz (veja cada robô abaixo);
- **Equipamento e mochila**: com ele na estação, dá para trocar o que ele leva;
- **Renomear** e **Pegar como item** (o item guarda o robô inteiro, com equipamento, mochila e tarefa).

Com a **Ferramenta de Link**, clicar num robô faz dele a fonte da próxima [Tela de Câmera](Cameras.md#tela-de-câmera).

---

## Regras de todos

- **Sem raio-X.** O robô só sabe do que viu: raios saem dos olhos dele o tempo todo, e o que eles tocam (e o que aparece quando ele cava) entra na memória. Ele não sabe de caverna, lava ou minério escondido atrás da pedra.
- **Bateria.** Ele não volta com 20%: sabe quanto gasta para voltar pelo caminho que fez e volta com só um pouco a mais (se a volta custa 2%, trabalha até uns 3,5%). Também volta com a vida em 40%, a mochila cheia ou a picareta quase quebrando (se a estação tiver outra). Depois de descarregar e carregar, ele **volta para a tarefa**.
- **Sem bateria** (perdeu vida, ficou preso): desliga onde está e você recebe as coordenadas. Uma **Bateria Reserva** (clique direito nele) ou um Robô Trabalhador religa ele ali.
- **Quebrar blocos.** O robô quebra como se fosse você: se a proteção do servidor não deixa você quebrar ali, ele também não quebra (e desvia). Com você offline, as tarefas que quebram blocos esperam você voltar. Ele nunca quebra equipamento do Míssil.
- **Dano.** Inimigos, mobs, explosões e mísseis ferem os robôs; você e os seus aliados não. Todo robô revida e foge para a estação se estiver perdendo; os de defesa correm para ajudar. As sirenes ganham os alertas **Robô atacado** e **Robô destruído**.
- **Destruído**, ele deixa cair a mochila, o equipamento e **Sucata de Robô**.
- **Preso** por um minuto, tenta cavar para sair e depois avisa você.
- **De longe** (mais de 500 m) só dá ordem com [satélite](Satelite.md); dentro de um bloqueador inimigo ele fica sem sinal (continua a tarefa, mas não aceita ordem nem câmera); o EMP desliga o robô por 60 s.
- **Servidor desligando:** os robôs fora voltam para a estação com a mochila e retomam a tarefa quando ele liga.
- **Andar e ir longe (3.1.0).** O robô anda sem parar a cada passo (segue o caminho enquanto calcula o próximo trecho), corta caminho quando a reta está livre e corre em reta. Para voltar de longe, ele refaz **o próprio caminho de trás para a frente**, que sempre passa. Os chunks à frente ficam carregados enquanto ele anda. Se mesmo assim ele não achar caminho, avisa você com as coordenadas antes de a bateria acabar.
- **Tudo volta para a estação (3.1.0).** Ao chegar, o robô entrega o equipamento (vai para os **Suprimentos**) e a mochila (vai para a **Carga**). Ele fica guardado sem nada e pega o que precisa ao sair de novo.
- Cada jogador pode ter até **5 robôs no mundo** ao mesmo tempo.
- A [Mesa de Radar](Mesa-de-Radar.md) e o Terminal mostram os seus robôs (quadrado azul-claro) e as estruturas que os exploradores acharam (losango roxo).

---

## Robô de Defesa

- **Modos:** guardar a estação (raio), guardar um ponto (clique num bloco com a Ferramenta de Link), patrulhar uma rota (clique nos blocos da rota; no ar termina) ou **seguir você**.
- **Alvos:** jogadores inimigos, monstros e animais, cada um com sua chave. Endermen, só se atacarem.
- **Quem ele escolhe (3.1.0):** só quem ele **vê** e consegue alcançar (um mob enterrado ou atrás da parede não conta, a não ser que tenha atacado). Primeiro quem atacou você, um robô ou um equipamento; depois jogadores inimigos; monstros atacando alguém; os outros monstros; animais. Nenhum mob tem prioridade especial, e entre iguais vai no mais perto dele. Ele não fica trocando de alvo.
- **Luta certa para cada mob (3.1.0, todos os robôs):** creeper — bate e se afasta, e foge quando ele acende (com arco, atira de longe); esqueleto e outros que atiram — chega perto em zigue-zague de escudo; aranha — espera o pulo de escudo; enderman — não olha para a cabeça; bruxa — chega rápido; slime — se afasta dos pedaços; jogador — golpe crítico e escudo.
- Um inimigo no chão que a sua [rede de radares](Radar-e-Misseis-SAM.md) vê perto da estação chama os robôs de defesa.

## Robô Minerador

- **Até quando:** sem parar, até ter um tanto de um item (por exemplo 64 diamantes), até um tanto de pilhas, ou por um tempo.
- **Minério:** escolha qual. Ele desce **em escada** (nunca reto para baixo) até a melhor altura daquele minério naquela dimensão: diamante perto de Y −59, ferro em 16, ouro em −16, detrito antigo em 15 no Nether, quartzo em 40.
- **Como acha o minério, sozinho:** abre **túnel em galhos**, **segue cavernas** que viu ou **segue um veio** que apareceu, e troca de jeito conforme rende mais.
- **Sempre de olho (3.1.0):** em qualquer momento (até descendo a escada), um minério que ele vê por perto é minerado na hora, e ele volta para onde estava.
- **Cuidados:** tampa a lava que aparece, não pisa em lava, quebra o bloco embaixo do cascalho e da areia **sem eles caírem**, não aceita queda de mais de 3 blocos, põe tocha no escuro e evita água funda.
- **O que guarda:** só minérios e valiosos (padrão), tudo menos pedra, terra e cascalho, ou tudo.
- **Ao chegar** à estação, descarrega e manda um relatório, por exemplo "23 raw iron, 4 diamond, 2 baús, 2 lutas". Depois **volta ao ponto onde parou**.
- Os baús de estrutura que ele achar cavando são saqueados (veja abaixo).

## Robô Explorador

- **Explora** o que ainda não viu, numa direção (ou qualquer uma) e até um raio da estação, fazendo ponte com o pedregulho que leva. Pode ir para o **Nether** por um portal.
- **Reconhece estruturas pelo que vê**: gerador de monstros e pedregulho com musgo (masmorra), trilhos e cercas (mina abandonada), tijolos do Nether (fortaleza), pedra-negra polida com ouro (bastião), purpúreo (cidade do Fim), moldura do portal do Fim, deepslate com sculk (cidade antiga), templos e vilas. Marca no mapa, entra e procura os baús.
- **Objetivo:** explorar sem parar, até achar um tipo de estrutura, ou até saquear os itens escolhidos.
- **O que leva dos baús:** "valiosos" (padrão) ou os itens que você escolher (clique esquerdo no botão com o item na mão).

## Regras de saque (minerador e explorador)

- Só baús **de estrutura** (e barris e carrinhos com baú da mina abandonada). **Nunca** um baú colocado por jogador, e só se você mesmo pudesse abrir.
- Se ninguém abriu o baú, o robô gera o saque como você abrindo.
- Ele leva só os itens escolhidos; o resto fica no baú.

## Robô Trabalhador

Monte a **fila de tarefas** no menu dele (clique esquerdo numa tarefa abre ela: equipe e subir; direito tira). Os pontos e cantos vão com a Ferramenta de Link ou com **[Usar minha posição]** no chat.

1. **Levar itens:** clique no baú A e depois no baú B com a Ferramenta de Link. O filtro é o item na sua mão (sem nada, leva tudo). Com **Repetir** ligado, ele fica levando sempre: é a logística entre bases, até em outra dimensão (ele atravessa o portal do Nether). Desde a 3.1.0 ele leva tudo numa **carga separada** e entrega **tudo** em B: não fica com ferramenta nem armadura de ninguém.
2. **Limpar área:** clique nos dois cantos (**sem limite de tamanho** desde a 3.1.0). Ele limpa de cima para baixo, junta os drops e pula baús e equipamentos.
3. **Consertar equipamentos:** usa os Kits de Reparo da estação nos seus equipamentos danificados perto dela.
4. **Reabastecer:** clique num Depósito de Munição e depois num equipamento longe dele: o robô leva a munição.
5. **Resgatar:** escolha um robô seu sem bateria; ele vai lá pelo caminho que o outro fez e religa com uma Bateria Reserva. Vai um robô só.
6. **Obras (3.1.0)**, bloco por bloco, como um construtor, com o bloco que você pôs nos **Suprimentos** da estação (quando acaba, ele busca mais e continua):
   - **Construir muro:** duas pontas e a altura. A altura conta a partir do chão de cada coluna (o muro acompanha o relevo), a base desce até o chão firme, e **na água** ele começa no fundo e sobe a altura acima do nível da água. Espessura de 1 a 3.
   - **Construir caixa:** dois cantos: paredes, piso e teto.
   - **Preencher área:** enche o que é ar ou água.
   - **Trocar blocos:** tira um bloco (mão secundária) e põe outro (mão principal).

   O bloco é o que está na sua mão quando você clica no botão.

### Equipes (3.1.0)

Vários trabalhadores da mesma estação podem fazer **a mesma tarefa**: clique na tarefa e marque os robôs da **Equipe**. Ela é dividida em **partes iguais** — a área e o muro em faixas do mesmo tamanho, a quantidade de itens em partes iguais (90 com 3 robôs = 30 cada), os equipamentos a consertar divididos. Se um sai no meio, o que faltava dele é repartido por igual entre os outros; se um termina antes, o que falta é repartido de novo contando com ele. **Resgatar** e **reabastecer** são de um robô só.

---

## Nas três dimensões

A estação e os robôs funcionam no Mundo normal, no Nether e no Fim.

- **Nether:** cuidado com lava, magma e fogo das almas; ele sai da linha de tiro dos gasts; com uma peça de **ouro** nos suprimentos, os piglins ficam neutros.
- **Fim:** ele nunca pisa onde não há chão embaixo.
- **Portais:** nas tarefas que precisam, ele atravessa um **portal do Nether** que conhece (ou um perto da estação); do outro lado usa um portal perto do ponto equivalente, ou constrói um. O portal do Fim ele não usa.

---

← [Câmeras](Cameras.md) · Próximo: [Comandos e permissões](Comandos-e-Permissoes.md) →
