import os
import sys
import tkinter as tk
import json

# Ensure the project root is in the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ui.block_ui import BlockUI
from playground.playground import Playground
from internal_logic.backend import Backend
from hotkey_management.hotkey_manager import HotkeyManager
from internal_logic.hotkey_runner import HotkeyRunner

def create_project_structure(base_path):
    # Define the folder structure
    folders = [
        "ui",
        "blocks",
        "playground",
        "hotkey_management",
        "internal_logic",
        "assets/icons",
        "assets/themes",
        "assets/data"
    ]

    # Create the base path if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Create all the folders in the structure
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Create __init__.py file in each folder to make them Python packages
        init_file_path = os.path.join(folder_path, "__init__.py")
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as f:
                f.write("# Init file for " + folder)

    # Create Python files for the main script if they do not exist
    files = [
        "main.py",
        "ui/ui.py",
        "ui/block_ui.py",
        "ui/custom_theme.py",
        "blocks/block_base.py",
        "blocks/mouse_block.py",
        "blocks/keyboard_block.py",
        "blocks/wait_block.py",
        "blocks/coordinate_block.py",
        "playground/playground.py",
        "playground/execution_flow.py",
        "hotkey_management/hotkey_manager.py",
        "hotkey_management/file_storage.py",
        "internal_logic/backend.py",
        "internal_logic/coordinate_finder.py",
        "internal_logic/utilities.py",
        "internal_logic/hotkey_runner.py"
    ]

    # Create empty files in the project structure
    for file in files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("# Placeholder for " + file)

    # Remove any extra files that are not part of the project structure
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_path)
            if relative_path not in files and file != "__init__.py":
                os.remove(file_path)

    # Check that all __init__.py files exist in each folder
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        init_file_path = os.path.join(folder_path, "__init__.py")
        if not os.path.exists(init_file_path):
            print(f"Missing __init__.py in {folder_path}, creating it now...")
            with open(init_file_path, 'w') as f:
                f.write("# Init file for " + folder)

def save_scan_status(base_path, status):
    status_file = os.path.join(base_path, "scan_status.json")
    with open(status_file, 'w') as f:
        json.dump({"scan_completed": status}, f)

def load_scan_status(base_path):
    status_file = os.path.join(base_path, "scan_status.json")
    if os.path.exists(status_file):
        with open(status_file, 'r') as f:
            data = json.load(f)
            return data.get("scan_completed", False)
    return False

def launch_project():
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
    # Check if the scan has already been completed
    scan_completed = load_scan_status(base_path)

    if not scan_completed:
        # Create the project structure if needed (first time setup)
        create_project_structure(base_path)
        save_scan_status(base_path, True)
        print(f"Project structure created at '{base_path}'. Please run the script again to launch the UI.")
    else:
        # Launch the complete project UI
        launch_project()
