# Perguntas frequentes

**Criei os bots e eles não saem do lugar.**
É a roda: eles esperam um jogador que estava dentro dela sair. Saia da roda ou use `/manhunt start`. Se o servidor estiver pausado, use `/manhunt resume`.

**Os bots não me atacam.**
Confira estes pontos:
- se a lista de jogadores (`/manhunt players`) deixou você de fora;
- se você entrou no meio da caçada e ainda está protegido;
- se o grupo está com `chaseplayers false`;
- se o pvp está desligado no mundo com `respeitar-pvp-desligado: true`.

**Os bots ficaram fortes rápido demais.**
- Eles pulam de fase quando você tem ferro, diamantes ou entra no Nether (veja [Saltos de fase](Dificuldades-e-Fases.md#saltos-de-fase)).
- Para fases mais lentas, aumente `bots.multiplicador-duracao-fase`.
- Para começar mais fraco, use uma dificuldade menor ou informe a fase no `/manhunt create`.

**Como tiro todos os bots?**
`/manhunt remove all confirm`. Esse comando também apaga o salvamento.

**A skin do bot ficou como robô.**
O nome não tem conta Mojang. Use `/manhunt skin <bot> <jogador>` ou coloque um `.png` na pasta `plugins/ManhuntStar/skins/`.

## Limitações

- Outros plugins que procuram "jogadores", como a bússola de outro plugin de ManHunt, não enxergam os bots. Eles aparecem no TAB, no `/list` e na contagem, mas não são jogadores para a API do servidor.
- A lista do TAB usa pacotes internos do servidor. Se uma versão futura do Paper mudar esses pacotes, só essa função se desliga (com aviso no console) e o resto continua.

## Para quem faz plugins

A API fica em `dev.manhuntstar.api.ManhuntStarAPI`: listar os bots e achar o bot de uma entidade.

Os eventos são:
- `BotEvents.BotDamageByPlayerEvent`;
- `BotFallDamageEvent`;
- `BotDeathEvent`;
- `BotKilledByPlayerEvent`.

## Créditos

O Manhunt* se baseia no mod Fabric **T\* (Terminator Star)**, de **OpaleMC**, com licença CC0. O comportamento foi estudado no mod e reescrito do zero para a API do Paper.

---

← [Configuração](Configuracao.md) · [Início](README.md)
