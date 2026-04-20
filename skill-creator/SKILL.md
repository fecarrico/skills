---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy in the Antigravity IDE.
---
 
# Skill Creator (Antigravity Edition)
 
A skill for creating new Antigravity skills and iteratively improving them.
 
At a high level, the process of creating a skill goes like this:
 
- Decide what you want the skill to do and roughly how it should do it.
- Write a draft of the skill in `SKILL.md` format.
- Create a few test prompts and run an Antigravity subagent with access to the skill.
- Help the user evaluate the results both qualitatively and quantitatively.
  - Draft quantitative evals (assertions) while runs happen in the background.
  - Use the `eval-viewer/generate_review.py` script to display results in the browser.
- Rewrite the skill based on feedback and benchmarking.
- Repeat until satisfied.
- Optimize the triggering description using the `run_loop.py` script.
 
## Communicating with the user
 
Antigravity users range from computer-literate developers to beginners. Adjust your tone accordingly:
- Use terms like "evaluation" and "benchmark" cautiously.
- Briefly explain technical jargon like "JSON" or "assertions" if the user seems unfamiliar.
- Maintain a premium, helpful, and "wow" aesthetic in your responses.
 
---
 
## Creating a skill
 
### Capture Intent
 
Understand the user's intent. If they say "turn this into a skill", extract the workflow, sequence, and tools used from the current conversation.
 
1. What should this skill enable Antigravity to do?
2. When should this skill trigger? (Contexts and phrases)
3. Expected output format?
4. Setup test cases in `evals/evals.json`.
 
### Write the SKILL.md
 
- **name**: Concise identifier.
- **description**: Triggering mechanism. Be "pushy" to avoid undertriggering. Mention specific keywords and contexts.
- **instructions**: Explicit, imperative guidance for the model.
 
### Skill Writing Guide
 
#### Anatomy of a Skill
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Utility scripts (Python/JS)
    ├── references/ - Docs and schemas
    └── assets/     - Templates, icons, etc.
```
 
#### Progressive Disclosure
1. **Metadata**: Always in context.
2. **SKILL.md body**: Loaded when triggered.
3. **Bundled resources**: Read as needed by the agent.
 
---
 
## Running and evaluating test cases
 
Organize results in `<skill-name>-workspace/iteration-N/eval-M/`.
 
### Step 1: Spawn all runs (with-skill AND baseline)
Spawn subagents in parallel for each test case.
- **With-skill**: Agent with the new skill draft.
- **Baseline**: Agent without the skill (or with the previous version).
 
### Step 2: Draft assertions
While runs are in progress, create quantitative checks (e.g., "contains specific text", "file exists").
 
### Step 3: Capture timing and token data
Access `total_tokens` and `duration_ms` from the subagent completion notification and save to `timing.json`.
 
### Step 4: Grade and Launch Viewer
1. **Grade**: Use a grader subagent or script to evaluate assertions.
2. **Aggregate**: Run `python -m scripts.aggregate_benchmark <workspace>/iteration-N`.
3. **Launch Viewer**:
   ```bash
   python eval-viewer/generate_review.py <workspace>/iteration-N --skill-name "name"
   ```
   Open the generated HTML to review outputs and feedback.
 
---
 
## Improving the skill
 
Apply feedback from the viewer to the skill draft. Focus on:
- **Generalization**: Don't overfit to specific test cases.
- **Explanation**: Explain *why* certain instructions are important.
- **Bundled scripts**: If subagents repeat the same logic, move it to a script in `scripts/`.
 
---
 
## Description Optimization
 
Use the `scripts/run_loop.py` script to optimize the `description` field for better triggering accuracy across various queries.
 
1. Generate 20+ trigger eval queries (realistic and specific).
2. Run the optimization loop to find the best description based on pass rates.
 
---
 
## Packaging
When finished, use the packager:
```bash
python -m scripts.package_skill /path/to/skill
```
