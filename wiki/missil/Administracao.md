[Início](README.md) › Administração

# Administração

Esta página é para quem administra o servidor (permissão `missil.admin`).

## Instalação

- Servidor **Paper 26.3** com **Java 25**.
- Copie `Missil-2.1.0.jar` para a pasta `plugins/` e reinicie. Na primeira vez são criados `plugins/Missil/config.yml` e `plugins/Missil/receitas.yml`.
- Para compilar do código: `./gradlew build` (o jar sai em `build/libs/`).

## O menu de administração

`/sam` → **Administração**. Cada botão muda o `config.yml`, salva e vale na hora.

| Botão | Chave no config | O que faz |
|---|---|---|
| Mísseis contra alvos no chão | `sam.terrestre.ativo` | Desligado, nenhum radar ataca quem está no chão; o resto continua. |
| Mísseis balísticos (silos) | `balistico.ativo` | Desligado, nenhum silo lança. |
| Anti-míssil da besta | `besta.anti-missil.ativo` | O foguete teleguiado trava e derruba mísseis. |
| Munição infinita (todos) | `sam.lancador.municao-infinita` | Para os lançadores sem valor próprio. |
| Política da rede | `sam.rede.politica` | `DISTRIBUIR` (um míssil por alvo por vez) ou `CONCENTRAR` (salva no alvo mais perto). |
| Alvos de radares novos | `sam.radar.alvos-padrao` | Modo com que cada radar novo começa. |
| Recarga dos lançadores | `sam.lancador.cooldown` | Esquerdo −1 s, direito +1 s. |
| Debug no console | `debug` | Registra cada lançamento e o resultado. |
| Recarregar config.yml | — | Relê o arquivo do disco. |
| Dar itens | — | Pegue qualquer item do plugin (Shift + clique: 16). |
| Radares / Lançadores / Silos / Comportas de todos | — | As listas com os equipamentos de todo mundo. |
| Drones | `drones.ativo` | Desligado, nenhuma base lança; os que estão no ar voltam. |
| Radar antidrone | `sam.radar.antidrone` | Radares atacam drones e kamikazes inimigos. |
| Radar antimíssil | `sam.radar.antimissil` | Radares atacam balísticos, antissatélites e foguetes de satélite inimigos. |
| Bases de drones de todos | — | Lista. |
| CIWS | `ciws.ativo` | Desligado, nenhum CIWS atira. |
| CIWS contra aeronaves e barcos | `ciws.aeronaves-e-barcos` | O CIWS também atira em quem voa de elytra ou montaria e em quem está de barco. |
| Guerra eletrônica | `guerra-eletronica.ativo` | Flare, chaff, dispensador e bloqueadores. |
| Defesas de todos | — | Lista de CIWS e bloqueadores. |
| Ogiva EMP | `emp.ativo` | Desligado, nenhum silo lança EMP. |
| Alertas da base | `alertas.ativo` | Desligado, nenhuma sirene toca e nenhum Bloco de Ação liga. |
| Alertas de todos | — | Lista de sirenes e blocos de ação. |

Nas listas, o admin alterna entre **só os seus** e **os de todos** (botão no canto). Na tela de um lançador, o admin também muda a munição infinita e a recarga só daquele lançador.

## Chaves de liga/desliga

`/sam admin <chave> on|off` faz o mesmo pelo chat:

| Chave | Config |
|---|---|
| `terrestre` | `sam.terrestre.ativo` |
| `balistico` | `balistico.ativo` |
| `antimissil` | `besta.anti-missil.ativo` |
| `satelite` | `satelite.ativo` |
| `antissatelite` | `antissatelite.ativo` |
| `comunicacao` | `comunicacao.exigir-satelite` (desligado: comanda tudo de qualquer distância, como antes da 2.0.0) |
| `drones` | `drones.ativo` |
| `antidrone` | `sam.radar.antidrone` |
| `antimissil-radar` | `sam.radar.antimissil` |
| `ciws` | `ciws.ativo` |
| `ciws-aeronaves` | `ciws.aeronaves-e-barcos` |
| `guerra-eletronica` | `guerra-eletronica.ativo` |
| `emp` | `emp.ativo` |
| `alertas` | `alertas.ativo` |

## O `config.yml`

Tudo é ajustável, inclusive as mensagens (em formato MiniMessage). As seções:

| Seção | O que tem |
|---|---|
| `fisica`, `limites` | gravidade, ar, máximo de mísseis no ar ao mesmo tempo |
| `besta` | modo padrão, `receita-quantidade` (quantos foguetes saem quando a receita não diz), trava (alcance, cones, tempo, Multishot), anti-míssil, física do foguete, explosão, FPV (câmera e o que acontece ao sair: `BALISTICO` ou `AUTODESTRUIR`) |
| `sam` | radar (alcance, varredura, linha de visada, mísseis por alvo, modo padrão, antidrone, antimíssil), ataque terrestre, rede (distâncias, auto-conectar, política), lançador (munição infinita, recarga, alcances), física e explosão do míssil |
| `comporta` | tempo para abrir e para fechar, distância da ligação |
| `balistico` | alcance mínimo e de cada nível do míssil (`alcance-max-por-nivel`), recarga, ogiva (`potencia-por-tnt`, `tnt-maximo`, `potencia-maxima`, `escala-cratera`), arco, explosão |
| `monitor` | Mesa de Radar: alcance para achar o radar, atualização, margem, relevo, aliados, rastro, `rotacao` (se o mapa aparecer girado) |
| `comunicacao` | `exigir-satelite` e `alcance-radio` (500 m) |
| `satelite`, `antissatelite` | cobertura, altitude, vida, velocidade, alerta antecipado, mapa; alcance, dano e raio do antissatélite |
| `drones` | patrulha, reconhecimento e kamikaze: vida, velocidade, bateria, altura, rota, flechas, alcances, TNT |
| `guerra-eletronica` | flare, chaff, dispensador e bloqueadores |
| `ciws` | alcance, ritmo, chances perto e longe, dano em aeronaves e barcos |
| `emp` | `raio` (64 m) e `duracao` (60 s) |
| `alertas` | quanto tempo um alerta fica ligado, raio máximo, sirene e Bloco de Ação |
| `avisos` | aviso de radar e de míssil chegando para quem é alvo |
| `mensagens` | todos os textos do plugin |

