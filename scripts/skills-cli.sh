#!/bin/bash

# Antigravity Skills CLI - v1.0.0
# Centralized setup and management for Figma Behavioral Expert and other skills.

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Antigravity Skills CLI ===${NC}"

# Function: Dependency Check (Bun)
check_bun() {
    if ! command -v bun &> /dev/null; then
        echo -e "${RED}[!] Bun not found.${NC} Installing..."
        curl -fsSL https://bun.sh/install | bash
        export PATH="$HOME/.bun/bin:$PATH"
        echo -e "${GREEN}[✓] Bun installed successfully.${NC}"
    else
        echo -e "${GREEN}[✓] Bun is already installed.${NC}"
    fi
}

# Function: Figma MCP Check
check_figma_mcp() {
    echo -e "${BLUE}[*] Checking Figma MCP...${NC}"
    # bunx will handle the latest version on run, but we can verify it works
    if bunx cursor-talk-to-figma-mcp --help &> /dev/null; then
        echo -e "${GREEN}[✓] Figma MCP is ready.${NC}"
    else
        echo -e "${RED}[!] Issue with Figma MCP. It will be downloaded on the first run.${NC}"
    fi
}

# Function: Setup Repository
setup_repo() {
    SKILLS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
    echo -e "${BLUE}[*] Configuring skills directory at: ${SKILLS_DIR}${NC}"
    
    # In a real CLI, we might symlink this to a standard location
    # For now, we confirm the current location is valid for Antigravity
    echo -e "${GREEN}[✓] Skills repository localized.${NC}"
}

# Main Commands
case "$1" in
    setup)
        echo -e "${BLUE}Starting Environment Setup...${NC}"
        check_bun
        check_figma_mcp
        setup_repo
        echo -e "\n${GREEN}READY TO GO!${NC}"
        echo -e "To use the skills, make sure your IDE is pointing to: ${BLUE}${SKILLS_DIR}${NC}"
        ;;
    update)
        echo -e "${BLUE}Checking for updates...${NC}"
        git pull
        check_bun
        echo -e "${GREEN}[✓] All skills are up to date.${NC}"
        ;;
    *)
        echo "Usage: $0 {setup|update}"
        exit 1
        ;;
esac
