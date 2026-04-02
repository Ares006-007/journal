import subprocess
import time
import os
import json
from datetime import datetime

REPO_PATH = r"C:\Users\Shaik Mohammad Ajhaj\OneDrive\Desktop\digi journal"
COMMIT_EVERY_SECONDS = 40 * 60
CHECK_INTERVAL = 30
STATE_FILE = os.path.join(REPO_PATH, ".git", "autocommit_state.json")
VSCODE_PROCESS = "Code.exe"

def is_vscode_running():
    try:
        result = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {VSCODE_PROCESS}"],
            capture_output=True, text=True
        )
        return VSCODE_PROCESS.lower() in result.stdout.lower()
    except Exception:
        return False

def has_changes():
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_PATH, capture_output=True, text=True
        )
        return bool(result.stdout.strip())
    except Exception:
        return False

def do_commit_and_push():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", f"auto-commit: {now}"],
            cwd=REPO_PATH, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_PATH, check=True)
        print(f"[{now}] Auto-committed and pushed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[{now}] Failed: {e}")
        return False

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f).get("cumulative_seconds", 0)
        except Exception:
            pass
    return 0

def save_state(cumulative_seconds):
    try:
        with open(STATE_FILE, "w") as f:
            json.dump({"cumulative_seconds": cumulative_seconds}, f)
    except Exception:
        pass

def main():
    os.chdir(REPO_PATH)
    cumulative_seconds = load_state()
    print("Auto-commit tracker started")
    print(f"Progress restored: {cumulative_seconds // 60}m")

    while True:
        if is_vscode_running():
            cumulative_seconds += CHECK_INTERVAL
            save_state(cumulative_seconds)
            mins = cumulative_seconds // 60
            remaining = max(0, COMMIT_EVERY_SECONDS - cumulative_seconds) // 60
            print(f"Coding: {mins}m | Next commit in: {remaining}m", end="\r")
            if cumulative_seconds >= COMMIT_EVERY_SECONDS:
                print()
                if has_changes():
                    if do_commit_and_push():
                        cumulative_seconds = 0
                        save_state(0)
                else:
                    print("40min reached but no changes.")
                    cumulative_seconds = 0
                    save_state(0)
        else:
            print(f"VS Code not open - timer paused at {cumulative_seconds // 60}m", end="\r")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped. Progress saved.")