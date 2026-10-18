[Início](README.md) › Bedrock (Geyser)

# Jogar no Bedrock (Geyser)

Quem joga no **celular, console ou Windows** (Minecraft Bedrock) entra no servidor pelo [Geyser](https://geysermc.org). Desde a **2.3.0** o Míssil funciona para esses jogadores também: os modelos aparecem, os itens têm nome e ícone, as receitas aparecem na bancada, os menus funcionam só com o toque e dá para pilotar o FPV e os drones.

## Para quem joga

Quase tudo funciona igual ao Java. As diferenças são estas:

| No Java | No Bedrock |
|---|---|
| **Shift + F** troca o modo da besta | **Agachado + toque/clique esquerdo** com a besta na mão, ou o botão **Modo da besta** no `/sam` (também valem no Java) |
| Esquerdo/direito muda números no menu (altura, raio, recarga) | O botão abre a **tela de ajuste**, com **−** e **+** (veja abaixo) |
| Shift + clique pega 16 em **Dar itens** (admin) | Um botão escolhe a quantidade: 1, 16 ou 64 |
| Bancada de trabalho | Bancada também, ou a tela **Fabricar** do `/sam` (veja abaixo) |

- **FPV e câmera dos drones:** girar a tela pilota, o toque/clique esquerdo atira e **agachar sai**, como no Java.
- **Modelos:** mísseis, drones, satélite, CIWS, radar, silo e chamarizes aparecem refeitos com blocos. Ficam um pouco mais "quadrados" que no Java. O brilho dos chamarizes não aparece.
- **Itens do plugin:** os mísseis, drones, chamarizes e componentes têm item próprio, com nome e ícone. Os que são blocos (radar, lançador, silo...) aparecem como o bloco comum, para dar para colocar.
- **`/sam bedrock`** diz se o servidor está tratando você como Bedrock. Se disser "Java" e você está no Bedrock, peça a um admin para usar `/sam bedrock <seu nome> sim`.

### Tela de ajuste

![Tela de ajuste](img/menus/ajuste.svg)

### Tela Fabricar

Serve para todos, no Java e no Bedrock: faz qualquer receita com o que está no inventário, sem a bancada.

![Tela Fabricar](img/menus/fabricar.svg)

## Para o admin: instalação

**Geyser e Floodgate são opcionais.** Sem eles, e sem ninguém no Bedrock, o Míssil funciona exatamente como antes e não cria nada a mais. A adaptação liga sozinha quando aparece um jogador Bedrock.

O Míssil gera dois arquivos em `plugins/Missil/geyser/`:

- `missil-geyser-mappings.json`: os itens do plugin para o Bedrock;
- `Missil.mcpack`: os ícones desses itens.

Eles aparecem quando o Geyser ou o Floodgate roda no mesmo servidor, quando entra o primeiro jogador Bedrock, ou com `/sam bedrock exportar`. O que fazer com eles depende de como o Geyser está instalado:

### 1. Geyser como plugin (Geyser-Spigot) no mesmo servidor

1. Ponha o `Geyser-Spigot.jar` (e, se quiser, o `floodgate-spigot.jar`) na pasta `plugins/`, junto com o Míssil.
2. Inicie o servidor. O Míssil copia os dois arquivos para `plugins/Geyser-Spigot/custom_mappings/` e `plugins/Geyser-Spigot/packs/`.
3. **Reinicie o servidor uma vez**, para o Geyser carregar os itens. Depois de atualizar o Míssil, reinicie de novo se o console avisar que os itens mudaram.

### 2. Geyser Standalone

1. Com o servidor rodando, entre uma vez pelo Bedrock (ou use `/sam bedrock exportar`) para gerar os arquivos.
2. Copie `plugins/Missil/geyser/missil-geyser-mappings.json` para a pasta `custom_mappings/` ao lado do `Geyser.jar`.
3. Copie `plugins/Missil/geyser/Missil.mcpack` para a pasta `packs/` ao lado do `Geyser.jar`.
4. Reinicie o Geyser.

Com o Floodgate no servidor Paper, o Míssil reconhece os jogadores Bedrock pela API dele. Sem nada no Paper, ele reconhece pela marca do cliente ("Geyser").

### 3. Velocity (ou BungeeCord) com Geyser no proxy

1. Gere os arquivos como no Standalone.
2. No proxy, copie `missil-geyser-mappings.json` para `plugins/Geyser-Velocity/custom_mappings/` e `Missil.mcpack` para `plugins/Geyser-Velocity/packs/`. No BungeeCord a pasta é `Geyser-BungeeCord`.
3. Reinicie o proxy.
4. Se o Floodgate está no proxy, ponha o Floodgate também no Paper, com a **mesma `key.pem`**, e use o encaminhamento moderno (*modern forwarding*) do Velocity.

Em qualquer caso, o `enable-custom-content` do config do Geyser precisa estar `true`, que é o padrão.

### Como o Míssil sabe quem é Bedrock

Ele usa a primeira resposta, nesta ordem:

1. a marcação de um admin (`/sam bedrock <jogador> sim|nao`; `auto` volta à detecção);
2. a API do Geyser, se ele roda no mesmo servidor;
3. a API do Floodgate, se ele roda no mesmo servidor;
4. a marca do cliente "Geyser", que chega também do Standalone e do Velocity;
5. o UUID do Floodgate.

O console mostra "Jogador Bedrock: nome (fonte)" quando um entra, e `/sam bedrock` lista quem está no Bedrock agora.

### Testado em

| Instalação | Como reconheceu | Resultado |
|---|---|---|
| Paper + Geyser-Spigot + Floodgate | API do Geyser | tudo funcionou |
| Geyser Standalone + Floodgate no Paper | API do Floodgate | tudo funcionou |
| Geyser Standalone, nada no Paper | marca do cliente | tudo funcionou |
| Velocity + Geyser + Floodgate, Floodgate no Paper | API do Floodgate | tudo funcionou |
| Velocity + Geyser, nada no Paper | marca do cliente | tudo funcionou |

"Tudo funcionou" quer dizer que um cliente Bedrock de teste:

- foi reconhecido;
- recebeu os 15 itens do plugin e as receitas;
- viu os modelos;
- entrou e saiu da câmera de um drone;
- pilotou e atirou;
- trocou o modo da besta;
- usou a tela de ajuste e a tela Fabricar.

O teste não tinha tela: a aparência dos modelos num aparelho de verdade se confere com a calibração abaixo.

## Calibrar os modelos

Os modelos do Bedrock são feitos de blocos na cabeça de *armor stands* invisíveis, que só os jogadores Bedrock veem. Para conferir se eles batem com o lugar certo no seu aparelho:

1. Use `/sam bedrock calibrar` (admin). Aparecem por 25 s, na sua frente, três blocos de vidro com um cubo de vidro vermelho dentro de cada um. O do meio fica girado 45° e o da direita 90°.
2. Olhe pelo celular ou console. Cada cubo vermelho tem que ficar **no meio do vidro e do mesmo tamanho**.
3. Se estiver alto ou baixo, mude `bedrock.modelos.ajuste-altura` no `config.yml` (em blocos; negativo desce). Se estiver grande ou pequeno, mude `bedrock.modelos.ajuste-tamanho` (1.0 = normal).
4. Use `/sam admin reload` e calibre de novo.

## Configuração

```yaml
bedrock:
  ativo: true                 # false: ninguém é tratado como Bedrock
  modelos:
    ativo: true               # refazer os modelos para o Bedrock
    max-cubos-por-peca: 6     # mais = mais fiel e mais entidades (1 a 27)
    ajuste-altura: 0.0
    ajuste-tamanho: 1.0
  fpv-ajuste-olho: 0.0        # altura do olho no FPV, só para o Bedrock
  exportar-para-geyser: true  # gerar os arquivos do Geyser
besta:
  trocar-modo-shift-clique: true  # agachado + clique esquerdo troca o modo da besta (todos)
```

Os modelos só existem nos mundos onde há alguém no Bedrock, e há um teto de 4000 armor stands. Para o resto do plugin eles não existem: não são alvo, o radar não os vê e os mísseis passam por eles.

> **Atenção (outubro de 2026):** o Geyser avisa que, a partir de **27 de outubro**, os jogadores Bedrock só vão conseguir entrar se o suporte a **NetherNet** estiver ligado no Geyser. Veja o [aviso do Geyser](https://geysermc.org/blog/preparing-for-nethernet) e mantenha o Geyser atualizado.

---

← [Perguntas frequentes](Perguntas-Frequentes.md) · [Início](README.md)
