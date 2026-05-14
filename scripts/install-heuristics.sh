#!/bin/bash

# Figma Heuristics Skill Installer - v1.2.0
# Instalação isolada da skill: Figma Behavioral Expert (Heurísticas Nielsen + Vieses Cognitivos)

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}=== Instalador: Figma Behavioral Expert ===${NC}"

# ─────────────────────────────────────────
# FASE 1: Detecção de OS
# ─────────────────────────────────────────
OS_TYPE="$(uname -s 2>/dev/null || echo 'unknown')"

case "$OS_TYPE" in
    Darwin)  OS_NAME="macOS" ;;
    Linux)   OS_NAME="Linux / WSL" ;;
    CYGWIN*|MINGW*|MSYS*) OS_NAME="Windows (Git Bash)" ;;
    *)
        echo -e "${RED}[!] Sistema operacional não suportado: $OS_TYPE${NC}"
        echo -e "${YELLOW}    Se estiver no Windows, use o WSL 2 (Ubuntu) e tente novamente.${NC}"
        exit 1
        ;;
esac

echo -e "${GREEN}[✓] Sistema detectado: ${OS_NAME}${NC}"

# ─────────────────────────────────────────
# FASE 2: Escolha do Diretório de Instalação
# ─────────────────────────────────────────
echo -e "\nOnde você deseja instalar a Skill? (Pressione Enter para usar o diretório atual)"
read -r -p "Caminho [./figma-heuristics]: " TARGET_PATH
TARGET_PATH=${TARGET_PATH:-"./figma-heuristics"}

mkdir -p "$TARGET_PATH"
cd "$TARGET_PATH" || exit 1

# ─────────────────────────────────────────
# FASE 3: Download da Skill
# ─────────────────────────────────────────
echo -e "${BLUE}[*] Baixando componentes da Skill de Heurísticas...${NC}"

if [ ! -d ".git" ]; then
    git clone --depth 1 --filter=blob:none --sparse https://github.com/fecarrico/skills.git . &> /dev/null
    git sparse-checkout set figma-behavioral-expert
    mv figma-behavioral-expert/* .
    rm -rf figma-behavioral-expert
    echo -e "${GREEN}[✓] Skill baixada com sucesso.${NC}"
else
    echo -e "${GREEN}[✓] Repositório já existente — pulando clone.${NC}"
fi

# ─────────────────────────────────────────
# FASE 4: Verificação e Instalação do Bun
# ─────────────────────────────────────────
BUN_INSTALLED_NOW=false

if ! command -v bun &> /dev/null; then
    echo -e "${YELLOW}[!] Bun não encontrado.${NC} Instalando..."
    curl -fsSL https://bun.sh/install | bash

    # Tenta ativar o bun no shell atual sem precisar reiniciar
    BUN_ENV_FILE="$HOME/.bun/env"
    if [ -f "$BUN_ENV_FILE" ]; then
        # shellcheck source=/dev/null
        source "$BUN_ENV_FILE"
    else
        export PATH="$HOME/.bun/bin:$PATH"
    fi

    BUN_INSTALLED_NOW=true
fi

# Valida se bunx está acessível AGORA
if ! command -v bunx &> /dev/null; then
    echo ""
    echo -e "${RED}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║  ⚠️  RESTART NECESSÁRIO                                      ║${NC}"
    echo -e "${RED}╠══════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${RED}║  O Bun foi instalado, mas seu terminal precisa ser           ║${NC}"
    echo -e "${RED}║  reiniciado para reconhecer o novo PATH.                     ║${NC}"
    echo -e "${RED}║                                                              ║${NC}"
    echo -e "${RED}║  1. Feche e reabra o terminal (ou a sessão do agente AI).    ║${NC}"
    echo -e "${RED}║  2. Navegue novamente até este diretório:                    ║${NC}"
    echo -e "${RED}║     cd $(pwd)${NC}"
    echo -e "${RED}║  3. Conclua a configuração do MCP no seu agente AI.          ║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════════════╝${NC}"
    exit 0
fi

echo -e "${GREEN}[✓] Bun disponível: $(bunx --version 2>/dev/null || bun --version)${NC}"

# ─────────────────────────────────────────
# FASE 5: Pré-aquecimento do MCP (cache)
# ─────────────────────────────────────────
echo -e "${BLUE}[*] Validando pacote do MCP (cursor-talk-to-figma-mcp)...${NC}"
if bunx cursor-talk-to-figma-mcp --help &> /dev/null; then
    echo -e "${GREEN}[✓] MCP pronto para uso.${NC}"
else
    echo -e "${YELLOW}[~] Pacote MCP será baixado automaticamente na primeira execução pelo agente.${NC}"
fi

# ─────────────────────────────────────────
# Resumo Final
# ─────────────────────────────────────────
echo ""
echo -e "${GREEN}=== Instalação Concluída! ===${NC}"
echo -e "Diretório: ${BLUE}$(pwd)${NC}"
echo ""
echo -e "${BLUE}Próximos passos:${NC}"
echo -e "  1. No seu agente AI (Antigravity, Cursor, Windsurf, Claude Desktop),"
echo -e "     configure o servidor MCP com o comando:"
echo -e "     ${YELLOW}bunx cursor-talk-to-figma-mcp@latest${NC}"
echo -e "  2. Reinicie o agente para ativar o MCP."
echo -e "  3. Abra o Figma e inicie o plugin 'Talk to Figma'."
echo -e "  4. Chame o agente: ${YELLOW}@figma-behavioral-expert audite esta jornada${NC}"
