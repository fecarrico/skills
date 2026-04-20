---
name: figma-ux-writer
description: Analyze UX Writing in Figma designs using company guidelines. Suggests improvements via annotations and can automatically apply those changes. Trigger when the user mentions Figma UX review, text auditing in Figma, or "revisão de texto no Figma".
---
 
# Figma UX Writer Skill
 
A specialized skill for auditing and implementing UX Writing improvements directly in Figma files.
 
## Workflow
 
### 0. MCP Connection & Verified Handshake (Obrigatório)
Antes de qualquer análise, garanta que a ponte entre o Agente e o Figma está ativa e respondendo:

1. **Teste de Conectividade**: Execute `mcp_TalkToFigma_get_selection`.
2. **Procedimento de Handshake (Se falhar ou Timeout)**:
   - Se você tiver um Channel ID, execute `mcp_TalkToFigma_join_channel`.
   - **CRÍTICO**: O sucesso do `join_channel` apenas confirma que o servidor local está pronto. Você **DEVE** validar a conexão real executando `mcp_TalkToFigma_get_selection` novamente logo em seguida.
   - Somente reporte "Conectado" se receber uma resposta válida (mesmo que vazia) do Figma neste segundo teste.
3. **Tratamento de Erro de Plugin**:
   - Se o `get_selection` continuar falhando/timing out após o ingresso no canal, interrompa e informe:
     > ⚠️ **Figma Plugin Desconectado**: 
     > 1. Certifique-se de que o plugin "Cursor Talk to Figma" está aberto no Figma.
     > 2. No plugin, clique em "Join Channel" (ou verifique se o ID coincide).
     > 3. Se o problema persistir, reinicie o servidor MCP no menu de configurações do Cursor.
 
### 1. Identificação e Percepção Visual (Modo Híbrido)
Sempre comece pela percepção visual para entender o contexto antes de auditar os dados brutos:
 
- **Captura Hierárquica**: Use `mcp_TalkToFigma_export_node_as_image` (PNG, escala 2) com base no link fornecido.
- **Vision Protocol**: Analise a imagem para identificar tipo de tela, hierarquia e tom visual.
 
### 2. Auditoria Técnica e Extração de Dados
- **Tratamento de Containers e Modo Jornada**: Antes de qualquer auditoria técnica, valide o tipo do node.
  - **Se o node for `SECTION` (Modo Jornada)**:
    1. Use `mcp_TalkToFigma_get_node_info` para listar os filhos imediatos do container.
    2. Identifique todos os nodes do tipo `FRAME` (telas individuais da jornada).
    3. **Processamento em Batches**: Processe as telas em blocos de 3 telas por vez, de forma sequencial, sem interromper para perguntar ao usuário.
    4. Para cada tela: execute (Análise Visual -> Auditoria Técnica -> Sugestões -> Anotações).
    5. **Resumo Executivo (Final)**: Ao concluir a jornada, forneça um resumo direto e "sem firulas" contendo apenas os **principais apontamentos** e **pontos de atenção** críticos observados.
  - **Se o node for `GROUP` ou possuir dimensões massivas (> 2000px)**:
    1. **NÃO EXECUTAR** `scan_text_nodes` ou `export_node_as_image` diretamente no container.
    2. Refine a seleção para o `FRAME` de interesse contido no grupo antes de prosseguir.
- **Scan de Nodes**: No contexto do `FRAME` sendo auditado, use `mcp_TalkToFigma_scan_text_nodes` para obter o texto exato e o `nodeId`.
 
### 3. Aplicação do Manual de UX Writing
- Use `references/ux_writing_manual.md` como guia.
- Use termos preferidos: "SuperApp Sem Parar", "tag", "carro".
 
### 4. Geração de Anotações Traceáveis (Categorização)
Ao gerar anotações, use a lógica de **Aprovação/Reprovação**:
1. **Verificação de Categorias**: Execute `mcp_TalkToFigma_get_annotations(includeCategories: true)` no frame principal.
2. **Mapeamento de IDs**:
   - Se encontrar categorias com nome "Aprovar" ou "Reprovar", use seus respectivos `categoryId`.
   - Caso contrário, gere anotações usando prefixos visuais no `labelMarkdown`.
3. **Formato da Anotação**:
   Utilize o seguinte template para garantir legibilidade (incluindo quebras de linha e negrito):
   ```text
   🤖 [UX-WRITER] [APROVAR ou REPROVAR]

   **Sugestão:**
   "<Texto Sugerido>"

   **Motivo:**
   <Razão Técnica/UX>

   [TS-ID:<nodeId>]
   ```
 
### 5. Implementação Automática ("Apply Changes")
Se o usuário solicitar a aplicação das mudanças:
1. Filtre anotações com o prefixo `🤖 [UX-WRITER]`.
2. Extraia o `<Texto>` e o `<nodeId>` do `TS-ID`.
3. Use `mcp_TalkToFigma_set_text_content` para atualizar os textos.
4. Use `mcp_TalkToFigma_delete_node` para limpar as anotações.
 
---
 
## Communication Guidelines
- Use Portuguese (PT-BR) as the primary language.
- Sempre informe se a conexão foi bem-sucedida ou se houve algum problema de canal no início.
- Informe ao designer se as anotações foram criadas usando categorias nativas do Figma ou labels de texto.
