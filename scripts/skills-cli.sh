#!/bin/bash

# Antigravity Skills CLI - v1.3.0
# Setup e gerenciamento centralizado das Skills Figma.

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

STATE_FILE="$HOME/.figma-skills-state"

echo -e "${BLUE}=== Antigravity Skills CLI ===${NC}"

# ─────────────────────────────────────────
# Estado: leitura e escrita
# ─────────────────────────────────────────
read_state() {
    if [ -f "$STATE_FILE" ]; then
        # shellcheck source=/dev/null
        source "$STATE_FILE"
    fi
}

write_state() {
    cat > "$STATE_FILE" << EOF
SKILL_ENV_OK=true
SKILL_VERIFIED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SKILL_OS=$(uname -s)
EOF
    echo -e "${GREEN}[✓] Estado do ambiente salvo em: ${STATE_FILE}${NC}"
}

invalidate_state() {
    if [ -f "$STATE_FILE" ]; then
        rm "$STATE_FILE"
        echo -e "${YELLOW}[~] Cache de ambiente removido (${STATE_FILE}).${NC}"
    else
        echo -e "${YELLOW}[~] Nenhum cache encontrado. Nada a remover.${NC}"
    fi
}

# ─────────────────────────────────────────
# FASE 1: Detecção de OS
# ─────────────────────────────────────────
detect_os() {
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
}

# ─────────────────────────────────────────
# FASE 2: Verificação e Instalação do Bun
# ─────────────────────────────────────────
check_bun() {
    if command -v bun &> /dev/null; then
        echo -e "${GREEN}[✓] Bun já instalado: $(bun --version)${NC}"
        return 0
    fi

    echo -e "${YELLOW}[!] Bun não encontrado.${NC} Instalando..."
    curl -fsSL https://bun.sh/install | bash

    # Tenta ativar no shell atual
    BUN_ENV_FILE="$HOME/.bun/env"
    if [ -f "$BUN_ENV_FILE" ]; then
        # shellcheck source=/dev/null
        source "$BUN_ENV_FILE"
    else
        export PATH="$HOME/.bun/bin:$PATH"
    fi

    # Valida se bunx está acessível agora
    if ! command -v bunx &> /dev/null; then
        echo ""
        echo -e "${RED}╔══════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${RED}║  ⚠️  RESTART NECESSÁRIO                                      ║${NC}"
        echo -e "${RED}╠══════════════════════════════════════════════════════════════╣${NC}"
        echo -e "${RED}║  O Bun foi instalado, mas seu terminal precisa ser           ║${NC}"
        echo -e "${RED}║  reiniciado para reconhecer o novo PATH.                     ║${NC}"
        echo -e "${RED}║                                                              ║${NC}"
        echo -e "${RED}║  Após reiniciar, execute novamente:                          ║${NC}"
        echo -e "${RED}║    ./scripts/skills-cli.sh setup                             ║${NC}"
        echo -e "${RED}║                                                              ║${NC}"
        echo -e "${RED}║  Se estiver usando um agente AI, reinicie a sessão também.   ║${NC}"
        echo -e "${RED}╚══════════════════════════════════════════════════════════════╝${NC}"
        exit 0
    fi

    echo -e "${GREEN}[✓] Bun instalado com sucesso: $(bun --version)${NC}"
}

# ─────────────────────────────────────────
# FASE 3: Pré-aquecimento do MCP
# ─────────────────────────────────────────
check_figma_mcp() {
    echo -e "${BLUE}[*] Verificando pacote do MCP (cursor-talk-to-figma-mcp)...${NC}"
    if bunx cursor-talk-to-figma-mcp --help &> /dev/null; then
        echo -e "${GREEN}[✓] MCP pronto para uso.${NC}"
    else
        echo -e "${YELLOW}[~] Pacote MCP será baixado automaticamente na primeira execução.${NC}"
    fi
}

# ─────────────────────────────────────────
# FASE 4: Localizar o repositório de skills
# ─────────────────────────────────────────
setup_repo() {
    SKILLS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
    echo -e "${BLUE}[*] Repositório de skills localizado em: ${SKILLS_DIR}${NC}"
    echo -e "${GREEN}[✓] Pronto.${NC}"
}

# ─────────────────────────────────────────
# Comandos Principais
# ─────────────────────────────────────────
case "$1" in
    setup)
        # Verifica se já existe estado válido
        read_state
        if [ "$SKILL_ENV_OK" = "true" ]; then
            echo -e "${GREEN}[✓] Ambiente já configurado (cache em ${STATE_FILE}).${NC}"
            echo -e "${YELLOW}    Para forçar reconfiguração: $0 reset && $0 setup${NC}"
            exit 0
        fi

        echo -e "${BLUE}Iniciando Setup do Ambiente...${NC}"
        detect_os
        check_bun
        check_figma_mcp
        setup_repo
        write_state

        echo ""
        echo -e "${GREEN}=== AMBIENTE PRONTO! ===${NC}"
        echo ""
        echo -e "${BLUE}Próximos passos:${NC}"
        echo -e "  1. Configure o MCP no seu agente AI com o comando:"
        echo -e "     ${YELLOW}bunx cursor-talk-to-figma-mcp@latest${NC}"
        echo -e "  2. Reinicie o agente para ativar o MCP."
        echo -e "  3. No Figma, abra o plugin 'Talk to Figma' e copie o Channel ID."
        ;;

    update)
        echo -e "${BLUE}Verificando atualizações...${NC}"
        detect_os
        git pull
        check_bun
        check_figma_mcp
        write_state
        echo -e "${GREEN}[✓] Todas as skills estão atualizadas.${NC}"
        ;;

    reset)
        echo -e "${BLUE}Resetando cache do ambiente...${NC}"
        invalidate_state
        echo -e "${GREEN}[✓] Próxima execução de 'setup' realizará verificação completa.${NC}"
        ;;

    status)
        read_state
        echo ""
        if [ "$SKILL_ENV_OK" = "true" ]; then
            echo -e "${GREEN}  Estado:       ✅ Ambiente configurado${NC}"
            echo -e "  Verificado:   ${SKILL_VERIFIED_AT}"
            echo -e "  OS:           ${SKILL_OS}"
        else
            echo -e "${RED}  Estado:       ❌ Ambiente não configurado${NC}"
            echo -e "${YELLOW}  Execute: $0 setup${NC}"
        fi
        echo ""
        ;;

    *)
        echo ""
        echo "Uso: $0 {setup|update|reset|status}"
        echo ""
        echo "  setup   — Verifica OS, instala Bun, valida o MCP e salva o estado"
        echo "  update  — Atualiza o repositório e revalida dependências"
        echo "  reset   — Remove o cache (força verificação completa no próximo setup)"
        echo "  status  — Exibe o estado atual do ambiente"
        echo ""
        exit 1
        ;;
esac
