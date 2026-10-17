# Dificuldades e fases

## Dificuldades

A dificuldade vai no `/manhunt create`, por exemplo `/manhunt create Cacador 3 hard`. Sem ela, vale `bots.dificuldade-padrao` (Terminator).

| Dificuldade | Fase inicial | Tempo de cada fase | Dano que recebe | Dano que causa | Chance dos drops da fase ao morrer (comida, maçãs, armas) |
|---|---|---|---|---|---|
| `easy` (Fácil) | 1 | 5 min | 100% | 100% | 100% |
| `medium` (Médio) | 2 | 3 min | 95% | 100% | 50% |
| `hard` (Difícil) | 4 | 4 min 10 s | 90% | 110% | 10% |
| `terminator` | 8 | 10 min | 85% | 115% | 0% |

O tempo de cada fase é multiplicado por `bots.multiplicador-duracao-fase`.

Para começar numa fase diferente, informe a fase (1 a 10) no `/manhunt create` ou no menu. Ela vale mesmo abaixo da fase inicial da dificuldade: um Terminator criado na fase 3 começa na 3.

## Fases

Os bots sobem de fase com o tempo e nunca descem. A cada fase nova, o servidor inteiro vê o aviso **[BOTS MAIS FORTES]**.

O relógio das fases só anda durante a caçada. Ele para na roda, na contagem, na pausa e quando não há jogador para caçar (morto, desconectado ou em espectador).

| Fase | O que o bot ganha |
|---|---|
| 1 | Sem equipamento: persegue, cava, faz pontes e se vira. |
| 2 | Espada de madeira e comida básica. |
| 3 | Besta, balde de água contra fogo e comida melhor. |
| 4 | Armadura de couro, espada de pedra, escudo, tridente com lealdade, cavalos e rajada de arco. |
| 5 | Armadura e espada de ferro, balde de lava e maçãs douradas. |
| 6 | Ferro com Proteção I, drops melhores e barcos contra alvos na água. |
| 7 | Espada de diamante, parte da armadura de diamante e drops mais fortes. |
| 8 | Diamante completo com Proteção II e espada com Afiação II. No Terminator, a armadura já é de netherite. |
| 9 | A recarga da pérola cai 50%. |
| 10 | A recarga da pérola cai 75%. É a última fase das outras dificuldades. |
| 12 | **Fase final, só do Terminator:** armadura de netherite e espada de netherite com Repulsão. |

## Saltos de fase

Os bots também pulam de fase na hora quando o jogador caçado fica mais forte. O servidor vê o aviso **[SALTO DE FASE]** com o motivo.

| O jogador... | Os bots vão para |
|---|---|
| segura uma arma de madeira | fase 2 |
| tem ferro no inventário | fase 4 |
| tem mais de 20 de ferro (bloco de ferro conta 9) | fase 5 |
| tem 5 ou mais diamantes (bloco de diamante conta 9) | fase 5 |
| entra no Nether | fase 5 |

Os bots que entram no Nether também vão para a fase 5, no mínimo.

## Morte e renascimento

- **Renascimento:** o bot renasce 5 s depois de morrer (`bots.respawn`), no ponto de renascimento dele ou do grupo, se houver um.
- **Equipamento ao morrer** (`bots.persistencia-equipamento`), para a melhor espada, picareta e armadura:
  - `keep_on_respawn_no_drop` (padrão): o bot mantém e não derruba;
  - `keep_and_drop`: o bot mantém e derruba uma cópia;
  - `drop_and_lose`: o bot derruba e perde.
- **Emboscada em caverna:** depois de renascer na cama da emboscada, o bot volta à fase 1 e recupera uma fase a cada 5 s.

---

← [A roda e a caçada](Roda-e-Cacada.md) · Próximo: [O que os bots fazem](O-que-os-Bots-Fazem.md) →
