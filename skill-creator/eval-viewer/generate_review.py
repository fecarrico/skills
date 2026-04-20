import os
import json
import argparse
import base64
from datetime import datetime

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skill Evaluation Viewer - {skill_name}</title>
    <style>
        body {{ font-family: 'Inter', -apple-system, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; display: flex; height: 100vh; }}
        nav {{ width: 300px; background: #1e293b; border-right: 1px solid #334155; overflow-y: auto; padding: 1rem; }}
        main {{ flex: 1; overflow-y: auto; padding: 2rem; background: #0f172a; }}
        .eval-item {{ padding: 0.75rem; cursor: pointer; border-radius: 0.5rem; margin-bottom: 0.5rem; border: 1px solid transparent; transition: all 0.2s; }}
        .eval-item:hover {{ background: #334155; }}
        .eval-item.active {{ background: #3b82f6; border-color: #60a5fa; color: white; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }}
        .card {{ background: #1e293b; border-radius: 0.75rem; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #334155; }}
        .pill {{ display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; }}
        .pill-pass {{ background: #065f46; color: #34d399; }}
        .pill-fail {{ background: #7f1d1d; color: #f87171; }}
        pre {{ background: #0f172a; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; color: #94a3b8; font-size: 0.875rem; }}
        textarea {{ width: 100%; height: 150px; background: #0f172a; color: #f8fafc; border: 1px solid #334155; border-radius: 0.5rem; padding: 1rem; margin-top: 1rem; font-family: inherit; }}
        .button {{ background: #3b82f6; color: white; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; border: none; font-weight: 600; display: inline-block; margin-top: 1rem; text-decoration: none; }}
        .button:hover {{ background: #2563eb; }}
        #benchmark-view {{ display: none; }}
        .tabs {{ display: flex; gap: 1rem; margin-bottom: 2rem; border-bottom: 1px solid #334155; padding-bottom: 0.5rem; }}
        .tab {{ cursor: pointer; padding: 0.5rem 1rem; color: #94a3b8; }}
        .tab.active {{ color: #3b82f6; border-bottom: 2px solid #3b82f6; }}
    </style>
</head>
<body>
    <nav>
        <h2>Test Cases</h2>
        <div id="eval-list"></div>
    </nav>
    <main>
        <div class="tabs">
            <div class="tab active" onclick="showTab('outputs')">Outputs</div>
            <div class="tab" onclick="showTab('benchmark')">Benchmark</div>
        </div>

        <div id="outputs-view">
            <div id="content-area">
                <h1>Select a test case to view results</h1>
            </div>
        </div>

        <div id="benchmark-view">
            <h1>Benchmark Summary</h1>
            <div id="benchmark-content"></div>
        </div>

        <div style="margin-top: 4rem;">
            <button class="button" onclick="downloadFeedback()">Submit All Reviews (Download JSON)</button>
        </div>
    </main>

    <script>
        const data = {data_json};
        const benchmark = {benchmark_json};
        let currentEvalId = null;
        let feedback = {{}};

        function showTab(tab) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelector(`.tab[onclick*="${{tab}}"]`).classList.add('active');
            document.getElementById('outputs-view').style.display = tab === 'outputs' ? 'block' : 'none';
            document.getElementById('benchmark-view').style.display = tab === 'benchmark' ? 'block' : 'none';
        }}

        function renderList() {{
            const list = document.getElementById('eval-list');
            list.innerHTML = '';
            data.evals.forEach(ev => {{
                const div = document.createElement('div');
                div.className = `eval-item ${{currentEvalId === ev.id ? 'active' : ''}}`;
                div.textContent = ev.name || ev.id;
                div.onclick = () => selectEval(ev.id);
                list.appendChild(div);
            }});
        }}

        function selectEval(id) {{
            currentEvalId = id;
            renderList();
            const ev = data.evals.find(e => e.id === id);
            const content = document.getElementById('content-area');
            
            let html = `<h1>${{ev.name || ev.id}}</h1>`;
            html += `<div class="card"><h3>Prompt</h3><pre>${{ev.prompt}}</pre></div>`;
            
            for (const config in ev.configs) {{
                const res = ev.configs[config];
                html += `<div class="card">
                    <h3>Output: ${{config}}</h3>
                    <div style="margin-bottom: 1rem;">
                        <span class="pill ${{res.pass_rate === 100 ? 'pill-pass' : 'pill-fail'}}">Pass Rate: ${{res.pass_rate}}%</span>
                    </div>
                    ${{res.output ? `<pre>${{res.output}}</pre>` : '<p>No output file found</p>'}}
                    <h4>Grading Details</h4>
                    <ul>
                        ${{res.expectations.map(e => `<li>${{e.passed ? '✅' : '❌'}} <strong>${{e.text}}</strong>: ${{e.evidence}}</li>`).join('')}}
                    </ul>
                </div>`;
            }}

            html += `<div class="card">
                <h3>Your Feedback</h3>
                <textarea oninput="saveFeedback('${{id}}', this.value)" placeholder="Enter notes here...">${{feedback[id] || ''}}</textarea>
            </div>`;
            
            content.innerHTML = html;
        }}

        function saveFeedback(id, val) {{
            feedback[id] = val;
        }}

        function downloadFeedback() {{
            const output = {{
                reviews: Object.keys(feedback).map(id => ({{ run_id: id, feedback: feedback[id], timestamp: new Date().toISOString() }})),
                status: 'complete'
            }};
            const blob = new Blob([JSON.stringify(output, null, 2)], {{ type: 'application/json' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'feedback.json';
            a.click();
        }}

        function renderBenchmark() {{
            if (!benchmark) return;
            const container = document.getElementById('benchmark-content');
            let html = '<table style="width:100%; border-collapse: collapse; margin-top: 1rem;">';
            html += '<tr style="border-bottom: 1px solid #334155; text-align: left;"><th>Config</th><th>Pass Rate</th><th>Avg Tokens</th><th>Avg Time</th></tr>';
            for (const config in benchmark.summary) {{
                const s = benchmark.summary[config];
                html += `<tr style="border-bottom: 1px solid #334155; height: 3rem;">
                    <td>${{config}}</td>
                    <td>${{s.mean_pass_rate.toFixed(1)}}%</td>
                    <td>${{s.mean_tokens.toFixed(0)}}</td>
                    <td>${{s.mean_duration_s.toFixed(1)}}s</td>
                </tr>`;
            }}
            html += '</table>';
            container.innerHTML = html;
        }}

        renderList();
        renderBenchmark();
    </script>
</body>
</html>
"""

def generate_review(workspace_path, skill_name, benchmark_path=None, output_file="review.html"):
    print(f"Generating review for {skill_name}...")
    
    data = {"skill_name": skill_name, "evals": []}
    
    eval_dirs = [d for d in os.listdir(workspace_path) if os.path.isdir(os.path.join(workspace_path, d)) and d.startswith("eval-")]
    
    for eval_dir in eval_dirs:
        eval_path = os.path.join(workspace_path, eval_dir)
        meta_file = os.path.join(eval_path, "eval_metadata.json")
        
        current_eval = {"id": eval_dir, "name": eval_dir, "prompt": "", "configs": {}}
        
        if os.path.exists(meta_file):
            with open(meta_file, 'r') as f:
                meta = json.load(f)
                current_eval["name"] = meta.get("eval_name", eval_dir)
                current_eval["prompt"] = meta.get("prompt", "")

        for config_name in os.listdir(eval_path):
            config_path = os.path.join(eval_path, config_name)
            if not os.path.isdir(config_path): continue
            
            grading_file = os.path.join(config_path, "grading.json")
            output_dir = os.path.join(config_path, "outputs")
            
            pass_rate = 0
            expectations = []
            if os.path.exists(grading_file):
                with open(grading_file, 'r') as f:
                    grading = json.load(f)
                    expectations = grading.get("expectations", [])
                    if expectations:
                        passed = sum(1 for e in expectations if e.get("passed"))
                        pass_rate = (passed / len(expectations)) * 100
            
            # Try to read some output text
            main_output = ""
            if os.path.exists(output_dir):
                files = os.listdir(output_dir)
                if files:
                    # Pick the largest or first .md/.txt file
                    for f in sorted(files, key=lambda x: os.path.getsize(os.path.join(output_dir, x)), reverse=True):
                        if f.endswith(('.md', '.txt', '.json', '.py', '.js')):
                            with open(os.path.join(output_dir, f), 'r', errors='ignore') as of:
                                main_output = of.read()
                            break

            current_eval["configs"][config_name] = {
                "pass_rate": pass_rate,
                "expectations": expectations,
                "output": main_output
            }
            
        data["evals"].append(current_eval)

    benchmark_data = None
    if benchmark_path and os.path.exists(benchmark_path):
        with open(benchmark_path, 'r') as f:
            benchmark_data = json.load(f)

    # Render HTML
    final_html = HTML_TEMPLATE.format(
        skill_name=skill_name,
        data_json=json.dumps(data),
        benchmark_json=json.dumps(benchmark_data) if benchmark_data else "null"
    )

    with open(output_file, 'w') as f:
        f.write(final_html)
    
    print(f"Viewer generated at: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace")
    parser.add_argument("--skill-name", required=True)
    parser.add_argument("--benchmark")
    parser.add_argument("--static", default="review.html")
    args = parser.parse_args()
    generate_review(args.workspace, args.skill_name, args.benchmark, args.static)
