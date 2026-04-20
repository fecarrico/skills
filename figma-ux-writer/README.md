# Figma UX Writer - Skill de Revisão de Texto no Figma
 
Esta skill permite realizar auditorias de UX Writing diretamente em seus arquivos do Figma, utilizando as diretrizes oficiais da empresa. Ela identifica melhorias de tom de voz, clareza e padronização, sugerindo alterações através de anotações e permitindo a implementação automática.
 
## Como Usar
 
### 1. Iniciar uma Auditoria (Modo Híbrido: Visão + Nodes)
Basta enviar um link de um arquivo, página, seção ou frame do Figma:
 
> "Antigravity, revise o UX Writing deste link: [link]"
 
Eu irei:
- **Percepção Visual**: Capturar o print da seção ou frame para entender a semântica da UI (o que é título, botão, alerta, etc.).
- **Análise Contextual**: Identificar padrões de layout e hierarquia visual.
- **Auditoria Técnica**: Escanear os nodes de texto e comparar com o manual `references/ux_writing_manual.md`.
- **Sugestões Traceáveis**: Criar anotações no Figma com o prefixo `🤖 [UX-WRITER]`.
 
### 2. Aplicar Sugestões
Se você gostar das sugestões e quiser que eu as aplique de uma vez, diga:
 
> "Antigravity, pode implementar as mudanças sugeridas."
 
Eu irei:
- Substituir o texto original pela sugestão.
- Apagar a anotação correspondente para manter o arquivo limpo.
 
## Estrutura da Skill
- **SKILL.md**: Instruções lógicas da skill.
- **references/ux_writing_manual.md**: Manual de diretrizes convertido do original.
- **scripts/**: Espaço para scripts auxiliares de automação.
 
## Identificação Visual
As anotações criadas por esta skill são identificáveis pela tag `🤖 [UX-WRITER]`, garantindo que eu nunca altere anotações manuais feitas por designers ou writers humanos.

## Solução de Problemas
Se eu informar que não consigo acessar o Figma, verifique se o servidor MCP está ativo no seu terminal (ex: rodando o comando `bunx cursor-talk-to-figma-socket`).
