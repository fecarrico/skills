# Sobre a Skill Creator

A `skill-creator` é uma ferramenta interna para desenvolvedores Antigravity que automatiza o ciclo de vida de uma Skill.

## Estrutura de Diretórios
- `SKILL.md`: O cérebro da skill.
- `scripts/`: Lógica de execução pesada (benchmarking, packaging).
- `eval-viewer/`: Interface visual para análise de resultados.
- `agents/`: Definições de subagents para grading automático.
- `references/`: Documentação e guias de estilo (incluindo este arquivo).

## Destaque: Fluxo Visual
Após rodar os testes, a skill gera um arquivo `review.html`. Você poderá abri-lo para comparar as saídas do Antigravity com e sem a skill, deixando feedback direto em cada caso de teste.
