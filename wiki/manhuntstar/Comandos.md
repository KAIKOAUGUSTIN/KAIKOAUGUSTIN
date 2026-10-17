# Comandos

Todos os comandos ficam no `/manhunt` e exigem a permissão `manhuntstar.admin` (os operadores já têm).

Os verbos são os mesmos em tudo:
- `create` e `remove` para bots e grupos;
- `add` e `remove` para listas;
- `clear` para apagar um valor.

As posições aceitam `~ ~ ~`. Sem posição, vale onde você está.

## Partida

| Comando | O que faz |
|---|---|
| `/manhunt start` | Começa a caçada na hora: solta todas as rodas e pula a contagem. |
| `/manhunt pause` · `/manhunt resume` | Pausa e continua. Veja [A roda e a caçada](Roda-e-Cacada.md#pausa). |
| `/manhunt target <jogador>` · `/manhunt target clear` | Força todos a perseguirem um jogador / volta ao normal. |
| `/manhunt ring` | Mostra a roda. |
| `/manhunt ring point [x y z \| clear]` | Marca um ponto fixo para as rodas (centro em manual) ou apaga o ponto. |
| `/manhunt players` · `players add\|remove <jogador>` · `players mode <off\|allowlist\|blocklist>` | Lista de jogadores que podem (ou não) ser caçados. |

## Bots

| Comando | O que faz |
|---|---|
| `/manhunt create <nome> [qtd] [dificuldade] [skin <jogador>] [at <x y z>] [fase] [agressividade]` | Cria bots onde você está, no ponto da roda (centro em manual) ou em `at x y z`. |
| `/manhunt remove <bot>` | Remove os bots com esse nome. |
| `/manhunt remove all confirm` | Apaga todos os bots, inclusive o salvamento. |
| `/manhunt list` · `/manhunt info <bot>` | Lista os bots: vida, fase, alvo, local e o que a IA está fazendo. |
| `/manhunt tp <bot\|all> [jogador]` | Leva os bots até um jogador (ou até você). |
| `/manhunt skin <bot> <jogador>` | Troca a skin. |
| `/manhunt spawnpoint <bot> [x y z \| clear]` | Ponto de renascimento de um bot. |
| `/manhunt equip item <item>` · `/manhunt equip armor <tipo>` | Dá um item ou uma armadura a todos os bots. |
| `/manhunt test <tnt-craft\|bow-burst\|firework-crossbow>` | Testa uma capacidade especial contra você. |

As opções do `create` vêm sempre nesta ordem:

| Opção | Valores |
|---|---|
| dificuldade | `easy`, `medium`, `hard` ou `terminator` |
| fase | de 1 a 10 |
| agressividade | de 0 a 10 |

## Grupos

Veja a página [Grupos](Grupos.md).

## Opções e menu

| Comando | O que faz |
|---|---|
| `/manhunt settings` | Mostra todas as opções. |
| `/manhunt settings <opção> [valor]` | Mostra ou muda uma opção. As chaves estão em [Configuração](Configuracao.md). |
| `/manhunt reload` | Relê o `config.yml` e o `messages.yml`. |
| `/manhunt menu` | Menu em baú com quatro seções: Partida, Regras da caçada, Bots e Configurações. No menu, os nomes de bots e grupos são digitados no chat. |

## Nomes e Tab

Nomes com `%`, acento ou espaço vão entre aspas, por exemplo `/manhunt group "Caçador%" role escape`. O Tab completa os nomes já com as aspas.

Os nomes antigos das opções (`starttime`, `glowing`, `nodes`...) continuam valendo no `/manhunt settings`, mas não aparecem no Tab.

---

← [Grupos](Grupos.md) · Próximo: [Configuração](Configuracao.md) →
