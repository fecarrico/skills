# 📊 Auditoria Comportamental: Contestação de Mensalidade

**Data:** 06 de Maio de 2026
**Score Behavioral:** 🟡 6.5/10 (Atenção Moderada)

---

## 📌 Resumo Executivo

A jornada de Contestação de Mensalidade possui uma estrutura visual limpa, mas peca em **transparência de sistema** e **visibilidade de ações críticas**. O usuário que entra com a intenção clara de contestar precisa lidar com alta carga cognitiva para encontrar a opção de reporte e enfrenta inconsistências na navegação ao longo do fluxo.

| Lei / Viés | Severidade | Tela Afetada | Impacto no Usuário |
| :--- | :--- | :--- | :--- |
| **Lei da Visibilidade** | Alta | HOME - Finanças | Dúvida sobre o status real das contestações e necessidade de ação. |
| **Viés da Saliência** | Alta | Detalhe de lançamento | Dificuldade extrema em encontrar o fluxo de contestação. |
| **Lei de Hick-Hyman** | Média | Motivos | Aumento do tempo de decisão e incerteza na escolha. |
| **Lei de Jakob** | Média | Contestação (Recebimento) | Quebra de expectativa no padrão de avanço de tela. |

---

## 🔎 Análise de Jornada (Passo a Passo)

### 1. HOME - Finanças
![HOME - Finanças](assets/4059-16588.png)

**A Experiência:** O usuário acessa sua lista de transações buscando entender as cobranças. Ele se depara com um extrato extenso onde cobranças normais e contestações em andamento estão misturadas na mesma timeline.

**Pontos de Atenção:**
- **Lei da Visibilidade & Ilusão de Transparência:** As tags ("Problema em análise", "Reembolsado realizado") assumem que o usuário entende o processo. Faltam calls-to-action claros caso o usuário precise enviar mais dados, e não há indicação de prazo (*Fonte: NIELSEN, 1995*).
- **Lei de Miller:** A falta de agrupamento (ex: separar "Transações do Mês" de "Acompanhamento de Protocolos") sobrecarrega a memória de trabalho do usuário durante o escaneamento (*Fonte: MILLER, 1956*).

### 2. Detalhes da Transação
![Detalhe de lançamento](assets/4059-19545.png)

**A Experiência:** Ao abrir uma mensalidade não reconhecida, o usuário busca instintivamente por um botão de ajuda ou contestação. O fluxo o obriga a ler todos os detalhes promocionais até o final da tela para encontrar o link.

**Pontos de Atenção:**
- **Viés da Saliência & Lei de Fitts:** O link "Relatar problema nesta cobrança" atua como a ação principal (job-to-be-done) desta jornada, mas possui baixíssimo contraste e pequena área de clique. Isso eleva a ansiedade e as chances de o usuário abandonar o app e ligar para o Call Center (*Fonte: CHABRIS; SIMONS, 1910; FITTS, 1954*).

### 3. Seleção de Motivos
![Motivos](assets/4067-22790.png)

**A Experiência:** O usuário encontra a área de contestação e precisa classificar seu problema. A lista de opções exige leitura atenta. Ele clica em uma opção e a tela avança instantaneamente.

**Pontos de Atenção:**
- **Lei de Hick-Hyman:** As descrições longas e com significados próximos ("Cobrança indevida" x "Condições não respeitadas") geram atrito cognitivo (*Fonte: HICK, 1952*).
- **Prevenção de Erros:** O avanço imediato ao tocar em um card de motivo impede que o usuário revise sua escolha, podendo gerar preenchimentos errôneos do protocolo (*Fonte: NIELSEN, 1995*).

### 4. Definição de Recebimento
![Contestação](assets/4094-7633.png)

**A Experiência:** Na etapa final, o usuário escolhe como quer receber o estorno. Diferente da tela anterior, aqui ele precisa selecionar a opção e depois clicar em "Continuar". Após finalizar, ele não sabe quando o dinheiro cai.

**Pontos de Atenção:**
- **Lei de Jakob (Consistência):** A mudança brusca do modelo de interação (clique avança na tela anterior vs. clique no botão "Continuar" nesta tela) quebra o padrão de navegação interno (*Fonte: NIELSEN, 2000*).
- **Ilusão de Controle & Desconto Temporal:** Não há indicação de prazo de resposta para a revisão do pedido ou SLA de estorno, removendo a previsibilidade do usuário (*Fonte: LANGER, 1975*).

---

## 🚀 Conclusão e Próximos Passos

A jornada tem potencial para ser self-service e reduzir drasticamente as ligações de contestação, mas precisa de ajustes na sua hierarquia e arquitetura de informação:

1. **Destacar a Ação de Contestação:** Transformar o link "Relatar problema" da tela de Detalhes em um botão secundário (`Ghost` ou `Outline`) bem posicionado, aumentando a saliência.
2. **Central de Acompanhamento:** Separar ou agrupar os itens em disputa na HOME para reduzir a carga cognitiva, tornando as tags de status clicáveis para abrir um "modal de andamento" com prazos claros.
3. **Padronizar a Interação de Listas:** Definir se listas de escolha avançam sozinhas ou se exigem confirmação (recomendado exigir confirmação em fluxos de erro/contestação para prevenir cliques acidentais).
4. **Gerenciar Expectativas:** Incluir um microcopy na tela final (e nas tags) informando o SLA médio de devolução e análise.
