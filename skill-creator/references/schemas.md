# Skill Creator Schemas
 
## evals.json
The master list of test cases for a skill.
```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```
 
## eval_metadata.json
Located in each test case directory.
```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name",
  "prompt": "The full prompt",
  "assertions": [
    {
      "name": "check_file_exists",
      "description": "Verify the output contains report.md"
    }
  ]
}
```
 
## grading.json
The output of the grader subagent.
```json
{
  "expectations": [
    {
      "text": "Assertion description",
      "passed": true,
      "evidence": "Detailed explanation"
    }
  ]
}
```
 
## timing.json
Timing and token usage for a specific run.
```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```
