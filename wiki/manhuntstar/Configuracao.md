# Configuração

Tudo fica comentado em `plugins/ManhuntStar/config.yml`. Há três jeitos de mudar uma opção:
- no jogo, com `/manhunt settings <chave> <valor>`;
- no `/manhunt menu`, em Configurações;
- editando o arquivo e rodando `/manhunt reload`.

As tabelas abaixo mostram a opção do arquivo, a chave do comando e o valor padrão. As mensagens do plugin ficam no `messages.yml`.

## Geral

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `geral.tab-list` | `tablist` | true | Bots na lista do TAB, com skin e ping. |
| `geral.mensagens-entrada-saida` | `joinmessages` | true | "X entrou/saiu do jogo" para os bots. |
| `geral.mensagens-morte` | `deathmessages` | true | Mensagens de morte dos bots no padrão do jogo. |
| `geral.contar-na-lista-de-servidores` | `serverlistcount` | true | Bots contam no número de jogadores online. |
| `geral.incluir-no-comando-list` | `listcommand` | true | O `/list` mostra os bots. |
| `geral.respeitar-pvp-desligado` | `respectpvp` | false | Com o pvp desligado no mundo, os bots não batem em jogadores. |
| `geral.skin-robo-mineskin` | `mineskin` | true | Sem skin para o nome, usa um `.png` da pasta `skins/` (ou o robô), assinado pelo MineSkin. |

