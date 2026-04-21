#!/bin/bash

# Script para automatizar a conexão entre Cursor e Figma
# 1. Detecta o bunx automaticamente no sistema
# 2. Verifica se o Socket Bridge já está rodando (Porta 3055)
# 3. Inicia o Socket Bridge em background se necessário
# 4. Inicia o Servidor MCP

PORT=3055

# Detecta o executável bunx automaticamente (portável entre máquinas)
BUNX=$(which bunx 2>/dev/null || echo "${HOME}/.bun/bin/bunx")

if [ ! -f "$BUNX" ] && ! command -v bunx &>/dev/null; then
  echo "[Figma Connection] ❌ ERRO: bunx não encontrado." >&2
  echo "[Figma Connection] Instale o Bun em: https://bun.sh" >&2
  exit 1
fi

# Verifica se a porta está em uso (o que indica que o socket bridge já está rodando)
if ! lsof -i :$PORT | grep LISTEN > /dev/null 2>&1; then
    echo "[Figma Connection] Iniciando Socket Bridge na porta $PORT..." >&2
    "$BUNX" cursor-talk-to-figma-socket > /dev/null 2>&1 &

    # Aguarda um momento para estabilização
    sleep 2
else
    echo "[Figma Connection] Socket Bridge já está rodando na porta $PORT." >&2
fi

# Inicia o Servidor MCP (foreground para comunicação via stdio)
echo "[Figma Connection] Iniciando Servidor MCP..." >&2
echo "[Figma Connection] 💡 DICA: O bridge local está ON, mas a conexão real depende do Plugin estar aberto no Figma e com o Channel ID correto." >&2
"$BUNX" cursor-talk-to-figma-mcp@latest
