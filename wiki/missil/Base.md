[Início](README.md) › Vida, contrabateria e depósito

# Vida, contrabateria e depósito (2.5.0)

## Vida dos equipamentos

Desde a 2.5.0 cada equipamento tem vida e não some mais na primeira explosão.

| Equipamento | Vida |
|---|:---:|
| Silo | 150 |
| Radar, Base de Drones | 100 |
| Lançador, CIWS, Depósito de Munição | 80 |
| Bloqueador de Radar | 60 |
| Mesa de Radar | 50 |
| Sirene, Bloco de Ação, Câmera de Segurança | 30 |

**O que tira vida:**

- **Explosões.** Uma TNT colada no equipamento tira ~50; a 4 blocos, ~18; a partir de 8 blocos, nada.
- **Flechas e tiros** que acertam o bloco: flecha 2 (mais o encantamento Força), tridente 4.
- **Golpes de inimigos.** Um inimigo não consegue quebrar o bloco: cada golpe tira vida conforme a ferramenta (mão 1, madeira 2, pedra 3, ferro 4, diamante 6, netherita 8; com picareta vale 1,5×, com machado 1,25×), no máximo um golpe a cada 0,5 s. Você, os seus aliados e os admins no criativo quebram normalmente.

**Estados:**

| Vida | Estado | O que acontece |
|---|---|---|
| 50% ou mais | intacto | normal |
| abaixo de 50% | danificado | o radar vê só a 70% do alcance, o lançador recarrega 1,5× mais devagar e o CIWS atira 30% menos |
| abaixo de 25% | crítico | cada ação falha 30% das vezes (o silo avisa "o lançamento falhou"), e sai fumaça e faíscas |
| zero | destruído | quebra e solta o item e o que tinha dentro |

**Aviso.** Quando um equipamento seu leva dano, você recebe uma mensagem e as [sirenes e Blocos de Ação](EMP-e-Alertas.md) ganham o alerta **Equipamento atacado** (no máximo um aviso a cada 10 s por equipamento).

**Onde ver a vida:** `/sam info` olhando para o equipamento, as telas e listas do [menu](Menu.md) e a [Mesa de Radar](Mesa-de-Radar.md), onde radar e lançador danificados ganham borda laranja e os críticos, vermelha.

### Kit de Reparo

Clique direito no equipamento com o Kit de Reparo devolve 50 de vida e gasta um kit. Só o dono e os aliados consertam. Receita: [Kit de Reparo](Receitas.md#kit-de-reparo).

---

## Contrabateria

Quando um Míssil Balístico ou de Cruzeiro inimigo vai cair a até 150 m de um equipamento seu, o plugin guarda de onde ele saiu, a **origem**:

- **exata**, se o seu [satélite](Satelite.md) cobre o lugar do lançamento nos primeiros 3 s do voo;
- **estimada**, se só os seus radares acompanharam o míssil. Ela vem com um círculo de erro que começa em 10 m ou 5% da distância (o que for maior) e diminui enquanto o radar acompanha.

Você recebe "**Contrabateria #n**" no chat com o botão **[Retaliar]**, que abre as **Ações no ponto** (as mesmas do mapa do satélite) sobre a origem. A Mesa de Radar e o Terminal de Satélite desenham a origem com um X vermelho e o círculo de erro. `/sam` → **Contrabateria** lista as últimas 10.

**Retaliação automática.** No menu de cada silo há a chave **Retaliação automática** (desligada por padrão). Ligada, o silo lança sozinho na origem, uma vez por origem, desde que tenha míssil, a recarga tenha passado e haja comunicação (rádio ou satélite). Dois lançamentos do mesmo silo inimigo em menos de 30 s contam como a mesma origem.

> **Destruição mútua:** se os dois lados têm silos com retaliação automática, eles trocam tiros até acabar a munição.

---

## Depósito de Munição

Um baú que não se junta com outro baú. A cada 2 s ele leva até 4 itens a cada equipamento:

| Equipamento | O que recebe |
|---|---|
| Lançador SAM | Mísseis SAM, até 9 |
| Silo | o míssil escolhido, a carga da ogiva escolhida e a TNT, até a **TNT desejada** |
| CIWS | Munição de CIWS |
| Base de Drones | drones, flechas e TNT |

- **Quais equipamentos:** os seus a até 48 m e os que você ligar com a [Ferramenta de Link](Comportas-e-Ferramenta-de-Link.md): clique no depósito e depois em cada equipamento (outro clique desliga). Só no mesmo mundo.
- **TNT desejada:** no menu do silo. O depósito não passa disso; sem escolher, vale o máximo do servidor.
- Só funciona com o chunk do depósito e o do equipamento carregados. Uma linha de partículas mostra o caminho do item. O funil continua funcionando como sempre.
- `/sam` → **Depósitos** (ou `/sam depositos`) liga e desliga cada depósito.

Receita: [Depósito de Munição](Receitas.md#depósito-de-munição).

---

← [Ogivas e minas](Ogivas-e-Minas.md) · Próximo: [Câmeras](Cameras.md) →
