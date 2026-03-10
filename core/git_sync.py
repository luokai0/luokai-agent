import subprocess
from datetime import datetime

def git_push(message=None):
    """Automatically commit and push everything to GitHub"""
    try:
        if not message:
            message = f"🧬 Auto-sync {datetime.now().strftime('%Y-%m-%d %H:%M')}"

        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        
        result = subprocess.run(
            ["git", "commit", "-m", message],
            capture_output=True, text=True
        )
        
        # Nothing new to commit
        if "nothing to commit" in result.stdout:
            print("📦 Nothing new to push")
            return True

        push = subprocess.run(
            ["git", "push"],
            capture_output=True, text=True
        )

        if push.returncode == 0:
            print(f"✅ Auto-pushed to GitHub: {message}")
            return True
        else:
            print(f"⚠️ Push failed: {push.stderr[:100]}")
            return False

    except Exception as e:
        print(f"⚠️ Git sync error: {e}")
        return False
