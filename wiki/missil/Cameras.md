[Início](README.md) › Câmeras

# Câmeras de Segurança, Telas e Tablet (2.5.0)

## Câmera de Segurança

**Colocar.** Clique direito com a câmera numa face de um bloco sólido (parede, teto ou chão) que tenha espaço livre na frente. A lente aponta **para fora do bloco**, de volta para você. Cada jogador pode ter até 32.

**Ajustar.** Clique direito na câmera abre a tela dela:

- **Ver pela câmera**;
- **Renomear** (digite o nome no chat);
- **Campo de visão:** 60°, 90° ou 120°. É o cone que a câmera enxerga: quem estiver dentro dele (e à vista) ganha uma marca para quem vê e dispara o aviso;
- **Apontar para onde estou olhando** (a câmera passa a apontar na direção do seu olhar);
- **O que detecta:** jogadores inimigos, monstros e animais (cada um liga e desliga);
- **Tirar a câmera** (devolve o item). Agachado e batendo nela, o dono também recolhe.

**Ver.** Pelo **Tablet** (clique direito), por `/sam cameras` ou pelo menu **Câmeras** do `/sam`. Vendo:

- você começa olhando para onde a câmera aponta, e **a câmera acompanha o seu olhar** (os outros veem ela mexendo); ao sair, ela volta para onde estava;
- a câmera (corpo, lente e ponto vermelho) some para você, para não tapar a vista;
- clique esquerdo: próxima câmera; clique direito: anterior. A hotbar vira **Câmera anterior**, **Próxima câmera** e **Sair** (os seus itens voltam ao sair);
- **tudo** no campo de visão ganha uma marca que só você enxerga: vermelha em quem a câmera vigia, branca nos outros. A barra de cima mostra "campo 90° · 2 à vista".

**Detecção de movimento.** Com alguém a até 96 m, a câmera procura a cada meio segundo, no cone de visão, a até 32 m, com a linha de visada livre (a [fumaça](Ogivas-e-Minas.md) tapa). Quando aparece alguém novo:

- as [sirenes e Blocos de Ação](EMP-e-Alertas.md) ganham o alerta **Movimento na câmera**;
- você recebe no chat **[Ver câmera]**, que abre a câmera direto;
- a câmera tira uma **foto**.

No máximo um alerta a cada 10 s por câmera.

**Sem sinal:**

- mais longe que 500 m, só com [satélite](Satelite.md) (como os outros equipamentos);
- dentro de um bloqueador de radar inimigo;
- por 60 s depois de um [EMP](EMP-e-Alertas.md);
- destruída.

**Vida:** 30. Explosões, flechas e golpes de inimigos tiram vida; o [Kit de Reparo](Base.md#kit-de-reparo) conserta.

---

## Tela de Câmera

A Tela de Câmera é um mapa que mostra **ao vivo**, em baixa resolução, o que uma câmera ou um drone vê.

1. Ponha a Tela de Câmera numa moldura (item frame).
2. Com a [Ferramenta de Link](Comportas-e-Ferramenta-de-Link.md), clique **primeiro na tela**: abre o menu **Ligar tela**.
3. Escolha a fonte no menu (uma câmera sua, um drone de uma base ou um robô), ou feche e clique na câmera com a ferramenta.

A tela de um **drone** fica ligada à base e ao tipo (patrulha ou reconhecimento): ela mostra o drone desse tipo que estiver no ar, a cada voo, e "Drone na base" quando nenhum está voando.

**Tela grande:** quatro molduras com Tela, em quadrado, na mesma parede, viram uma tela 2×2 quando você liga uma delas.

- A imagem atualiza 2 vezes por segundo, só com alguém a até 24 m da moldura.
- Os blocos aparecem com a cor do mapa e sombra; as criaturas aparecem por cima: inimigos em vermelho, monstros em laranja, animais em verde.
- Sem sinal (veja acima) ou sem a fonte, a tela mostra chiado e "SEM SINAL".

---

## Fotos

`/sam cameras` → **Fotos** guarda as 10 últimas detecções. Clique numa foto para pegá-la como mapa; ela continua lá depois de o servidor reiniciar.

---

## Tablet

Clique direito com o Tablet abre a lista das suas câmeras, de onde você vê qualquer uma.

Receitas: [Câmera de Segurança, Tela de Câmera e Tablet](Receitas.md#base-e-câmeras-250).

---

← [Vida, contrabateria e depósito](Base.md) · Próximo: [Robôs](Robos.md) →
