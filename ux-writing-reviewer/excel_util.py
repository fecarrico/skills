import pandas as pd
import json
import sys
import os

def read_column(file_path, column_name):
    try:
        df = pd.read_excel(file_path)
        if column_name not in df.columns:
            return {"error": f"Coluna '{column_name}' não encontrada. Disponíveis: {list(df.columns)}"}
        return df[column_name].tolist()
    except Exception as e:
        return {"error": str(e)}

def write_results(file_path, original_column, results, explanations, output_path=None):
    try:
        df = pd.read_excel(file_path)
        df["Texto Revisado (UX)"] = results
        df["Explicação (UX)"] = explanations
        
        if not output_path:
            output_path = file_path.replace(".xlsx", "_revisado_ag.xlsx")
            
        df.to_excel(output_path, index=False)
        return {"success": True, "path": output_path}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["read", "write"])
    parser.add_argument("--file", required=True)
    parser.add_argument("--column", required=False)
    parser.add_argument("--data", required=False)
    parser.add_argument("--explanations", required=False)
    parser.add_argument("--output", required=False)

    args = parser.parse_args()

    if args.command == "read":
        print(json.dumps(read_column(args.file, args.column)))
    elif args.command == "write":
        data = json.loads(args.data)
        explanations = json.loads(args.explanations)
        print(json.dumps(write_results(args.file, args.column, data, explanations, args.output)))