Depois de editar o arquivo, use `/sam admin reload` (ou o botão no menu).

## Receitas (`receitas.yml`)

As receitas ficam num arquivo à parte, `plugins/Missil/receitas.yml`. Na primeira partida, o plugin cria o arquivo com as receitas padrão (as da página [Receitas](Receitas.md)). Depois disso o arquivo é seu: o plugin só lê. Use `/sam admin reload` depois de editar.

Cada entrada é uma receita:

```yaml
missil_balistico_3:
  item: missil_balistico          # o id do item que sai (os de /sam dar)
  duracao: 3                      # 1, 2 ou 3: foguete, Míssil SAM e Míssil Balístico (sem ela, 3)
  quantidade: 1                   # de 1 a 64 (sem ela, 1)
  forma: ["FKF", "NSN", "FCF"]    # até 3 linhas de até 3 letras; espaço é casa vazia
  ingredientes:
    F: missil:combustivel_foguete # missil:<id> = item do plugin
    K: COMPASS                    # nome do item do jogo, em inglês
    N: NETHERITE_INGOT
    S: NETHER_STAR
    C: missil:circuito
  ativo: true                     # false desliga a receita
```

- **Sem forma:** no lugar de `forma` e `ingredientes`, use `sem-forma: [PAPER, ENDER_EYE, GUNPOWDER]`. Os itens vão em qualquer casa da grade, e para pedir mais de um é só repetir o item.
- **Itens do plugin como ingrediente:** só entram na casa que pede aquele item. Em qualquer outro lugar, numa receita do plugin ou do jogo, eles nunca são ingrediente. Vale também para o Crafter (o bloco).
- **Nível do balístico:** cada nível do Míssil Balístico é uma entrada (`missil_balistico_1`, `_2` e `_3`), com a sua `duracao`. O alcance de cada nível fica em `balistico.alcance-max-por-nivel`, no `config.yml`.
- **Foguete Teleguiado:** sem `quantidade`, usa `besta.receita-quantidade`, do `config.yml`.

**Erros:**
- **Entrada com erro** (material ou item que não existe, letra sem ingrediente, forma maior que 3x3, número fora da faixa ou campo com nome errado): é pulada, e o console mostra o nome dela e o motivo. As outras continuam valendo.
- **Resumo:** no fim da leitura aparece um resumo, como `Receitas: 31 carregadas, 1 com erro (veja acima)`, e quem usou `/sam admin reload` recebe o mesmo resumo no chat.
- **Erro de sintaxe no arquivo inteiro:** as receitas que já valiam continuam. Na partida do servidor, valem as padrão.
- **Voltar às receitas padrão:** apague o arquivo e use `/sam admin reload`.

**Vindo da 2.0.0:** o arquivo é criado com as receitas novas, que são mais caras. Quem quiser as antigas pode escrevê-las aqui. O Míssil SAM e o Míssil Balístico não herdam mais a duração do foguete de fogos da receita. Os mísseis que já estavam feitos continuam com a duração que tinham.

## Explosões e proteção de região

- As explosões do silo e do kamikaze contam como explosões causadas pelo dono. Elas **só quebram blocos com a regra `mobGriefing` ligada** no mundo. Desligada, só causam dano.
- Cada explosão é uma explosão normal do jogo, então plugins de proteção de região conseguem bloqueá-las.
- O satélite só existe em mundos sem teto (o mundo normal).

## Arquivos salvos

| Arquivo | O que guarda |
|---|---|
| `plugins/Missil/receitas.yml` | as receitas (veja [Receitas](#receitas-receitasyml)) |
| `plugins/Missil/sites.yml` | todos os equipamentos e as configurações de cada um: radares (modo, ligações), lançadores, silos (alvo, ogiva), comportas, mesas (modo do mapa), satélites (posição, destino, vida), bases de drones (rota, altura, patrulha, drones esperando espaço), CIWS e bloqueadores, sirenes e blocos de ação, e os aliados |
| `plugins/Missil/terreno.dat` | o relevo do mapa do satélite |
| `plugins/Missil/fpv-pendentes.yml` | devolve o jogador ao lugar certo se o servidor cair durante um voo FPV |

## Autoteste

`/sam teste [cenário]` monta cenários no mundo e confere se tudo funciona, registrando o resultado no console. Sem cenário, roda todos (`tudo`). **Use num mundo de teste:** ele constrói, lança mísseis e explode coisas. A lista de cenários aparece no autocompletar do comando.

---

← [Comandos e permissões](Comandos-e-Permissoes.md) · Próximo: [Perguntas frequentes](Perguntas-Frequentes.md) →
