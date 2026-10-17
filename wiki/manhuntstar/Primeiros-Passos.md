# Primeiros passos

## Instalar

1. Coloque `ManhuntStar-1.5.3.jar` na pasta `plugins/` de um servidor **Paper 26.2** (ou 26.3), com Java 25.
2. Inicie o servidor. O plugin cria `plugins/ManhuntStar/config.yml`, `messages.yml` e a pasta `skins/`.

Ele não depende de outros plugins.

Os comandos exigem a permissão `manhuntstar.admin`, que os operadores já têm.

## A primeira caçada

1. Fique onde a caçada vai começar e crie os bots:
   ```
   /manhunt create Cacador 3
   ```
   Isso cria 3 bots na dificuldade padrão (Terminator). Para escolher a dificuldade:
   ```
   /manhunt create Cacador 3 easy
   ```
2. Os bots nascem **em roda** à sua volta e ficam parados, sem levar dano.
3. **Saia da roda.** Começa a contagem de vantagem (20 s por padrão), com barra no topo da tela e títulos 3-2-1.
4. Quando a contagem acaba, os bots começam a caçar. Corra!

Para soltar todos na hora, sem esperar a contagem, use `/manhunt start`.

Prefere clicar? Use `/manhunt menu`. O menu tem quatro seções: Partida, Regras da caçada, Bots e Configurações.

## Durante a caçada

| Quero... | Comando |
|---|---|
| Pausar tudo | `/manhunt pause` (e `/manhunt resume` para continuar) |
| Ver os bots, a vida, a fase e o que cada um está fazendo | `/manhunt list` e `/manhunt info <bot>` |
| Trazer os bots até mim | `/manhunt tp all` |
| Fazer todos perseguirem um jogador | `/manhunt target <jogador>` |
| Acabar com a caçada | `/manhunt remove all confirm` |

Nomes com `%`, acento ou espaço vão entre aspas, por exemplo `/manhunt create "Caçador%" 5`. O Tab completa os nomes já com as aspas.

---

← [Início](README.md) · Próximo: [A roda e a caçada](Roda-e-Cacada.md) →