## Bots

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `bots.vida-maxima` | `bothealth` | 20 | Vida máxima. |
| `bots.invenciveis` | `botinvincible` | false | Bots só morrem pelo void e pelo `/kill`. |
| `bots.respawn` | `respawn` | true | Renascem 5 s depois de morrer. |
| `bots.persistentes` | `persistentbots` | true | Bots, grupos e equipamento salvos no `bots.yml` ao reiniciar. |
| `bots.dropar-inventario` | `dropinventory` | true | Derrubam o inventário ao morrer. |
| `bots.persistencia-equipamento` | `gearpersistence` | keep_on_respawn_no_drop | O que acontece com o melhor equipamento ao morrer. Veja [Dificuldades e fases](Dificuldades-e-Fases.md#morte-e-renascimento). |
| `bots.multiplicador-duracao-fase` | `phasemultiplier` | 1.0 | Multiplica a duração de cada fase. |
| `bots.dificuldade-padrao` | `defaultdifficulty` | terminator | Dificuldade quando o comando não informa. |
| `bots.comer-automaticamente` | `autoeat` | true | Comem quando ficam com fome. |
| `bots.maca-dourada-automatica` | `autogapple` | true | Maçã dourada em combate (fase 5+). |
| `bots.fugir-do-fogo-com-agua` | `firewaterescape` | true | Apagam o fogo com balde de água (fase 3+). |
| `bots.mobs-atacam-bots` | `mobsattackbots` | true | Mobs hostis atacam os bots. |
| `bots.mobs-que-nao-atacam-bots` | (só no arquivo) | [] | Mobs que nunca miram nos bots, por exemplo `CREEPER`. |
| `bots.suavidade-mira-ms` | `aimsmoothness` | 0 | Suavidade da mira em ms (0 = instantânea). |

## Combate

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `combate.prioridade-alvo` | `targetpriority` | 2.0 | De 5 (só jogadores) a -5 (só mobs). |
| `combate.modo-alvo` | `targetmode` | equal | Como dividem os jogadores: `closest`, `equal`, `farthest`. |
| `combate.tridente` | `allowtrident` | true | Tridente (fase 4+). |
| `combate.besta` | `allowcrossbow` | true | Besta (fase 3+). |
| `combate.lanca-a-cavalo` | `allowspear` | true | Carga de lança a cavalo (fase 4+). |
| `combate.imprecisao-projeteis` | `projinaccuracy` | 1.0 | Multiplica a imprecisão de flechas e tridente. |
| `combate.humanizacao` | `humanize` | 0.0 | De 0 a 1: erros de mira, golpes perdidos e ritmo irregular. |

Com a humanização ligada, valem também `meleemisschance`, `meleedelayjitter`, `meleereachvariance`, `meleeaimoffset` e `meleespamvariance`.

## Mobilidade

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `mobilidade.construir-torres` | `allowtowering` | true | Torres e pontes perto do alvo. |
| `mobilidade.perolas` | `allowpearl` | true | Pérolas do End. |
| `mobilidade.multiplicador-recarga-perola` | `pearlcooldownmult` | 1.0 | Multiplica a recarga das pérolas. |
| `mobilidade.dimensao-perolas` | `pearldimension` | nether | Onde usam pérolas: `nether`, `ambas`, `overworld`. |
| `mobilidade.cavalos` | `allowhorse` | true | Cavalos (fase 4+). |
| `mobilidade.barcos` | `allowboat` | true | Barcos para perseguir e atravessar lagos. |
| `mobilidade.elytra` | `allowelytra` | false | Elytra para alcançar alvos longe. |
| `mobilidade.redistribuir` | `allowredistribution` | true | Bots muito longe reaparecem perto do alvo. |
| `mobilidade.distancia-redistribuicao` | `redistdistance` | 200 | Distância para a redistribuição, em blocos. |
| `mobilidade.atraso-min-dimensao-segundos` | `minnetherdelay` | 30 | Tempo mínimo para seguir o alvo para outra dimensão. |
| `mobilidade.atraso-max-dimensao-segundos` | `maxnetherdelay` | 60 | Tempo máximo para seguir o alvo para outra dimensão. |

## Pathfinding

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `pathfinding.modo` | `pathmode` | ASTAR | `ASTAR` ou `DUMB` (anda direto). |
| `pathfinding.gulosidade` | `pathgreediness` | 1.5 | Maior = mais rápido, caminhos piores. |
| `pathfinding.limite-nos` | `pathnodes` | 2500 | Limite de nós do A*. |
| `pathfinding.limite-dinamico` | `pathdynamicnodes` | true | Ajusta o limite conforme o tempo de cálculo. |
| `pathfinding.fallback-dumb` | `pathfallback` | true | Sem caminho, anda direto para o alvo. |
| `pathfinding.assincrono` | `pathasync` | true | Calcula fora da thread principal. |
| `pathfinding.debug-particulas` | `pathdebug` | false | Mostra o caminho em partículas para quem tem `manhuntstar.admin`. |

## Táticas

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `taticas.emboscada-caverna` | `caveambush` | true | Emboscada em caverna com cama. |
| `taticas.recarga-emboscada-caverna-segundos` | `caveambushcooldown` | 1 | Segundos entre um bot e o próximo ir para a emboscada. |
| `taticas.capacidades-automaticas` | `autocapacities` | false | Emboscada de TNT e besta com fogos automáticas. |
| `taticas.besta-com-fogos` | `fireworkcrossbow` | false | Besta com fogos. |
| `taticas.pressao-de-arco` | `bowpressure` | true | Rajada de arco quando o bot fica muito tempo sem acertar. |
| `taticas.mortes-silenciosas` | `silentdeaths` | true | O bot mais longe some e renasce mais perto. |
| `taticas.entrada-por-portal` | `portalentrance` | true | Bots chegam em outra dimensão saindo de um portal que o jogador vê. |

## Manhunt

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `manhunt.modo-spawn` | `spawnmode` | MANHUNT | `MANHUNT` (roda) ou `NORMAL`. |
| `manhunt.contagem-segundos` | `countdown` | 20 | Contagem de vantagem. |
| `manhunt.contagem-ao-sair-da-roda` | `countdownonleave` | true | A contagem espera alguém sair da roda. |
| `manhunt.invulneravel-na-contagem` | `countdowninvulnerable` | true | Bots da roda sem dano até a caçada começar. |
| `manhunt.raio-roda` | `ringradius` | 0 | Raio da roda (0 = automático). |
| `manhunt.centro-roda` | `ringcenter` | automatico | `automatico` ou `manual`. |
| `manhunt.quem-entra-no-meio` | `latejoin` | protegido | `protegido`, `cacado` ou `fora`. |
| `manhunt.lista-modo` | `playerlistmode` | desligada | `desligada`, `permitidos` ou `bloqueados`. |
| `manhunt.lista-jogadores` | (`/manhunt players`) | [] | Nomes da lista de jogadores. |

## Aparência

| Opção | Chave | Padrão | O que faz |
|---|---|---|---|
| `aparencia.brilho-cacadores` | `glowhunters` | false | Brilho nos caçadores. |
| `aparencia.cor-brilho-cacadores` | `glowhunterscolor` | red | Cor do brilho dos caçadores. |
| `aparencia.brilho-fugitivos` | `glowescapers` | false | Brilho nos fugitivos. |
| `aparencia.cor-brilho-fugitivos` | `glowescaperscolor` | aqua | Cor do brilho dos fugitivos. |
| `aparencia.mostrar-nome` | `nametag` | true | Nome visível em cima do bot. |

---

← [Comandos](Comandos.md) · Próximo: [Perguntas frequentes](Perguntas-Frequentes.md) →
