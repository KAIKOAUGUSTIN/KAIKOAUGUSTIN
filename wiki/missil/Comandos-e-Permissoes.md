[Início](README.md) › Comandos e permissões

# Comandos e permissões

Todos os comandos começam com **`/sam`** (também funciona `/missil`). Os que dizem "olhando para" valem para o bloco na sua mira, a até 8 blocos.

## Para todo mundo

| Comando | O que faz |
|---|---|
| `/sam` ou `/sam menu` | Abre o [menu](Menu.md). |
| `/sam ajuda` | Lista os comandos no chat. |
| `/sam info` | Estado do equipamento que você está olhando: radar, lançador, silo, comporta, mesa, base de drones, CIWS, bloqueador, sirene ou bloco de ação (e se um EMP o desligou). |
| `/sam modo aereo` / `terrestre` / `ambos` | Que alvos o radar olhado ataca. |
| `/sam alvo-dono on` / `off` | O radar olhado também ataca o dono (para testar). |
| `/sam rede` | Abre o menu da rede do radar olhado. |
| `/sam rede juntar-todos` | Liga numa rede todos os seus radares do mundo. |
| `/sam rede lancadores` | Conecta à rede do radar olhado os seus lançadores livres por perto. |
| `/sam rede sair` | Tira o radar olhado da rede. |
| `/sam alvo <x> [y] <z>` | Coordenadas do alvo do silo olhado. Aceita `~` (a sua posição). Sem Y, o míssil desce no chão. |
| `/sam lancar` | Lança o míssil do silo olhado. Precisa da permissão `missil.balistico`. |
| `/sam satelite` | Menu do seu satélite: mover, marcar um ponto, jogadores na área, alertas. |
| `/sam drones` | Suas Bases de Drones (olhando para uma base, abre ela). |
| `/sam defesa` | Seus CIWS e Bloqueadores de Radar (liga e desliga). |
| `/sam alertas` | Suas Sirenes e Blocos de Ação (olhando para um, abre ele). |
| `/sam confiar <jogador>` | Torna o jogador seu aliado. |
| `/sam desconfiar <jogador>` | Tira o jogador dos aliados. |
| `/sam aliados` | Lista os seus aliados. |
| `/sam fabricar` | Abre a tela [Fabricar](Menu.md#fabricar): faz os itens do plugin com o que está no inventário. |
| `/sam bedrock` | Diz se você está sendo tratado como jogador [Bedrock](Bedrock.md) e como o servidor reconheceu. |

## Aliados

- `/sam confiar <jogador>` faz os **seus** radares, drones de patrulha e CIWS pararem de atacar esse jogador e os equipamentos dele. Os alertas da sua base também ignoram os mísseis e drones dele.
- **Vale num sentido só.** Para os equipamentos dele não atacarem você, ele precisa usar `/sam confiar` com o seu nome.
- Um aliado que confia em você também empresta o satélite: você pode usar a cobertura do satélite dele para comandar a sua base de longe.
- Quem está no **mesmo time do scoreboard** também não é atacado.

## Para admins

Precisa da permissão `missil.admin` (os operadores do servidor têm).

| Comando | O que faz |
|---|---|
| `/sam dar <jogador> <item> [qtd] [duração]` | Entrega itens do plugin (veja a lista abaixo). `duração` (1 a 3) vale para foguetes e mísseis. |
| `/sam admin <chave> on` / `off` | Liga ou desliga uma parte do sistema no servidor inteiro (veja [Administração](Administracao.md#chaves-de-ligadesliga)). |
| `/sam admin municao-infinita on` / `off` `[global]` | Munição infinita no lançador olhado (ou em todos, com `global`). |
| `/sam admin municao-infinita padrao` | O lançador olhado volta a usar o valor do config. |
| `/sam admin cooldown <segundos> [global]` | Recarga do lançador olhado (ou de todos). |
| `/sam admin cooldown padrao` | O lançador olhado volta a usar a recarga do config. |
| `/sam bedrock` | Também lista quem está no Bedrock agora. |
| `/sam bedrock <jogador> [sim\|nao\|auto]` | Mostra ou marca à mão se o jogador está no Bedrock (`auto` volta à detecção). |
| `/sam bedrock exportar` | Gera de novo os arquivos do Geyser em `plugins/Missil/geyser/` (e copia para o Geyser do mesmo servidor). |
| `/sam bedrock calibrar` | Blocos de calibração dos modelos do Bedrock por 25 s (veja [Bedrock](Bedrock.md#calibrar-os-modelos)). |
| `/sam admin reload` | Relê o `config.yml` e o `receitas.yml`, e mostra o resumo das receitas (quantas carregaram e quantas têm erro). |
| `/sam teste [cenário]` | Autoteste dentro do servidor. **Use num mundo de teste**: ele monta construções e explode coisas. |

**Itens do `/sam dar`:** `foguete_guiado`, `missil_sam`, `radar`, `lancador`, `link`, `monitor` (Mesa de Radar), `missil_balistico`, `silo`, `comporta`, `satelite`, `missil_antissatelite`, `terminal`, `base_drones`, `drone_patrulha`, `drone_reconhecimento`, `drone_kamikaze`, `flare`, `chaff`, `dispensador`, `bloqueador_portatil`, `bloqueador`, `ciws`, `municao_ciws`, `carga_emp`, `sirene`, `bloco_acao`, `combustivel_foguete`, `circuito`, `ogiva_multipla`, `ponta_perfurante`, `carga_incendiaria`, `carga_fumaca`, `granada_fumaca`, `mina_terrestre`, `mina_antidrone`, `mina_naval`, `missil_cruzeiro`.

Exemplo: `/sam dar Steve missil_balistico 4 3` entrega 4 Mísseis Balísticos com duração de voo 3.

## Permissões

| Permissão | Quem tem | Libera |
|---|---|---|
| `missil.use` | todo mundo | o menu e os comandos de jogador |
| `missil.balistico` | todo mundo | lançar mísseis balísticos dos próprios silos |
| `missil.admin` | operadores | `/sam dar`, `/sam admin`, `/sam teste`, o menu de administração e mexer nos equipamentos de qualquer um (inclui as outras duas) |

---

← [Ogivas e minas](Ogivas-e-Minas.md) · Próximo: [Administração](Administracao.md) →
