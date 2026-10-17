# O que os bots fazem

## Combate

- **Corpo a corpo:** espada com recarga de arma, críticos e escudo, como um jogador.
- **Mira dos projéteis:** com arco, besta e tridente, o bot calcula o ângulo pela física real do projétil e antecipa o alvo pelo tempo de voo.
- **Rajada de arco** (fase 4+, `taticas.pressao-de-arco`): quando o bot fica muito tempo sem acertar, ele atira uma rajada de flechas.
  - Ele puxa o arco o quanto precisa e só atira se a flecha alcança o jogador sem bater em bloco.
  - De cima de um morro, a flecha vai bem mais longe.
- **Besta com fogos** (`taticas.besta-com-fogos`, desligada por padrão): o foguete voa uns 64 blocos.
  - O bot só atira se o foguete chega ao jogador antes de explodir e sem bloco no caminho.
  - Com a besta carregada, ele espera até 1 s o jogador entrar no alcance. Se não entrar, desiste sem atirar.
- **Lança a cavalo** (fase 4+): montado, o bot faz a carga do jogo contra o alvo com a lança da fase.
  - O dano vem da velocidade do cavalo, e a carga a galope derruba quem estiver montado.
  - O bot passa pelo alvo, dá a volta e carrega de novo.
  - Depois de 3 passadas sem acertar, ele desce e luta de espada.
- **Sobrevivência:** o bot come quando tem fome. Em combate come maçã dourada (fase 5+). Apaga o fogo com balde de água (fase 3+).
- **Agressividade** (0 a 10, no `/manhunt create` ou no menu):
  - aumenta o número de flechas da rajada de arco, de 2 a 6;
  - aumenta a chance da emboscada de TNT e da besta com fogos, quando essas táticas estão ligadas.

## Mobilidade

- **Caminho:** o bot calcula o caminho com A* fora da thread principal. Sem caminho, ele anda direto para o alvo.
- **Torres e pontes:** perto do alvo, até 3 blocos na horizontal, o bot constrói torres e pontes para chegar até você.
- **Cavar:** o bot quebra os blocos que estão no caminho.
- **Pérolas do End:** por padrão, só no Nether (`mobilidade.dimensao-perolas`).
- **Cavalo** (fase 4+): o cavalo vira para onde o bot olha, galopa, pula obstáculos e vãos e boia na água.
- **Barco:** o bot persegue quem está de barco ou nadando. Quando atravessar um lago de barco é mais rápido que dar a volta a pé, ele coloca o barco na beira, rema até a outra margem e quebra o barco ao descer.
- **Elytra** (desligada por padrão): para alcançar alvos longe.
- **Outras dimensões:** os bots seguem você para o Nether e o End, entre 30 s e 60 s depois de você. Eles chegam saindo de um portal que você vê.
- **Longe dos jogadores:** os bots continuam se movendo, porque o plugin mantém os chunks em volta deles carregados.

## Táticas

- **Redistribuição:** um bot a mais de 200 blocos do alvo reaparece escondido perto dele.
- **Mortes silenciosas:** o bot mais longe de cada jogador (200+ blocos) some e renasce mais perto.
- **Emboscada em caverna:** quando você está numa caverna (abaixo de Y 60, sem luz do céu), um bot que te persegue vai para um ponto escondido da mesma caverna, a 50–130 blocos, e coloca uma cama vermelha.
  - Enquanto a cama existir e você continuar na caverna, o bot renasce ao lado dela.
  - Se você sair da caverna ou quebrar a cama, a emboscada acaba e os bots da caverna morrem.
- **Capacidades automáticas** (desligadas por padrão): emboscada de TNT e besta com fogos sem comando.
  - Para testar uma capacidade contra você: `/manhunt test <tnt-craft|bow-burst|firework-crossbow>`.

## Parecer jogador

- **TAB:** os bots aparecem na lista do TAB com skin e ping.
- **Contagem de jogadores:** eles contam no número de jogadores da lista de servidores e no `/list`.
- **Mensagens:** o servidor mostra "entrou/saiu do jogo" e as mensagens de morte do jogo para os bots.
- **Mobs:** os mobs hostis atacam os bots como atacam jogadores. Os piglins ignoram bot com ouro, e você pode criar uma lista de exceções.
- **Skin:** pela conta Mojang do nome, por um `.png` em `plugins/ManhuntStar/skins/` ou a skin de robô padrão. Para trocar, use `/manhunt skin <bot> <jogador>`.
- **Humanização** (`combate.humanizacao`, de 0 a 1): o bot erra a mira, perde golpes e bate num ritmo irregular, como uma pessoa.

---

← [Dificuldades e fases](Dificuldades-e-Fases.md) · Próximo: [Grupos](Grupos.md) →
