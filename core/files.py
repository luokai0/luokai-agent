import os
import json
import pandas as pd
from datetime import datetime

WORKSPACE = "workspace"
os.makedirs(WORKSPACE, exist_ok=True)

def read_file(filepath):
    """Read any text/csv/excel file"""
    try:
        ext = filepath.split(".")[-1].lower()
        if ext in ["csv"]:
            df = pd.read_csv(filepath)
            return df.to_string()
        elif ext in ["xlsx", "xls"]:
            df = pd.read_excel(filepath)
            return df.to_string()
        else:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        return f"❌ Could not read file: {e}"

def write_file(filename, content):
    """Write content to a file in workspace"""
    try:
        filepath = os.path.join(WORKSPACE, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ File saved: {filepath}")
        return filepath
    except Exception as e:
        return f"❌ Could not write file: {e}"

def write_csv(filename, data):
    """Write a list of dicts to CSV"""
    try:
        filepath = os.path.join(WORKSPACE, filename)
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
        print(f"✅ CSV saved: {filepath}")
        return filepath
    except Exception as e:
        return f"❌ Could not write CSV: {e}"

def list_files():
    """List all files in workspace"""
    try:
        files = os.listdir(WORKSPACE)
        if not files:
            return "📂 Workspace is empty"
        return "\n".join([f"📄 {f}" for f in files])
    except Exception as e:
        return f"❌ Error: {e}"

def delete_file(filename):
    """Delete a file from workspace"""
    try:
        filepath = os.path.join(WORKSPACE, filename)
        os.remove(filepath)
        return f"✅ Deleted: {filename}"
    except Exception as e:
        return f"❌ Could not delete: {e}"
