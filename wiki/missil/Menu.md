[Início](README.md) › O menu /sam

# O menu `/sam`

Digite **`/sam`** (ou `/sam menu`) para abrir o painel. É um baú com um botão para cada tipo de equipamento. Clique num botão para ver a lista dos seus equipamentos daquele tipo e clique em um para abrir a tela dele.

- Quem não é admin vê e gerencia **só o que é seu**.
- Nas listas, os equipamentos mais perto de você aparecem primeiro. Num chunk descarregado (ninguém por perto) aparecem menos detalhes. O silo e a base de drones mostram os números da última visita, e o silo carrega sozinho quando você abre a tela dele.
- De longe (mais de 500 m), abrir e mexer num equipamento precisa de [comunicação pelo satélite](Satelite.md#comunicação-rádio-e-satélite).
- Passe o mouse em cima de qualquer botão: o texto explica o que ele faz e, quando algo não dá, por quê.

Os números amarelos nos desenhos abaixo correspondem à legenda de cada tela.

## Painel

![Painel do /sam](img/menus/painel.svg)

## Radares, rede e lançadores

| Radar | Rede do radar |
|:---:|:---:|
| ![Tela do radar](img/menus/radar.svg) | ![Tela da rede](img/menus/rede.svg) |

| Lançador | |
|:---:|:---:|
| ![Tela do lançador](img/menus/lancador.svg) | Veja [Radar e mísseis SAM](Radar-e-Misseis-SAM.md). |

## Silo

![Tela do silo](img/menus/silo.svg)

Ao clicar em **LANÇAR**, uma tela de confirmação mostra o alvo, a distância e a ogiva. Veja [Silo e Míssil Balístico](Silo-e-Missil-Balistico.md).

## Satélite e Ações no ponto

| Satélite | Ações no ponto |
|:---:|:---:|
| ![Tela do satélite](img/menus/satelite.svg) | ![Tela Ações no ponto](img/menus/acoes-no-ponto.svg) |

Veja [Satélite](Satelite.md).

## Base de Drones e missão

| Base de Drones | Missão (drones → ponto) |
|:---:|:---:|
| ![Tela da Base de Drones](img/menus/base-drones.svg) | ![Tela de missão](img/menus/missao-drone.svg) |

| Drones da base | Um drone |
|:---:|:---:|
| ![Tela Drones da base](img/menus/drones-da-base.svg) | ![Tela de um drone](img/menus/drone.svg) |

A base, os drones da base e a tela de um drone se atualizam sozinhas a cada segundo. Veja [Drones](Drones.md).

## Defesa

Uma lista com os seus CIWS e Bloqueadores de Radar. Cada ícone mostra o estado, a munição (CIWS), o alcance e os abates. **Clique para ligar ou desligar.** Veja [Guerra eletrônica e CIWS](Guerra-Eletronica-e-CIWS.md).

## Alertas

![Tela do Bloco de Ação](img/menus/alerta.svg)

Veja [EMP e alertas da base](EMP-e-Alertas.md).

## Aliados e Comportas

- **Aliados:** quem você confia (os seus radares, drones e CIWS não atacam). Adicione e remova por ali ou com `/sam confiar` e `/sam desconfiar`.
- **Comportas:** a que lançador, silo ou base cada comporta está ligada. Abra e feche para testar.

## Administração (só admins)

O botão **Administração** aparece só para quem tem a permissão `missil.admin`. Veja [Administração](Administracao.md).

---

← [Receitas](Receitas.md) · Próximo: [Besta](Besta.md) →
