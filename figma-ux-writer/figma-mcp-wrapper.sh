#!/bin/bash

# Identifica o diretório do usuário de forma dinâmica
USER_HOME="$HOME"

# Procura pelo bunx em locais comuns
BUNX_BIN="$USER_HOME/.bun/bin/bunx"
if [ ! -x "$BUNX_BIN" ]; then
    BUNX_BIN=$(command -v bunx)
fi

# Se não encontrar o bunx, tenta rodar via npx como fallback
if [ -z "$BUNX_BIN" ]; then
    BUNX_BIN=$(command -v npx)
fi

# Configuração específica para Linux (correção do erro de crypto)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Locais comuns do NVM
    NVM_PATHS=(
        "$USER_HOME/.config/nvm/nvm.sh"
        "$USER_HOME/.nvm/nvm.sh"
    )
    
    for NVM_SH in "${NVM_PATHS[@]}"; do
        if [ -f "$NVM_SH" ]; then
            source "$NVM_SH"
            # Tenta usar a versão default que configuramos (v24)
            nvm use default >/dev/null 2>&1
            break
        fi
    done
fi

# Executa o servidor MCP com todos os argumentos originais
exec "$BUNX_BIN" cursor-talk-to-figma-mcp@latest "$@"
