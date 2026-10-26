[Início](README.md) › Silo e Míssil Balístico

# Silo e Míssil Balístico

<img src="img/icones/silo.svg" width="48" align="right">

O **Silo de Míssil** lança um **Míssil Balístico** até as coordenadas que você escolher, onde ele explode. A **ogiva** é o que você guarda no silo: **TNT** (quanto mais, maior a explosão) ou uma **[Carga EMP](EMP-e-Alertas.md#ogiva-emp)**, que desliga equipamentos sem quebrar nada. O silo também lança o [Satélite](Satelite.md) e o [Míssil Antissatélite](Satelite.md#derrubar-um-satélite).

## Passo a passo

1. **Coloque o silo** (um barril; ele fica sempre virado para cima). Pode ficar na superfície ou enterrado, com uma [Comporta](Comportas-e-Ferramenta-de-Link.md) em cima.
2. **Abasteça:** clique direito no silo e ponha **Mísseis Balísticos** e **TNT**. Funis (hoppers) também abastecem. O silo só aceita mísseis (Balístico, Antissatélite), o Satélite, TNT, as cargas das ogivas e Chaff. Com um míssil dentro, ele aparece **em pé em cima do barril**, pronto para sair.
3. **Veja o tamanho da explosão:** a cada TNT colocada ou tirada, a barra de ação mostra o raio esperado. Ao fechar o silo, o resumo vai para o chat.
4. **Escolha o alvo** no menu (`/sam` → Silos → o silo): digite as coordenadas no chat, use **a sua posição** ou **o bloco que você está olhando**. Também dá para usar `/sam alvo <x> [y] <z>` olhando para o silo (aceita `~`). Sem Y, o míssil desce no chão daquele ponto.
5. **Lance:** botão **LANÇAR** no menu (pede confirmação) ou `/sam lancar` olhando para o silo. Também dá para lançar das [Ações no ponto](Satelite.md#ações-no-ponto), marcando no mapa.

![Tela do silo](img/menus/silo.svg)

Se o botão LANÇAR estiver cinza, passe o mouse em cima: ele diz o que falta (sem alvo, sem míssil, sem TNT, alvo perto ou longe demais, recarregando...).

## O voo

![Trajeto do Míssil Balístico](img/esquemas/arco-balistico.svg)

- O míssil sobe reto, faz um arco e desce em cima das coordenadas.
- Ele gasta **um míssil** (o de maior alcance) e **a TNT da ogiva**: até 64 TNT por lançamento; o resto fica no silo.
- Se bater em algo no caminho, explode ali mesmo.
- Ele pode ser **derrubado** pelo [foguete da besta](Besta.md), por [SAMs inimigos](Radar-e-Misseis-SAM.md#drones-e-mísseis-inimigos-antidrone-e-antimíssil) e por um [CIWS](Guerra-Eletronica-e-CIWS.md#ciws).
- Um [satélite](Satelite.md#alerta-antecipado) de outro jogador que cubra o silo ou o alvo vê o lançamento e avisa o dono dele.

| Nível do míssil | Alcance padrão |
|:---:|---|
| 1 | 40 a 300 m |
| 2 | 40 a 650 m |
| 3 | 40 a 1000 m (~17 s de voo) |

Cada nível tem a sua [receita](Receitas.md#míssil-balístico): o nível 1 é barato, o 2 pede diamantes e o 3 pede estrela do Nether e netherite. O nível aparece no item como "duração de voo". O alcance de cada nível é do servidor: num mapa grande, o admin pode deixar, por exemplo, 10, 20 e 30 mil blocos.

## O tamanho da explosão (ogiva de TNT)

![A ogiva de TNT](img/esquemas/ogiva-tnt.svg)

| TNT na ogiva | Explosões | Raio da cratera em terra | Em pedra | Dano até |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 (uma TNT normal) | ~4 blocos | ~3 | 8 blocos |
| 8 | 1 | ~9,5 | ~5 | 18 |
| 20 | 1 | ~13,5 | ~7,5 | 32 |
| 32 | 7 | ~16 | ~12,5 | 32 |
| 64 (máximo) | 7 (centro + anel de 6) | **~21** | ~17 | 40 |

- Até 20 TNT é uma explosão só. Com mais, é uma explosão no centro e, logo depois, um anel de explosões em volta, como TNT em cadeia. **64 TNT tiram quase os mesmos blocos que 64 TNT separadas.**
- **A explosão é do dono do silo.** Ela só quebra blocos se a regra `mobGriefing` do mundo estiver ligada (o padrão do Minecraft), esteja o dono online ou não. Desligada, a ogiva só causa dano, e o menu avisa. Plugins de proteção de região conseguem bloquear as explosões.

## Ogiva EMP

Com **Cargas EMP** no silo, clique em **Ogiva** no menu do silo até chegar na EMP (o botão passa por todas as ogivas; o clique direito volta). As outras ogivas (perfurante, incendiária, fumaça e múltipla) estão em [Ogivas e minas](Ogivas-e-Minas.md). O lançamento gasta um míssil e uma carga; a TNT fica guardada. O míssil voa igual, mas na chegada não quebra nada: desliga por 60 s os equipamentos a até 64 m. Veja [Ogiva EMP](EMP-e-Alertas.md#ogiva-emp).

## Míssil de Cruzeiro

O **Míssil de Cruzeiro** também sai do silo, com a mesma ogiva, mas voa **baixo**, acompanhando o relevo, em vez do arco alto.

1. Ponha **Mísseis de Cruzeiro** no silo. Com balísticos e de cruzeiro dentro, o botão **Míssil** do menu escolhe qual sai.
2. Opcional: até **5 pontos de passagem**. Com a [Ferramenta de Link](Comportas-e-Ferramenta-de-Link.md#ferramenta-de-link), clique no silo e depois nos blocos por onde ele deve passar (Shift + clique tira o último). Use os pontos para contornar radares e morros.
3. Escolha o alvo e lance como o balístico.

- Ele sai do poço, desce até **6 m acima do chão** e voa a ~35 m/s. Olha o terreno até 90 m à frente: sobe cedo antes de morros, árvores e prédios e desce do outro lado. Se o silo está num vale, ele sobe até sair dele antes de virar.
- A 90 m do alvo, sobe 20 m e **mergulha** nele.
- O alcance é o **comprimento da rota** (silo → pontos → alvo): 400, 800 e 1200 m para os níveis 1, 2 e 3.
- **É difícil de ver:** o radar só o vê com linha de visada (um morro no meio esconde) e, com ele voando baixo, só a até metade do alcance. O satélite vê de onde ele saiu, mas não para onde vai.
- O CIWS, os mísseis SAM e a besta derrubam o cruzeiro como os outros mísseis.
- No Nether, ele voa entre o chão e o teto. A Ogiva Múltipla é só do balístico.

## Lançar de longe

- **Dá para lançar de longe.** Abrir o silo no menu carrega o chunk dele e o das comportas e mostra o que tem dentro. Se ninguém estiver perto, o lançamento carrega o silo sozinho antes de soltar o míssil.
- Antes de soltar o míssil, o plugin carrega **o caminho inteiro e a área do alvo**. Por isso o míssil não "some" no meio do caminho nem chega num lugar descarregado, mesmo com todos os jogadores longe.
- Mais longe que 500 m você precisa de **comunicação**: um [satélite](Satelite.md) cobrindo você e o silo.

## Regras

- O silo precisa ser seu (admins lançam de qualquer um) e você precisa da permissão `missil.balistico` (todo mundo tem, a não ser que o admin tire).
- Entre dois lançamentos do mesmo silo há uma **recarga de 10 s**.
- O admin pode desligar os balísticos no servidor inteiro.

---

← [Mesa de Radar](Mesa-de-Radar.md) · Próximo: [Comportas e Ferramenta de Link](Comportas-e-Ferramenta-de-Link.md) →
