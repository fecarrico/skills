# Skill Creator - Editor de Skills do Antigravity
 
Esta skill permite criar, testar e otimizar novas skills para o seu ambiente Antigravity de forma sistematizada.
 
## Como Usar
 
Se você tem uma ideia para uma nova automação ou quer transformar um fluxo de chat em algo reutilizável, peça:
 
> "Antigravity, vamos criar uma nova skill para [descrição do objetivo]"
 
A partir daí, eu (Antigravity) seguirei o processo de:
1.  **Captura de Intenção**: Entender exatamente o que a skill deve fazer.
2.  **Rascunho**: Criar o `SKILL.md` inicial.
3.  **Testes**: Rodar casos de teste em paralelo (usando subagents).
4.  **Avaliação**: Gerar um relatório visual no navegador para você revisar os resultados.
5.  **Iteração**: Melhorar a skill com base no seu feedback.
6.  **Otimização**: Ajustar a descrição da skill para garantir que ela seja acionada no momento certo.
 
## Estrutura da Skill
- [SKILL.md](./SKILL.md): Instruções mestre da skill.
- **scripts/**: Scripts para benchmarking e empacotamento.
- **eval-viewer/**: Gerador de relatórios visuais.
- **agents/**: Instruções para subagents especializados (avaliadores).
- **references/**: Esquemas de dados e boas práticas.
 
## Destaque: Fluxo Visual
Após rodar os testes, eu gerarei um arquivo `review.html`. Você poderá abri-lo para comparar as saídas do Antigravity com e sem a skill, deixando feedback direto em cada caso de teste.
