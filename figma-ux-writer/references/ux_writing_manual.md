# Manual de UX Writing — SuperApp Sem Parar

---

## O que é UX Writing

UX Writing é o design de conteúdo que integra diretamente a interface do aplicativo. Abrange botões, instruções, mensagens de erro, notificações e toda comunicação com o usuário, garantindo clareza, concisão e orientação para ação.

### Por que importa

**Para os usuários:**
- Facilita a navegação intuitiva
- Reduz erros e frustrações
- Aumenta o engajamento e a retenção
- Torna o uso mais agradável e eficiente
- Ajuda o usuário a alcançar seus objetivos com facilidade

**Para o negócio:**
- Fortalece a identidade da marca
- Garante tom e personalidade consistentes
- Aumenta conversões
- Torna a comunicação clara e estratégica
- Alinha a experiência aos objetivos do negócio

> "O conteúdo é a experiência do usuário"

### UX Writing vem junto com o design, não depois

Para ser eficaz, precisa ser desenvolvido junto com a interface. Essa integração:
- Cria um sistema único entre texto e visual
- Define hierarquia e sequência de ações
- Organiza melhor os elementos na tela
- Gera experiências mais eficazes para usuário e negócio

---

## Princípios de Escrita

### Geometria de conteúdo
A forma como o conteúdo é organizado importa:
- **Simplicidade**: escreva como as pessoas falam e elimine excessos
- **Consistência**: conexão entre o que foi dito e o que vem a seguir
- **Hierarquia**: o mais importante primeiro, o mais complexo depois

### Pilares
- Utilidade e orientação
- Usabilidade, semântica e arquitetura de informação

### Cognição, Consistência e Conversa
- **Cognição**: frases curtas, palavras comuns, sentimentos
- **Consistência**: padronização que gera confiança
- **Conversa**: organização pensando em ação e reação

---

## Componentes de Interface

### Header

O header está orientando a navegação, não titulando um artigo. Ele responde silenciosamente: *Onde estou? Em que etapa estou? O que posso fazer aqui?*

**Padrão recomendado:** Capitalização de sentença
- Apenas a primeira palavra em maiúscula
- Nomes próprios seguem a regra gramatical normal
- Sem ponto final

| ✅ Correto | ❌ Evitar |
|---|---|
| Histórico de pagamento | Histórico De Pagamento |
| Formas de pagamento | FORMAS DE PAGAMENTO |
| Detalhes do veículo | Detalhes Do Veículo |
| Resumo da contratação | Resumo Da Contratação |

**Por que capitalização de sentença:**
- Reduz carga cognitiva
- Melhora escaneabilidade
- Soa mais humano e acessível
- Padroniza com microcopy

---

### Título Principal

O título não é editorial nem botão. Funciona como instrução contextual, respondendo: *O que faço aqui? O que o app espera de mim?*

**Como escrever:**
- Use verbo no imperativo: fala direto com o usuário, reduz esforço cognitivo
- Use "seu/sua" para personalizar: soa menos autoritário
- Mantenha objetivo claro

| ✅ Correto | ❌ Evitar |
|---|---|
| Cadastre seu cartão para continuar | Cadastre o cartão para prosseguir |
| Escolha sua forma de pagamento | Escolha a forma de pagamento |

---

### Subtítulo

O subtítulo não é decorativo: é funcional. Responde: *O que acontece se eu fizer isso?*

**Função principal:**
- Explicar o que vai acontecer
- Antecipar o resultado
- Reduzir dúvidas e trazer contexto
- Reforçar segurança

**Como escrever:** Claro, curto, complementar (não repetitivo em relação ao título)

| ✅ Correto | ❌ Evitar |
|---|---|
| Título: "Pague agora" + Subtítulo: "Escolha como pagar e finalize em segundos" | Título: "Pague agora" + Subtítulo: "Faça o pagamento agora" |

**O que evitar:** Repetição, texto longo, informação irrelevante, linguagem técnica, misturar mensagens.

---

### CTA (Call to Action)

O CTA é a tradução da próxima ação. Responde: *O que acontece se eu clicar? Vale a pena clicar?*

**Tamanho ideal:** 1 a 3 palavras (máximo 4 se necessário)

**Estrutura:** Verbo + ação clara (preferencialmente no infinitivo)

| ✅ Usar | ❌ Evitar |
|---|---|
| Continuar | Próximo |
| Confirmar pagamento | Clique aqui para continuar |
| Cadastrar cartão | Prosseguir para a próxima etapa |
| Ver detalhes | OK |
| Concluir | Finalizar (genérico) |
| Agora não | Cancelar (ambíguo) |
| Excluir | Remover (quando for ação crítica) |

**Regra essencial:** O CTA deve repetir a ação do contexto.

Exemplo de consistência:
- Header: "Formas de pagamento"
- Texto: "Cadastre seu cartão para continuar"
- CTA: "Cadastrar cartão"

---

### Mensagens de Erro

#### Erro genérico/sistêmico
Falha interna do sistema — não depende do usuário, pode ocorrer em várias telas.

Exemplos:
- "Algo deu errado! Por favor, tente novamente"
- "Algo deu errado! Por favor, tente mais tarde"

#### Erro específico
O sistema sabe o que deu errado — ligado a uma ação do usuário, identificável e resolvível.

**Estrutura ideal:**
1. O que aconteceu
2. Onde aconteceu
3. Como resolver

Exemplo: "Não foi possível concluir o pagamento. Verifique os dados e tente novamente."

#### Erros em campos
- Devem ser curtos
- Focar no erro, não na explicação
- Estrutura: campo + problema + ação

