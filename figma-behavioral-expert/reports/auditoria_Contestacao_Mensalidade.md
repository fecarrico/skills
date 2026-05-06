# Relatório Estratégico Visual: Contestação de Mensalidade

**Data da Auditoria:** 29 de Abril de 2026
**Persona/Usuário Final:** Usuários do App Sem Parar
**Objetivo Principal (JTBD):** Compreender e acompanhar o processo de contestação de uma cobrança de mensalidade.
**Dor Principal Mapeada:** Dificuldade no entendimento do processo, especificamente relacionada à interpretação dos "status do sistema".

---

## 🧠 1. Diagnóstico Geral de Comportamento
A jornada atual de Contestação de Mensalidade falha em gerenciar a expectativa do usuário (Ilusão de Transparência) e não fecha os ciclos psicológicos de ansiedade, resultando no Efeito Zeigarnik. O usuário abre uma contestação e recebe um status passivo ("Problema relatado") sem indicativos claros de SLA (prazo) ou próximos passos, o que muito provavelmente aumenta o volume de chamados no Call Center.

## 🔎 2. Análise Técnica e Violações Heurísticas (Tela: HOME - Finanças)

### Achado 1: Status Passivo e Ansiedade do Usuário
- **Elemento Analisado:** Tag de status "Problema relatado"
- **Violação:** Ilusão de Transparência (Gilovich; Savitsky, 1998) & Efeito Zeigarnik (Zeigarnik, 1927)
- **Impacto de Negócio:** Alto. A incerteza gera ansiedade, levando o usuário a tentar outros canais de contato (WhatsApp, Call Center, ReclameAqui) para buscar o "status real" da sua demanda.
- **Estratégia de Correção:** Transformar o status de uma observação passiva para uma comunicação ativa.
  * *Recomendação Técnica:* Substituir "Problema relatado" por "Em análise (Prazo: X dias)" ou incluir um CTA "Acompanhar contestação". Isso fecha o ciclo de ansiedade ao definir uma expectativa clara.

### Achado 2: Oportunidade Perdida na Devolução (Pico Emocional)
- **Elemento Analisado:** Tag de status "Reembolsada" e "Reembolso parcial"
- **Oportunidade:** Regra do Pico-Fim (Kahneman; Redelmeier, 1996)
- **Impacto de Negócio:** Médio. A jornada termina de forma "fria". O estorno do dinheiro é o momento de maior alívio emocional do cliente.
- **Estratégia de Correção:** O design não deve tratar o reembolso apenas como uma mudança de status sistêmico, mas como uma *vitória* do cliente. 
  * *Recomendação Técnica:* Evidenciar visualmente a resolução a favor do usuário (ex: ícones comemorativos, cores mais vibrantes ou uma micro-interação de sucesso), garantindo que a "memória residual" do usuário em relação ao Sem Parar seja altamente positiva, minimizando o atrito inicial do erro na mensalidade.

### Achado 3: Competição Visual de Status
- **Elemento Analisado:** Lista de transações com múltiplos status concorrentes
- **Violação:** Lei de Hick-Hyman (Hick, 1952)
- **Impacto de Negócio:** Baixo/Médio. Sobrecarga cognitiva ao ler a fatura.
- **Estratégia de Correção:** Os itens que requerem ação ou que estão pendentes (em análise) deveriam ter precedência ou destaque visual diferente dos que já estão resolvidos (Reembolsado), facilitando a varredura visual.

---

## 🔎 3. Análise Heurística Profunda (Novas Telas Mapeadas)

### Achado 4: Carga Cognitiva e Fricção no Funil de Motivos
- **Elemento Analisado:** Lista de seleção de motivos (Tela: Motivos)
- **Violação:** Lei de Hick (Hick, 1952) & Fricção de Lembrança
- **Impacto de Negócio:** Alto. A presença de categorias quase sobrepostas ("Valor incorreto" vs "Cobrança indevida") seguida de submotivos que exigem que o usuário lembre do seu estado sistêmico (ex: "Meu plano estava pausado") aumenta o esforço mental e as chances de abandono ou de acionar o SAC.
- **Estratégia de Correção:** 
  * *Recomendação Técnica:* Utilize a automação para poupar esforço (ex: se o sistema sabe que a tag foi cancelada, pré-selecione a opção ou oculte as não relacionadas). Utilize o "Efeito Padrão" destacando os 2 motivos mais comuns e apoie a diferenciação com iconografia.

### Achado 5: Aversão à Perda em Avisos de Cobrança
- **Elemento Analisado:** Mensagem "A partir de 02/02 a mensalidade passará a ser R$ 65,00" (Tela: Detalhe de Lançamento)
- **Violação:** Aversão à Perda (Kahneman; Tversky, 1979) e Efeito Punição
- **Impacto de Negócio:** Alto. O tom puramente punitivo e focado na cobrança futura amplifica a ansiedade, fazendo com que a jornada pareça uma advertência ao invés de um detalhamento transparente.
- **Estratégia de Correção:** 
  * *Recomendação Técnica:* Utilize o viés da **Ancoragem Positiva**. Reforce o benefício que o usuário teve até o momento ("Você economizou R$ X com esta promoção! Aproveite até 02/02") antes de introduzir o novo valor de R$ 65,00.

---

## 🎯 4. Próximos Passos e Recomendações (Action Items)

Para evoluir a maturidade desta jornada incompleta:
1. **Mapeamento de SLA:** Levantar junto ao time de Negócios/Operações os prazos reais de análise para refinar os textos de status.
2. **Tela de Detalhe:** Criar uma tela de detalhamento ("Acompanhar contestação") que exiba a linha do tempo do chamado (Recebido -> Em Análise -> Resolvido).
3. **Revisão Visual:** Aplicar as correções recomendadas diretamente nos componentes de Tag do Design System.

*Nota: As violações técnicas já foram documentadas diretamente nas células correspondentes no arquivo Figma através de anotações automatizadas.*
