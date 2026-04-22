# Guia de Heurísticas e Vieses Cognitivos — Especialista em Comportamento

Este guia contém as leis da psicologia aplicada ao UX Design, extraídas do TCC de Felipe Carrico, refinadas com critérios de detecção para auditorias de alta performance.

---

## 1. Leis da Atenção e Tempo de Resposta

*   **Lei de Fitts** (FITTS, 1954)
    *   **Explicação:** O tempo para atingir um alvo depende da distância e do tamanho do objeto.
    *   **🔍 Sinais de Alerta:** CTAs principais com altura < 44px (mobile), botões de "Continuar" no topo da tela (longe do polegar), ou links pequenos muito próximos uns dos outros.
*   **Lei de Hick-Hyman** (HICK, 1952; HYMAN, 1953)
    *   **Explicação:** O tempo de decisão aumenta conforme cresce a complexidade das opções.
    *   **🔍 Sinais de Alerta:** Menus com > 7 itens sem categorias, formulários com > 5 campos em uma única página, ou excesso de botões com o mesmo peso visual.
*   **Limiar de Doherty** (DOHERTY; SORRELL, 1982)
    *   **Explicação:** A interação é maximizada quando o feedback ocorre em menos de 400ms.
    *   **🔍 Sinais de Alerta:** Falta de skeleton screens em carregamentos, ausência de feedback visual imediato ao clicar em um botão, ou transições lentas.
*   **Teoria da Carga Cognitiva** (SWELLER, 1988)
    *   **Explicação:** Energia mental exigida para utilizar a tela.
    *   **🔍 Sinais de Alerta:** Uso excessivo de ícones sem labels, textos longos em blocos únicos, ou poluição visual com muitas cores vibrantes competindo.
*   **Lei de Miller** (MILLER, 1956)
    *   **Explicação:** Retenção de 7 (±2) unidades de informação.
    *   **🔍 Sinais de Alerta:** Listas longas sem agrupamento (chunking), códigos de verificação (OTP) sem separação por hífens, ou cabeçalhos com excesso de informações secundárias.
*   **Lei de Tesler** (TESLER, 1984)
    *   **Explicação:** Conservação da complexidade intrínseca do sistema.
    *   **🔍 Sinais de Alerta:** Usuário sendo forçado a tomar decisões técnicas (ex: escolher protocolos de rede) que deveriam ser automáticas.
*   **Lei de Parkinson** (PARKINSON, 1955)
    *   **Explicação:** Uma tarefa se alarga até preencher o prazo dado.
    *   **🔍 Sinais de Alerta:** Fluxos sem indicação de tempo estimado, ou ausência de reforço de urgência em processos de checkout.

---

## 2. Leis da Percepção Visual e Organização (Gestalt)

*   **Lei da Proximidade** (KOFFKA, 1935)
    *   **🔍 Sinais de Alerta:** Labels muito distantes dos seus campos de input, ou títulos de seção mais próximos da seção anterior do que da sua própria.
*   **Lei da Similaridade** (KOFFKA, 1935)
    *   **🔍 Sinais de Alerta:** Botões com funções diferentes (ex: "Excluir" e "Salvar") usando a mesma cor e forma, ou links que não se parecem com links.
*   **Lei da Região Comum** (PALMER, 1992)
    *   **🔍 Sinais de Alerta:** Itens semanticamente relacionados que não estão contidos em um card ou área sombreada, perdendo a conexão lógica.
*   **Lei da Conectividade Uniforme** (WERTHEIMER, 1923)
    *   **🔍 Sinais de Alerta:** Steppers (passo a passo) sem linhas conectoras, ou listas onde o item e sua ação não estão visualmente ligados.
*   **Lei da Prägnanz** (KOFFKA, 1935)
    *   **🔍 Sinais de Alerta:** Layouts assimétricos sem propósito, formas complexas para representar funções simples, ou falta de alinhamento em grids.
*   **Viés da Saliência** (CHABRIS; SIMONS, 1910)
    *   **🔍 Sinais de Alerta:** Ação primária da tela (ex: "Pagar") com menos destaque visual que uma ação secundária (ex: "Cancelar").
*   **Ilusão de Agrupamento** (TVERSKY; KAHNEMAN, 1971)
    *   **🔍 Sinais de Alerta:** Elementos aleatórios dispostos de forma que sugiram um padrão inexistente, confundindo o modelo mental.
*   **Lei da Legibilidade** (DYSON; HASSELL, 2004)
    *   **🔍 Sinais de Alerta:** Contraste texto/fundo < 4.5:1, fontes menores que 12pt, ou altura de linha (line-height) muito comprimida.
*   **Lei da Visibilidade** (NIELSEN, 1995)
    *   **🔍 Sinais de Alerta:** Itens essenciais (ex: carrinho, perfil) escondidos dentro de submenus desnecessários (hambúrguer no desktop).
*   **Navalha de Occam** (OCKHAM, séc. XIV)
    *   **🔍 Sinais de Alerta:** Funcionalidades que exigem 5 cliques quando poderiam ser resolvidas em 2, ou excesso de elementos decorativos que não auxiliam a tarefa.

