# A roda e a caçada

## A roda

No modo **MANHUNT** (o padrão, `manhunt.modo-spawn`), os bots nascem em roda e esperam a caçada começar. No modo **NORMAL** eles nascem no ponto e já saem caçando.

- **A roda não tem dono.** Os bots esperam até **um jogador que estava dentro sair** dela; vale o primeiro que sair.
- **Roda criada longe de todos:** espera alguém entrar e sair, ou o `/manhunt start`.
- **Proteção:** enquanto esperam e durante a contagem, os bots da roda não levam dano (`manhunt.invulneravel-na-contagem`).
- **Várias rodas:** cada roda tem a sua contagem.
- **Reinício do servidor:** a roda é salva e continua esperando.

### Tamanho e lugar

- **Raio** (`manhunt.raio-roda`): `0` é automático, com 5 blocos mais 1 a cada 5 bots.
- **Centro** (`manhunt.centro-roda`):
  - `automatico`: a roda fica onde ela é criada, na sua posição ou no `at x y z` do `/manhunt create`.
  - `manual`: a roda fica no ponto marcado com `/manhunt ring point x y z`. `/manhunt ring point clear` apaga o ponto e volta ao automático.
- **Ver a roda:** `/manhunt ring`.

## A contagem de vantagem

`manhunt.contagem-segundos` (padrão 20) é o tempo que você tem antes dos bots saírem. Ela aparece numa barra no topo da tela e em títulos 3-2-1.

- `0`: os bots saem assim que alguém sai da roda.
- `manhunt.contagem-ao-sair-da-roda: false`: a contagem começa assim que os bots são criados, sem esperar ninguém sair.

## Pausa

`/manhunt pause` congela cada bot onde está, até no ar, montado ou de barco. Parado, ele fica invencível e não pensa. A pausa também para:
- a contagem da roda;
- a proteção de quem entrou no meio;
- o tempo das fases;
- o renascimento.

A pausa continua se o servidor reiniciar. Para voltar, use `/manhunt resume`.

## Quem é caçado

### Quem entra no meio da caçada

Quem entra no servidor com a caçada em andamento segue `manhunt.quem-entra-no-meio`:

| Valor | O que acontece |
|---|---|
| `protegido` (padrão) | Fica sem ser alvo pelo tempo da contagem da roda, no mínimo 5 s. |
| `cacado` | Vira alvo na hora. |
| `fora` | Não é caçado até a próxima caçada. |

Quem já estava na caçada, cai e volta continua sendo caçado.

### Lista de jogadores

Use `/manhunt players` para ver a lista e `/manhunt players add|remove <jogador>` para editá-la. `/manhunt players mode` escolhe o modo:

| Modo | Efeito |
|---|---|
| `off` (desligada) | Todos podem ser caçados. |
| `allowlist` (permitidos) | Só os da lista são caçados e disparam a roda. |
| `blocklist` (bloqueados) | Os da lista não são caçados nem disparam a roda. |

`/manhunt target <jogador>` passa por cima da lista: todos os bots perseguem esse jogador. Para voltar ao normal, use `/manhunt target clear`.

### Como os bots dividem os alvos

`combate.modo-alvo` decide como os bots dividem os jogadores:
- `closest`: cada bot vai no jogador mais perto;
- `equal` (padrão): os bots se dividem igualmente entre os jogadores;
- `farthest`: cada bot vai no jogador mais longe.

`combate.prioridade-alvo` decide entre jogadores e mobs, de `5` (só jogadores) a `-5` (só mobs).

---

← [Primeiros passos](Primeiros-Passos.md) · Próximo: [Dificuldades e fases](Dificuldades-e-Fases.md) →
