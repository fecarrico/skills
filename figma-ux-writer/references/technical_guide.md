# Guia Técnico: Logística e Inventário (Figma UX Writer)

Este documento contém os padrões de execução técnica para garantir que o Antigravity consiga auditar 100% de uma jornada no Figma sem falhas de conexão ou memória.

## 📁 Caminhos de Arquivo
- **Inventário Temporário**: `/tmp/figma_audit_inventory.json`
- **Contexto de Auditoria**: `/tmp/current_audit_context.txt`

## 🛠️ Comandos de Crawler (Shell)

### Mapear Estrutura de Nível Inicial
Use este comando após rodar `mcp_TalkToFigma_read_my_design` ou similar para extrair os IDs de interesse do JSON gerado:
```bash
grep -oP '"id":"[^"]+","name":"[^"]+","type":"(SECTION|FRAME|COMPONENT|INSTANCE)"' [PATH_TO_JSON]
```

### Mapeamento de Textos por Node
Para extrair apenas o conteúdo textual de um node específico para análise:
```bash
grep -oP '"id":"[^"]+","name":"[^"]+","type":"TEXT","characters":"[^"]+"' [PATH_TO_JSON]
```

## 🔄 Lógica de Reconcliciação
Ao aplicar correções em massa:
1. **Listagem**: Use `get_annotations` para obter todas as anotações bot-signed (`🤖 [UX-WRITER]`).
2. **Regex de Extração**: Use o seguinte padrão para extrair o ID e a Sugestão de cada anotação:
   - ID: `\[TS-ID:(?<id>[^\]]+)\]`
   - Sugestão: `✅ \*\*Sugestão\*\*: "(?<suggestion>[^"]+)"`
3. **Validação**: Antes de aplicar, verifique se o Node ID ainda existe e se o texto original do node não foi alterado manualmente pelo designer após a análise.

## ⚠️ Tratamento de Erros de Conexão
Se o MCP retornar "timeout" ou "connection lost":
1. Não tente reconectar repetidamente no mesmo canal.
2. Peça ao usuário para abrir o plugin no Figma.
3. Solicite o novo **Channel ID** e use `join_channel` imediatamente.
4. Reinicie a exploração a partir do último ID salvo no log de inventário.