---

## 3. Leis da Emoção e Estética

*   **Efeito da Usabilidade Estética** (KUROSU; KASHIMURA, 1995)
    *   **🔍 Sinais de Alerta:** Um design visualmente impecável que esconde erros graves de fluxo (ex: erro no botão de submit que o usuário perdoa por ser "bonito").
*   **Estado de Flow** (CSIKSZENTMIHALYI, 1990)
    *   **🔍 Sinais de Alerta:** Interrupções constantes (pop-ups, tooltips) em momentos de alta concentração (ex: preenchimento de dados bancários).
*   **Efeito Zeigarnik** (ZEIGARNIK, 1927)
    *   **🔍 Sinais de Alerta:** Barra de progresso estagnada, ou ausência de salvamento automático em formulários longos que desencoraja o retorno após pausa.
*   **Viés da Negatividade** (BAUMEISTER et al., 2001)
    *   **🔍 Sinais de Alerta:** Mensagens de erro com tom acusatório ou visual agressivo demais, que marcam a memória do usuário negativamente.
*   **Desconto Temporal** (AINSLIE, 1975)
    *   **🔍 Sinais de Alerta:** Pedir dados complexos no início do fluxo sem oferecer uma gratificação imediata (ex: valor do desconto) antes.

---

## 4. Leis da Memória e Decisão

*   **Lei de Jakob** (NIELSEN, 2000)
    *   **🔍 Sinais de Alerta:** Padrões de navegação não-convencionais (ex: scroll horizontal onde se espera vertical) que ignoram o hábito do usuário.
*   **Viés de Escassez** (WORCHEL et al., 1975)
    *   **🔍 Sinais de Alerta:** Ausência de indicadores de estoque ou tempo restante em ofertas, perdendo a chance de converter por urgência.
*   **Heurística da Disponibilidade** (TVERSKY; KAHNEMAN, 1973)
    *   **🔍 Sinais de Alerta:** Falta de exemplos de uso ou depoimentos recentes em momentos de dúvida do usuário.
*   **Regra do Pico-Fim** (KAHNEMAN; REDELMEIER, 1996)
    *   **🔍 Sinais de Alerta:** O momento final da jornada (ex: tela de sucesso) é frio e sem feedback positivo, ou o momento de maior dor (pagamento) é burocrático demais.
*   **Efeito Von Restorff** (VON RESTORFF, 1933)
    *   **🔍 Sinais de Alerta:** Uma lista de planos de assinatura onde o "Mais Popular" não tem nenhuma distinção visual das demais.
*   **Efeito da Posição Serial** (EBBINGHAUS, 1885)
    *   **🔍 Sinais de Alerta:** Informações cruciais (ex: preço, erro) colocadas no meio de um parágrafo longo ou lista extensa.
*   **Princípio de Pareto** (PARETO, 1896)
    *   **🔍 Sinais de Alerta:** As 3 ações mais usadas pelo usuário estão escondidas enquanto funções raramente acessadas ocupam o menu principal.
*   **Viés de Apoio à Escolha** (MATHER; JOHNSON, 2000)
    *   **🔍 Sinais de Alerta:** Falta de confirmação positiva após uma escolha difícil, deixando o usuário com "remorso do comprador".
*   **Efeito da Posse** (KAHNEMAN et al., 1991)
    *   **🔍 Sinais de Alerta:** Não permitir personalização (ex: foto de perfil, nome da conta) que criaria vínculo emocional e retenção.
*   **Viés de Ancoragem** (TVERSKY; KAHNEMAN, 1974)
    *   **🔍 Sinais de Alerta:** Exibir o preço final sem mostrar o preço original "de/por", perdendo a ancoragem de valor do desconto.

---

## 5. Leis do Comportamento Social e Expectativa

*   **Viés da Prova Social** (CIALDINI, 2001)
    *   **🔍 Sinais de Alerta:** Formulários de contratação sem indicação de quantos usuários já usam o serviço ("Junte-se a outros 5000...").
*   **Efeito da Mera Exposição** (ZAJONC, 1968)
    *   **🔍 Sinais de Alerta:** Mudanças bruscas de UI em funcionalidades core que quebram a familiaridade sem aviso prévio.
*   **Ilusão de Transparência** (GILOVICH; SAVITSKY, 1998)
    *   **🔍 Sinais de Alerta:** Ícones abstratos sem tooltip ou label, assumindo que o usuário entende o significado "óbvio" para o designer.
*   **Erro Fundamental de Atribuição** (ROSS, 1977)
    *   **🔍 Sinais de Alerta:** Mensagens de erro que dizem "Você digitou errado" em vez de "O formato deve ser DD/MM/AAAA".
*   **Design para Extremos** (BURGGRAAF, 2011)
    *   **🔍 Sinais de Alerta:** Ausência de atalhos de teclado para usuários pro, ou falta de explicações básicas para novos usuários.
*   **Ilusão de Controle** (LANGER, 1975)
    *   **🔍 Sinais de Alerta:** Processos automáticos demorados sem botão de "Atualizar" ou indicadores de que o usuário pode intervir.
