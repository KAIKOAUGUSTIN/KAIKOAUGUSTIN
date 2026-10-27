[Início](README.md) › Ogivas e minas

# Ogivas e minas (2.4.0)

## Escolher a ogiva no silo

No menu do [silo](Silo-e-Missil-Balistico.md), o botão **Ogiva** passa pelas seis ogivas: um clique vai para a próxima e o clique direito volta para a anterior. O botão mostra o que a ogiva faz e quantas cargas dela há no silo. Cada ogiva, menos a de TNT, gasta o seu item; a TNT, quando a ogiva usa, é a TNT guardada no silo.

| Ogiva | Gasta | O que faz |
|---|---|---|
| **TNT** | a TNT do silo | a explosão de sempre: mais TNT, explosão maior |
| **EMP** | 1 Carga EMP | não quebra nada: desliga os equipamentos perto por 60 s ([EMP](EMP-e-Alertas.md#ogiva-emp)) |
| **Perfurante** | 1 Ponta Perfurante + a TNT | entra no chão antes de explodir |
| **Incendiária** | 1 Carga Incendiária + a TNT | explosão menor e fogo em volta |
| **Fumaça** | 1 Carga de Fumaça | não explode: deixa uma nuvem de fumaça |
| **Múltipla** | 1 Ogiva Múltipla + a TNT | o míssil se divide em várias ogivas em volta do alvo |

As receitas das cargas estão em [Receitas](Receitas.md#ogivas-e-minas-240).

### Perfurante

O míssil não explode na superfície: ele entra no chão e a TNT explode lá embaixo. Serve contra bases enterradas.

- Entra **8 blocos**, mais **2 por nível** do míssil (nível 3: 14 blocos).
- **Obsidiana** (e blocos tão duros quanto ela) conta como **3 blocos**. A **bedrock** para a ponta.
- Cavernas no caminho não gastam nada.
- Pequenas explosões abrem o túnel no caminho.

### Incendiária

A TNT explode com **metade da força** e, logo depois, o chão em volta pega fogo (6 blocos, mais um pouco por TNT, até 16). Quem estiver perto pega fogo também.

- Só põe fogo nos blocos onde as explosões podem quebrar blocos (a regra `mobGriefing` do mundo e o config do servidor). Senão, só as criaturas pegam fogo.
- O fogo que ela põe some sozinho em 15 s.

### Fumaça

Não explode e não fere ninguém. No lugar do impacto fica uma **nuvem de 20 m por 60 s**.

- A nuvem **tapa a visão**: a trava e o buscador da [besta](Besta.md), a câmera do [kamikaze](Drones.md) e os sensores dos drones (reconhecimento e patrulha) não veem através dela.
- Quem está dentro fica cego aos poucos.
- O **radar continua vendo**: contra o radar, use o [chaff](Guerra-Eletronica-e-CIWS.md).
- A TNT fica guardada no silo.

### Múltipla

Só vai no **Míssil Balístico**. Uns 3 s antes de chegar, o míssil se divide em **4 ogivas**, que caem num **anel de 15 m** em volta do alvo. A TNT do silo é dividida entre elas.

- Cada **Chaff** no silo (até 3) vira um **chamariz**: cai junto e parece uma ogiva no radar, mas não explode.
- Para o inimigo, cada ogiva é um míssil: a rede de radares dele precisa de um SAM para cada uma.
- Se o míssil bater em algo antes de se dividir, a TNT inteira explode ali.

## Granada de Fumaça

Clique direito arremessa a granada. Onde ela cair, sai uma **nuvem de 6 m por 20 s**, com as mesmas regras da ogiva de fumaça. Serve para fugir de quem está te travando com a besta ou para cegar a câmera de um drone.

## Minas

Clique direito com a mina coloca ela no mundo. Ela **arma 3 s depois**.

| Mina | Onde vai | O que faz |
|---|---|---|
| **Terrestre** | em cima de um bloco sólido | um inimigo a pé ou num veículo passa por cima, ela estala e explode logo depois. Não quebra blocos |
| **Antidrone** | em cima de um bloco sólido | derruba o primeiro drone ou kamikaze inimigo que passar a até 8 m. Serve uma vez só |
| **Naval** | na superfície da água | boia e explode com barcos e nadadores inimigos a até 2 m |

**Quem aciona.** Só inimigos: você, os seus aliados e quem é do mesmo time não acionam as suas minas. Mobs não acionam (a não ser que o admin ligue).

**Ver as minas.** A terrestre é quase rente ao chão e tem a cor do bloco de baixo. Só você e os aliados veem a **marca** das suas minas, segurando uma mina ou a Ferramenta de Link: vermelha (terrestre), azul-clara (antidrone) ou azul (naval); cinza enquanto ainda arma. Um [drone de reconhecimento](Drones.md) seu **revela** por 1 minuto as minas inimigas que vê (marca laranja).

**Desarmar.** Agachado, com uma **tesoura** na mão, perto da mina (até 2,5 m): um inimigo desarma em **3 s** e leva a mina. O dono e os aliados fazem o mesmo para recolher, em 1 s. O dono é avisado quando desarmam uma mina dele.

**Em cadeia.** Uma explosão perto (até 6 m) dispara as minas terrestres e navais em volta.

**Alerta.** A [Sirene e o Bloco de Ação](EMP-e-Alertas.md) têm o alerta **Mina acionada**: uma mina sua a até o raio deles foi acionada. Você também recebe uma mensagem.

**Menu.** `/sam` → **Minas** lista as suas minas, da mais perto para a mais longe. Clicar numa tira a mina do mundo e devolve o item. Cada jogador pode ter até 50 minas.

---

← [EMP e alertas da base](EMP-e-Alertas.md) · Próximo: [Vida, contrabateria e depósito](Base.md) →
