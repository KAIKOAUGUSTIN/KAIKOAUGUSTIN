[Início](README.md) › Perguntas frequentes

# Perguntas frequentes

Primeiro passo para quase tudo: **olhe para o equipamento e digite `/sam info`**, ou abra a tela dele no [menu](Menu.md) e passe o mouse nos botões. Eles dizem o que está faltando.

## Radar e mísseis SAM

**Meu radar não atira. O que pode ser?**

Confira, nesta ordem:

1. **Modo do radar:** no padrão (**Aéreo**) ele só ataca quem voa de elytra ou em montaria voadora. Para quem anda, troque para Terrestre ou Os dois (`/sam modo ambos`).
2. **O alvo é você, um aliado ou alguém do seu time?** Esses nunca são atacados (a não ser você, com "Atacar o dono" ligado).
3. **Tem lançador conectado?** O lançador precisa estar a até 64 m de um radar da rede. `/sam info` no radar mostra quantos lançadores ele tem.
4. **Tem Mísseis SAM no lançador?** E ele está fora da recarga?
5. **O alvo está entre 8 e 180 m do lançador?** No chão, a menos de 20 m não vale.
6. **Linha de visada:** o radar enxerga 200 m, mas morros e construções escondem o alvo.
7. **Alguém atrapalhando?** Chaff, Bloqueador Portátil, Bloqueador de Radar inimigo ou um EMP (`/sam info` mostra "desligado por EMP").
8. **O admin desligou o ataque no chão?** Aí os radares não atacam ninguém no chão.
9. **O alvo está no modo criativo ou espectador?** O radar só vê quem está em sobrevivência ou aventura.

