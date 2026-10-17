# Grupos

O nome usado no `/manhunt create` vira um **grupo**. Por exemplo, `/manhunt create Cacador 5` cria o grupo `Cacador`, com os bots `Cacador1` a `Cacador5`. Com `%` no nome, o número entra no lugar do `%`.

Os comandos de grupo levam o nome do grupo antes da ação.

| Comando | O que faz |
|---|---|
| `/manhunt group <grupo> role hunter` | O grupo caça (o padrão). |
| `/manhunt group <grupo> role escape` | O grupo foge. |
| `/manhunt group <grupo> enemy add <outro>` | Os dois grupos lutam entre si. Para desfazer, use `enemy remove <outro>`. |
| `/manhunt group <grupo> spawnpoint [x y z]` | Ponto onde o grupo renasce. Para apagar, use `spawnpoint clear`. |
| `/manhunt group <grupo> phases <true\|false>` | Liga ou desliga as fases do grupo. |
| `/manhunt group <grupo> chaseplayers <true\|false>` | O grupo persegue ou ignora os jogadores. |
| `/manhunt group <grupo> remove` | Remove o grupo e os bots dele. |

## Exemplos

**Bots contra bots:** dois grupos inimigos que ignoram os jogadores.
```
/manhunt create Azul 5
/manhunt create Vermelho 5
/manhunt group Azul enemy add Vermelho
/manhunt group Azul chaseplayers false
/manhunt group Vermelho chaseplayers false
```

**Caçadores e fugitivos:** um grupo foge e o outro caça.
```
/manhunt create Fugitivo 2
/manhunt group Fugitivo role escape
/manhunt create Cacador 4
```

## Brilho

Para ver os bots através das paredes, ligue o brilho no menu (Configurações) ou por comando:

| Quem brilha | Opção do `config.yml` | Comando | Cor padrão |
|---|---|---|---|
| Caçadores | `aparencia.brilho-cacadores` | `/manhunt settings glowhunters true red` | vermelho |
| Fugitivos | `aparencia.brilho-fugitivos` | `/manhunt settings glowescapers true aqua` | ciano |

O brilho vem desligado.

---

← [O que os bots fazem](O-que-os-Bots-Fazem.md) · Próximo: [Comandos](Comandos.md) →
