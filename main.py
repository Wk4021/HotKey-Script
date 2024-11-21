import os
import sys
import tkinter as tk
import json
import subprocess

# Ensure the project root is in the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def create_or_update_project_structure(base_path):
    repo_url = "https://github.com/Wk4021/HotKey-Script.git"
    if not os.path.exists(base_path):
        # Clone the project from GitHub if not already present
        try:
            subprocess.run(["git", "clone", repo_url, base_path], check=True)
            print(f"Project cloned from {repo_url}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repository: {e}")
            return False
    else:
        # Pull the latest changes if the project already exists
        try:
            subprocess.run(["git", "-C", base_path, "pull"], check=True)
            print(f"Project updated from {repo_url}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to update repository: {e}")
            return False
    return True

def load_scan_status(base_path):
    status_file = os.path.join(base_path, "scan_status.json")
    if os.path.exists(status_file):
        with open(status_file, 'r') as f:
            data = json.load(f)
            return data.get("scan_completed", False)
    return False

def save_scan_status(base_path, status):
    status_file = os.path.join(base_path, "scan_status.json")
    with open(status_file, 'w') as f:
        json.dump({"scan_completed": status}, f)

def launch_project():
    try:
        from ui.block_ui import BlockUI
        from playground.playground import Playground
        from internal_logic.backend import Backend
        from hotkey_management.hotkey_manager import HotkeyManager
        from internal_logic.hotkey_runner import HotkeyRunner
    except ImportError as e:
        print(f"Error importing modules: {e}")
        return

    root = tk.Tk()
    root.title("Hotkey Script Playground")
    root.geometry("1000x700")

    # Initialize Backend to orchestrate everything
    backend = Backend(root)

    # Integrate the BlockUI and Playground into the backend
    backend.block_ui = BlockUI(root)
    backend.playground = Playground(root)

    # Set up Hotkey Manager for saving/loading scripts
    backend.hotkey_manager = HotkeyManager()

    # Optionally, set up hotkey runner for running scripts
    backend.hotkey_runner = HotkeyRunner(backend.blocks)

    # Start the UI main loop
    root.mainloop()

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Create or update the project structure by cloning or pulling from GitHub
    if create_or_update_project_structure(base_path):
        # Launch the complete project UI
        launch_project()