**O lançador diz que não tem radar.** Ele precisa estar a até 64 m de um radar seu. Use `/sam` → Lançadores → o lançador → **Conectar ao radar mais perto**, ou a [Ferramenta de Link](Comportas-e-Ferramenta-de-Link.md#ferramenta-de-link).

**Dois radares meus não estão na mesma rede.** Sozinhos, eles só se juntam a até 300 m. Mais longe, ligue à mão (até 1000 m) com a Ferramenta de Link ou com **Juntar todos os meus radares** no menu da rede.

**O míssil SAM explodiu sozinho no ar.** A rede perdeu o alvo (atrás de um morro, longe demais, chaff, bloqueador...) e o míssil se autodestruiu 3 s depois.

## Comunicação e satélite

**"Sem comunicação" no menu.** Você está a mais de 500 m do equipamento e não há satélite (seu ou de um aliado que confia em você) cobrindo **você e o equipamento**. Chegue mais perto ou lance um [satélite](Satelite.md).

**Não consigo lançar o satélite.** O silo precisa ter um Satélite dentro, você só pode ter um satélite, e o mundo não pode ter teto (o Nether não serve). O admin também pode ter desligado os satélites.

**O Terminal está vazio ou diz "Sem satélite".** Você precisa estar dentro da cobertura do seu satélite (ou do de um aliado). O relevo vai aparecendo conforme os chunks carregam.

## Silo

**O LANÇAR está cinza.** Passe o mouse em cima: ele diz o motivo. Os mais comuns:

- **sem alvo:** escolha as coordenadas;
- **sem míssil** ou **sem TNT** (com a ogiva de TNT) ou **sem Carga EMP** (com a ogiva EMP);
- **alvo perto demais:** o mínimo é 40 m;
- **alvo longe demais:** 300, 650 ou 1000 m no padrão, conforme o nível (a duração de voo) do míssil;
- **recarregando:** 10 s entre dois lançamentos;
- **desligado por EMP**, ou os balísticos (ou o EMP) desligados pelo admin.

**A explosão não quebrou nenhum bloco.** O mundo está com `mobGriefing` desligado, ou um plugin de proteção de região bloqueou. Fale com o admin.

**O míssil sumiu no caminho.** Ele pode ter sido abatido (o chat avisa: "Seu míssil balístico foi abatido"), ou batido em algo antes de chegar.

## Mesa de Radar

**Não consigo colocar a mesa.** Os 3x3 blocos à frente dela (no mesmo nível) precisam estar livres e ter chão firme embaixo. A frente é para onde você está olhando ao colocar.

**A mesa não mostra a minha rede.** Ela usa o seu radar mais perto, a até 128 m dela.

**O mapa está girado.** O topo do mapa aponta para a frente da mesa. Se ainda assim parecer errado, o admin pode ajustar `monitor.rotacao`.

## Drones

**Os drones de patrulha não saem.**

- A patrulha está ligada no menu da base?
- Tem **flechas** na base?
- Tem alguém a até 256 m da base ou da rota? Sem gente por perto eles ficam guardados.
- O céu em cima da base está livre (ou tem uma comporta)?
- O drone está carregando? Depois de pousar, ele carrega o que falta da bateria (até 20 s) e só sai cheio. O menu da base mostra quanto falta.
- Um EMP pegou a base, ou o admin desligou os drones?

**O kamikaze não sai.** Precisa ter um Drone Kamikaze **e TNT** na base, o alvo precisa estar a até 1200 m dela e você precisa de comunicação.

**Meu drone caiu e o item sumiu.** Drone derrubado se perde. O chat diz quem derrubou.

**Como vejo a bateria dos drones?** No menu da base, ou em **Drones da base**: cada drone no ar mostra a bateria e o tempo de voo, e cada um carregando mostra quanto falta. Veja [Drones da base](Drones.md#drones-da-base).

**A patrulha atira nos meus animais?** Não. Animais vêm desligados, e os domesticados por você ou pelos aliados nunca são alvo. Mobs com etiqueta de nome também ficam em paz. Veja [Alvos da patrulha](Drones.md#alvos-da-patrulha).

**A patrulha não atira nos zumbis.** Confira **Atirar em monstros** no menu da base. Ela só voa com alguém a até 256 m da base ou da rota, e precisa de flechas.

**Posso pôr flechas com poção ou espectrais na base?** Pode. O drone atira cada uma com o seu efeito, na ordem dos slots da base. Veja [Patrulha](Drones.md#patrulha).

**Como vejo pela câmera do drone?** Menu da base → **Drones da base** → clique no drone → **Ver câmera**. Shift sai.

## Defesa e alertas

**O CIWS não atira.** Tem Munição de CIWS dentro? Ele está ligado em `/sam defesa`? O alvo está a até 48 m e é inimigo? Lembre: ele nunca atira em quem está a pé.

**A sirene não toca.**

- O alerta está marcado (verde) na tela dela, e está dentro do raio?
- Mísseis e drones seus ou de aliados não contam.
- "Inimigo no radar" precisa que a sua rede de radares esteja vendo o inimigo.
- A sirene está ligada? O admin não desligou os alertas?
- Use **Testar** na tela dela para ouvir.

**O Bloco de Ação não liga a minha porta.** Ele precisa estar **encostado** na porta (ou ligado por redstone). No modo **pulso** ele fica ligado só 1 s.

## Itens

**Não consigo usar um item do plugin numa receita.** Itens do plugin só entram onde a receita pede aquele item: o [Combustível de Foguete](Receitas.md#combustível-de-foguete) e o [Circuito de Guiagem](Receitas.md#circuito-de-guiagem). Fora disso, não servem de ingrediente. O Míssil SAM, por exemplo, não entra em nenhuma receita.

**Não consigo fazer o míssil (ou o satélite, o radar...).** Confira três coisas:

- **Componentes:** os mísseis pedem [Combustível de Foguete](Receitas.md#combustível-de-foguete) e quase tudo pede [Circuito de Guiagem](Receitas.md#circuito-de-guiagem). Um fragmento de eco comum não substitui nenhum dos dois.
- **A receita certa:** o Míssil Balístico tem uma receita por nível, e o foguete de fogos não entra mais nele.
- **As receitas do seu servidor:** o admin pode ter mudado alguma. O livro de receitas do jogo mostra as que valem.

**O Foguete Teleguiado não dá impulso na elytra.** É de propósito: ele só funciona na besta.

**Quebrei um equipamento. Perdi?** Não: quebrar devolve o item do plugin e o que estava guardado dentro (no modo criativo nada cai).

---

← [Administração](Administracao.md) · [Início](README.md)
