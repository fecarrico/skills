# Auditoria Comportamental: Fluxo de Contestação
**Status**: 🟢 Concluída | **Data**: 08/05/2026
**Analista**: Behavioral Design Agent (Skill: Heuristics Expert)

## 🎯 Contexto do Usuário
- **Persona**: Cliente Pessoa Física tentando entender suas cobranças.
- **Job-to-be-done**: "Entender minhas transações e contestar valores que parecem incorretos de forma simples e segura."
- **Principais Dores**: Incerteza sobre o motivo da cobrança e ansiedade no processo de prova (anexos).

---

## 🏗️ Análise da Jornada
A auditoria percorreu o fluxo completo, identificando pontos de fricção cognitiva e violações de acessibilidade.

### Tela 1: HOME - Finanças
Identificamos falhas de "Higiene de Interface" que minam a credibilidade.

**Achados Técnicos & Vieses:**
- **Violação da Lei de Fitts**: Botões de ação secundária ("Selecionar" e "Filtrar") possuem alvos de toque reduzidos (~41-42px). O padrão WCAG 2.2 exige no mínimo 44px para garantir usabilidade.
- **Consistência e Confiança**: O texto "dezembroembro" na fatura é um erro de digitação crítico. No contexto financeiro, erros gramaticais ativam o *Viés de Negatividade*, fazendo o usuário questionar se o cálculo do valor também está errado.

**Recomendação Estratégica**:
> Implementar um **"Resumo Amigável"** antes da lista de transações, destacando reembolsos ou descontos aplicados. Isso utiliza o *Viés de Confirmação* para mostrar que o Sem Parar também está "do lado do usuário".

---

### Tela 2: Detalhes da Cobrança
O usuário busca entender o porquê do valor.

**Achados Técnicos & Vieses:**
- **Peak-End Rule (Reforço Positivo)**: O destaque para "Valor promocional" é eficaz para reduzir a reatividade negativa.
- **Lei de Fitts (Acessibilidade)**: O link "Relatar problema nesta cobrança" está isolado no rodapé. Recomenda-se garantir que a área de toque seja de no mínimo 44x44px.

---

### Tela 3: Contestação (Motivos e Anexos)
O usuário entra no funil de **Ação e Esforço**.

**Achados Técnicos & Vieses:**
- **Inconsistência Grave (Miller's Law)**: O texto instrucional solicita arquivos de até **3 MB**, mas a mensagem de erro de sistema cita **10 MB**. Essa contradição gera dúvida e aumenta a carga cognitiva.
- **Efeito Zeigarnik**: A ausência de um stepper (ex: Passo 2 de 3) cria a percepção de um processo infinito.
- **Lei de Tesler (Complexidade)**: O processo de anexar documentos é o momento de maior atrito. Não há exemplos visuais do que seria um "comprovante válido".

**Recomendação Estratégica**:
> Padronizar os limites de upload (sugerido: 10MB) e adicionar uma barra de progresso. Alterar o copy de "Relatar problema" para **"Solicitar Revisão"**.

---

### Tela 4: Sucesso (Encerramento)
Momento de fechamento da tarefa.

**Achados Técnicos & Vieses:**
- **Gratificação Imediata**: O feedback visual verde é excelente para liberar dopamina e confirmar o sucesso.
- **Gestão de Expectativa**: O prazo de "2 dias úteis" é claro, mas o usuário fica com a carga de memorizar o protocolo.

**Recomendação Estratégica**:
> Adicionar um botão **"Copiar Protocolo"** ou **"Enviar por E-mail"** para reduzir o esforço de memorização.

---

## 📈 Impacto de Negócio Estimado
1. **Redução de Churn**: Ao facilitar a contestação, reduzimos a frustração do usuário.
2. **Eficiência Operacional**: Instruções claras sobre anexos diminuem a taxa de "documentos inválidos".
3. **Aumento de Trust Score**: A correção de erros de UI/Copy eleva a percepção de segurança.

---

*Relatório gerado automaticamente pelo Behavioral Design Agent.*
