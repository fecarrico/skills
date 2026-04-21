---
name: sample-skill-name
description: [O QUE FAZ] + [QUANDO USAR] + [CAPACIDADES]. Ex: Analisa erros de deploy e sugere correções. Use quando o usuário encontrar erros de pipeline, 'build failed' ou pedir 'debug deploy'. Suporta AWS, GitHub Actions e Jenkins.
metadata:
  version: 1.0.0
  author: [Seu Nome]
---

# Nome da Skill

Breve visão geral do valor que esta skill entrega. Foco no "Outcome" (Resultado final).

## 🚀 Workflows Principais

### Fluxo 1: [Nome do Cenário Principal]
1. **Passo 1**: [Ação] - Chamar ferramenta MCP `exemplo_tool`.
2. **Passo 2**: [Ação] - Validar saída usando `scripts/validator.py`.
3. **Passo 3**: [Ação] - Gerar relatório final.

### Fluxo 2: [Nome do Cenário Secundário]
...

## 🛡️ Regras de Qualidade e Segurança

- **Validação**: Sempre verifique [Critério X] antes de prosseguir para o passo [Y].
- **Segurança**: Nunca exponha [Dados Sensíveis].
- **Tratamento de Erros**: Se a ferramenta `mcp_tool` falhar, tente [Estratégia de Retry] antes de reportar ao usuário.

## 📚 Referências

- Guia de Estilo: [link para references/style_guide.md]
- Exemplos de Saída: [link para references/examples.md]

---
*Esta skill segue o padrão Anthropic de Progressive Disclosure.*
