import os
import json
import argparse
import statistics

def aggregate(iteration_path, skill_name):
    print(f"Aggregating results for {skill_name} in {iteration_path}...")
    
    results = {
        "skill_name": skill_name,
        "iteration_path": iteration_path,
        "evals": [],
        "summary": {}
    }

    # Configuration types (e.g., "with_skill", "without_skill", "old_skill")
    configs = {}

    eval_dirs = [d for d in os.listdir(iteration_path) if os.path.isdir(os.path.join(iteration_path, d)) and d.startswith("eval-")]
    
    for eval_dir in eval_dirs:
        eval_path = os.path.join(iteration_path, eval_dir)
        eval_data = {"id": eval_dir, "configs": {}}
        
        # Look for subdirectories like "with_skill", "without_skill"
        for config_name in os.listdir(eval_path):
            config_path = os.path.join(eval_path, config_name)
            if not os.path.isdir(config_path):
                continue
            
            # Read Grading
            grading_file = os.path.join(config_path, "grading.json")
            timing_file = os.path.join(config_path, "timing.json")
            
            pass_rate = 0
            if os.path.exists(grading_file):
                with open(grading_file, 'r') as f:
                    grading = json.load(f)
                    expectations = grading.get("expectations", [])
                    if expectations:
                        passed = sum(1 for e in expectations if e.get("passed"))
                        pass_rate = (passed / len(expectations)) * 100
            
            timing = {}
            if os.path.exists(timing_file):
                with open(timing_file, 'r') as f:
                    timing = json.load(f)

            eval_data["configs"][config_name] = {
                "pass_rate": pass_rate,
                "tokens": timing.get("total_tokens", 0),
                "duration_ms": timing.get("duration_ms", 0)
            }
            
            if config_name not in configs:
                configs[config_name] = {"pass_rates": [], "tokens": [], "durations": []}
            
            configs[config_name]["pass_rates"].append(pass_rate)
            configs[config_name]["tokens"].append(timing.get("total_tokens", 0))
            configs[config_name]["durations"].append(timing.get("duration_ms", 0) / 1000.0)

        results["evals"].append(eval_data)

    # Compute Averages
    for name, data in configs.items():
        results["summary"][name] = {
            "mean_pass_rate": statistics.mean(data["pass_rates"]) if data["pass_rates"] else 0,
            "mean_tokens": statistics.mean(data["tokens"]) if data["tokens"] else 0,
            "mean_duration_s": statistics.mean(data["durations"]) if data["durations"] else 0,
            "std_pass_rate": statistics.stdev(data["pass_rates"]) if len(data["pass_rates"]) > 1 else 0
        }

    # Save benchmark.json
    output_json = os.path.join(iteration_path, "benchmark.json")
    with open(output_json, 'w') as f:
        json.dump(results, f, indent=2)

    # Save benchmark.md
    output_md = os.path.join(iteration_path, "benchmark.md")
    with open(output_md, 'w') as f:
        f.write(f"# Benchmark Results: {skill_name}\n\n")
        f.write("| Config | Pass Rate (%) | Avg Tokens | Avg Time (s) |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for name, summary in results["summary"].items():
            f.write(f"| {name} | {summary['mean_pass_rate']:.1f}% (±{summary['std_pass_rate']:.1f}) | {summary['mean_tokens']:.0f} | {summary['mean_duration_s']:.1f}s |\n")

    print(f"Aggregation complete. Saved to {output_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("iteration_path")
    parser.add_argument("--skill-name", required=True)
    args = parser.parse_args()
    aggregate(args.iteration_path, args.skill_name)
