# Relatório de Auditoria Comportamental (UX/Psychology)
**Projeto:** Área de Protocolos — Detalhe de Lançamento
**Data:** 22 de Abril de 2026
**Status:** Auditado

---

## 1. Visão Geral da Jornada
A tela analisada representa o "momento da verdade" (Peak-End) de um fluxo de contestação financeira. O usuário chega aqui para resolver uma tensão (perda financeira) e espera uma resolução clara e definitiva.

### Objetivos do Usuário (JTBD):
- **Primário:** Saber se o dinheiro será devolvido (Resultado da Contestação).
- **Secundário:** Entender o porquê da decisão (Justificativa) e agir caso discorde (Recontestação).

---

## 2. Análise Técnica (Heurísticas e Vieses)

### 🚨 Viés da Saliência & Regra do Pico-Fim
O resultado da solicitação ("Aprovado") e o valor ressarcido possuem o mesmo peso visual que metadados técnicos (ex: número do protocolo). No final de uma jornada emocionalmente carregada, o cérebro busca por fechamento rápido.
- **Problema:** O usuário precisa ler uma lista técnica para encontrar a resposta que busca.
- **Impacto:** Aumento da carga cognitiva e sensação de frieza no atendimento.
- **Sugestão Estratégica:** Transformar o status em um **Card de Destaque** no topo da tela com cores semânticas.

### 🧠 Teoria da Carga Cognitiva
A tela apresenta uma estrutura de "formulário preenchido" com muitos campos de texto. 
- **Problema:** A visualização dos detalhes da transação (Mapa, Local, Carro) ocupa muito espaço vertical, "empurrando" a justificativa e os botões de ação para fora da primeira dobra (fold).
- **Sugestão Estratégica:** Utilizar **Progressive Disclosure** (acordeões) para o "Resumo da Solicitação", mantendo o foco inicial apenas no Resultado e na Explicação.

### ⚠️ Viés da Negatividade & Incerteza
A maior dor relatada pelo usuário é a incerteza sobre a justificativa em casos negativos.
- **Problema:** O campo "Explicação do resultado" é apenas um texto simples. Em casos de negativa, se o texto for curto ou puramente técnico, ele ativa o viés da negatividade, gerando desconfiança e frustração.
- **Sugestão Estratégica:** Estruturar a explicação em "passos" ou "critérios analisados". Se for negativo, oferecer imediatamente o botão de "Reabrir Protocolo" como uma **Rampa de Recuperação**, e não como um botão fantasma escondido no rodapé.

### 📐 Lei de Fitts (Acessibilidade e Decisão)
O botão "Reabrir protocolo" é um *Ghost Button* abaixo do botão principal "Voltar".
- **Problema:** Para um usuário insatisfeito, a reabertura é a tarefa principal. O design atual dificulta a interação e dá menos importância a essa ação crítica.
- **Sugestão Estratégica:** Inverter a hierarquia se o resultado for negativo. O botão de reabertura deve ser o CTA principal (Solid) e o "Voltar" o secundário.

---

## 3. Ficha Técnica de Achados

| Heurística / Viés | Severidade | Achado | Sugestão |
| :--- | :---: | :--- | :--- |
| **Pico-Fim** | 🟠 Média | Finalização da jornada sem reforço visual do sucesso/falha. | Criar badge de status proeminente. |
| **Saliência** | 🔴 Alta | Valor ressarcido diluído no meio de IDs técnicos. | Destacar o valor `R$ 70,00` em fonte maior. |
| **Lei de Fitts** | 🟠 Média | Botão de reabertura com pouco peso visual e difícil alcance. | Tornar o botão de reabertura dinâmico (Primário em caso de erro). |
| **Carga Cognitiva** | 🟡 Baixa | Excesso de informação transacional desnecessária no momento do resultado. | Colapsar detalhes da transação original. |

---

## 4. Próximos Passos Recomendados

1. **Testar Versão "Negative Case":** Validar se o tom de voz da explicação reduz a taxa de reabertura desnecessária.
2. **Hierarquia Dinâmica:** Implementar lógica de UI que altera os botões de ação com base no status (`Aprovado` vs `Reprovado`).
3. **Feedback Visual Imediato:** Garantir que o valor ressarcido seja a primeira coisa que o usuário vê ao abrir a tela.

---
*Relatório gerado por Figma Behavioral Expert Agent v1.3*
