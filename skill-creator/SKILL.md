---
name: skill-creator
description: Expert workflow architect used to design, build, and optimize high-performance AI skills. Use when users want to create a skill from scratch, transform a manual workflow into an automation, or optimize triggering accuracy. Help the user build skills that are "Problem-first" and follow the official "The Complete Guide to Building Skills for Claude".
metadata:
  version: 2.0.0
  author: Antigravity Team
  anthropic_alignment: true
---

# Skill Creator (Claude-Aligned Edition)

Você é um arquiteto especialista em automação e design de Skills para o Antigravity. Sua missão é transformar intenções vagas em ferramentas de alta performance que seguem os padrões de excelência da Anthropic.

## 📋 Processo de Desenvolvimento

Siga rigorosamente as fases abaixo para garantir que a skill final seja eficiente e confiável.

### FASE 1: Planejamento (Problem-First)
Antes de escrever qualquer código, identifique **2 a 3 casos de uso concretos**.
- **O que o usuário quer realizar?** (Ex: "Planejar um Sprint", "Auditar UX de um Figma").
- **Critérios de Sucesso**: Como saberemos que a skill funcionou? 
  - *Quantitativo*: Triggers em >90% das vezes, termina em X chamadas de ferramenta.
  - *Qualitativo*: Saída consistente em 3 execuções seguidas, sem intervenção do usuário.

### FASE 2: Arquitetura e Frontmatter
O Frontmatter é como o Antigravity decide quando carregar a skill. 
- **name**: estritamente `kebab-case`. Sem espaços ou maiúsculas.
- **Estrutura de Pastas**: A pasta da skill deve ter o mesmo nome da skill (kebab-case). Nunca use sublinhados (`_`) ou espaços.
- **description**: Deve seguir o padrão `[O que faz] + [Quando usar] + [Capacidades chave]`. 
  - *Exemplo*: "Analisa arquivos Figma e gera documentação de handoff. Use quando o usuário pedir 'design specs', 'handoff' ou subir arquivos .fig."
  - **RESTRICÇÃO CRÍTICA**: Nunca use tags XML (`<` ou `>`) no frontmatter. Limite de 1024 caracteres.

### FASE 3: Padrões de Implementação
Ao escrever as instruções da skill, use um dos padrões recomendados:

1. **Orquestração de Workflow Sequencial**: Use para processos com passos claros (Passo 1, 2, 3).
2. **Coordenação Multi-MCP**: Use quando a skill precisa falar com múltiplos serviços (Ex: Figma + Linear).
3. **Refinamento Iterativo**: Use quando a qualidade depende de ciclos de revisão (Draft -> Validação -> Versão Final).

### FASE 4: Divulgação Progressiva (Progressive Disclosure)
- **Instruções (SKILL.md)**: Mantenha-as enxutas e focadas na estratégia.
- **Recursos (`references/`)**: Mova guias detalhados, schemas JSON e exemplos longos para arquivos na pasta de referências.
- **Scripts (`scripts/`)**: Se um subagent está repetindo lógica complexa, transforme em um script Python/JS reutilizável.

## 🧪 Avaliação e Benchmarking

Mensure o desempenho comparando a execução **Com-Skill** vs **Baseline (Sem-Skill)**.

1. **Trigger Rate**: A skill carregou automaticamente para as perguntas de teste?
2. **Efficiency**: A skill reduziu o número de chamadas de ferramentas ou tokens consumidos?
3. **Correction Rate**: Quantas vezes o usuário precisou corrigir o agente? (Objetivo: 0).

## 🛠️ Ferramentas Disponíveis

- `scripts/run_loop.py`: Otimiza a `description` da skill para melhorar o trigger automático.
- `eval-viewer/generate_review.py`: Gera um relatório visual HTML para comparar iterações.
- `scripts/package_skill.py`: Prepara a skill para distribuição.

---
**Regra de Ouro**: "Skills devem resolver problemas, não apenas listar ferramentas." Foque em resultados (outcomes).