Exemplo: "CPF inválido. Revise os números e tente novamente."

**Boas práticas gerais:**
- Não culpar o usuário ou a empresa
- Evitar linguagem técnica
- Sempre oferecer saída (botão de ação)

---

### Snackbars

Feedback rápido após uma ação — temporários, não interrompem o fluxo, mensagem curta.

**Boas práticas:**
- Linguagem neutra
- Apenas informação essencial
- **Usar ponto final**
- Sem exclamação ou exagero emocional

| ✅ Correto | ❌ Evitar |
|---|---|
| O cartão foi cancelado. | O cartão foi cancelado com sucesso! |
| Salvo com sucesso. | Ótimo! Arquivo salvo! |

---

### Alertas

Mensagens para situações críticas — chamam atenção, podem interromper o fluxo e indicam ação necessária.

---

### Botões (detalhes por intenção)

| Intenção | ✅ Usar | ❌ Evitar |
|---|---|---|
| Avançar fluxo | Continuar | Próximo |
| Voltar | Ir para o início | — |
| Finalizar ação | Concluir | Finalizar (genérico) |
| Confirmar decisão | Confirmar | OK |
| Cancelar / sair | Agora não | Cancelar (ambíguo) |
| Ação destrutiva | Excluir | Remover (quando crítico) |

**Boas práticas:**
- Evitar termos genéricos como "OK"
- O texto do botão deve antecipar o que acontece depois do clique
- Manter consistência ao longo do fluxo

---

### Campos de Formulário (Input)

Elementos de conteúdo em um campo:
- **Label**: nome claro e direto (ex: "CPF", "Data de nascimento")
- **Placeholder**: exemplo de preenchimento, não substitui o label (ex: "000.000.000-00")
- **Mensagem de erro**: campo + problema + ação (ex: "CPF inválido. Revise os números e tente novamente.")
- **Helper text**: explica quando necessário, antecipa dúvida (ex: "Use o mesmo CPF do titular da conta")

**Boas práticas:**
- Evitar repetir informação entre label e placeholder
- Priorizar clareza sobre brevidade em erros

---

## Repetição de Termos

A repetição intencional é baseada em psicologia cognitiva (Lei de Miller, Chunking, Gestalt).

**Quando repetir** — entre header e instrução:
- Header: "Voucher de abastecimento"
- Texto: "Defina o valor do seu voucher de abastecimento"

**Quando evitar** — na mesma frase ou entre título e subtítulo:

| ❌ Errado | ✅ Correto |
|---|---|
| Título: "Digite a senha do cartão" + Subtítulo: "Aqui você informa a senha do seu cartão" | Título: "Digite a senha do cartão" + Subtítulo: "Você tem 3 tentativas disponíveis" |

---

## Termos Preferenciais do Produto

| ✅ Usar | ❌ Evitar |
|---|---|
| SuperApp Sem Parar | Aplicativo, app |
| tag | adesivo, transponder |
| carro | veículo, automóvel |

---

## Convenções de Escrita

- **Datas**: abril (minúsculo, sem abreviação)
- **Horários**: 14h30 (sem espaço, sem "horas")
- **Números**: escrever por extenso até 9 (um, dois... nove), numeral a partir de 10
- **Pronomes**: "você", "seu/sua" — nunca tutear nem usar "vós"
- **Ponto final**: usar em snackbars e descrições; não usar em headers e CTAs

---

## Checklist de Padronização por Contexto

### Botões (CTAs)
- Avançar fluxo (Continuar vs Próximo)
- Voltar (ex: "Ir para o início")
- Cancelar / Sair
- Confirmar ação
- Finalizar ação (Concluir vs Finalizar)
- Ações destrutivas (Excluir, Cancelar serviço)
- Estados do botão (carregando, desabilitado)

### Navegação
- Títulos de tela (estrutura: ação vs substantivo)
- Nome de menus e categorias
- Tabs (abas)
- Padrão de uso de "seu/sua"

### Mensagens de Sistema
- Erro genérico (sistema indisponível)
- Erro específico (ex: pagamento recusado)
- Sucesso (ação concluída)
- Alertas (antes de uma ação crítica)
- Informativos (sem ação obrigatória)

### Estados de Interface
- Empty state (sem conteúdo)
- Sem resultados (busca/filtro)
- Loading (carregando)
- Erro dentro de componente (ex: lista quebrada)
- Primeiro acesso (sem histórico)

### Formulários
- Labels (nomes dos campos)
- Placeholders
- Mensagens de erro de campo
- Helper text (ajuda contextual)
- Máscaras e formatação (datas, CPF, etc.)

### Onboarding e Fluxos Guiados
- CTA principal (Continuar vs Próximo)
- Estrutura de título (benefício vs instrução)
- Descrições (curtas e escaneáveis)
- Indicadores de progresso (passo 1, 2, 3)
- Encerramento do fluxo

### Ações Críticas
- Confirmação de cancelamento
- Exclusão de conta/serviço
- Pagamentos
- Contratação de serviços

### Feedback Rápido (Microinterações)
- Toasts / snackbars
- Confirmações rápidas (ex: "Salvo com sucesso.")
- Feedback de ação instantânea

### Comunicação de Status
Padronizar tempo verbal, nível de clareza, e quando detalhar ou não:
- "Em análise"
- "Aprovado"
- "Recusado"
- "Processando"

### Permissões e Acessos
- Solicitação de permissão (notificação, localização)
- Explicação de por que pedir
- Estado negado (o que fazer)
