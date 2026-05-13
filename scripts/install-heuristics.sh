#!/bin/bash

# Figma Heuristics Skill Installer - v1.1.0
# Instalação isolada da skill de Heurísticas Nielsen & Vieses Cognitivos.

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Instalador: Figma Behavioral Expert ===${NC}"

# 1. Escolha do Caminho
echo -e "\nOnde você deseja instalar a Skill? (Pressione Enter para usar o diretório atual)"
read -p "Caminho [./figma-heuristics]: " TARGET_PATH
TARGET_PATH=${TARGET_PATH:-"./figma-heuristics"}

# 2. Criação do Diretório
mkdir -p "$TARGET_PATH"
cd "$TARGET_PATH" || exit

# 3. Download da Skill (Apenas a pasta de Heurísticas)
echo -e "${BLUE}[*] Baixando componentes da Skill de Heurísticas...${NC}"

# Estratégia: Se estivermos em um repo git, podemos usar sparse-checkout.
# Se for um download limpo, clonamos e limpamos.
if [ ! -d ".git" ]; then
    git clone --depth 1 --filter=blob:none --sparse https://github.com/fecarrico/skills.git . &> /dev/null
    git sparse-checkout set figma-behavioral-expert
    # Movemos o conteúdo para a raiz do TARGET_PATH para ficar mais limpo
    mv figma-behavioral-expert/* .
    rm -rf figma-behavioral-expert
fi

# 4. Verificação de Infra (Bun)
if ! command -v bun &> /dev/null; then
    echo -e "${RED}[!] Bun não encontrado.${NC} Instalando..."
    curl -fsSL https://bun.sh/install | bash
    export PATH="$HOME/.bun/bin:$PATH"
fi

# 5. Handshake com Figma MCP
echo -e "${BLUE}[*] Validando conexão com Figma MCP...${NC}"
bunx cursor-talk-to-figma-mcp --help &> /dev/null

echo -e "\n${GREEN}=== Instalação Concluída com Sucesso! ===${NC}"
echo -e "Diretório: ${BLUE}$(pwd)${NC}"
echo -e "\n${BLUE}Como ativar no seu ambiente:${NC}"
echo -e "1. No seu Agente (Cursor/Claude Desktop/Windsurf), adicione este diretório às 'Skills Paths'."
echo -e "2. Abra o Figma e inicie o plugin 'Talk to Figma'."
echo -e "3. Chame o agente: '@figma-behavioral-expert audite esta tela'."
