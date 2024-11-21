import os
import json
from utilities import ensure_directory_exists

class FileStorage:
    def __init__(self, storage_directory="data_storage"):
        self.storage_directory = storage_directory
        ensure_directory_exists(self.storage_directory)

    def save_hotkey_script(self, script_name, script_data):
        """
        Save a hotkey script to a JSON file.
        """
        file_path = os.path.join(self.storage_directory, f"{script_name}.json")
        try:
            with open(file_path, 'w') as json_file:
                json.dump(script_data, json_file, indent=4)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving data to {file_path}: {e}")

    def load_hotkey_script(self, script_name):
        """
        Load a hotkey script from a JSON file.
        """
        file_path = os.path.join(self.storage_directory, f"{script_name}.json")
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                print(f"Data successfully loaded from {file_path}")
                return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_path}: {e}")
            return None
        except Exception as e:
            print(f"Error loading data from {file_path}: {e}")
            return None

    def delete_hotkey_script(self, script_name):
        """
        Delete a hotkey script file.
        """
        file_path = os.path.join(self.storage_directory, f"{script_name}.json")
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted script: {file_path}")
            else:
                print(f"Script not found: {file_path}")
        except Exception as e:
            print(f"Error deleting script: {e}")

    def list_hotkey_scripts(self):
        """
        List all hotkey scripts available in the storage directory.
        """
        try:
            files = [f for f in os.listdir(self.storage_directory) if f.endswith('.json')]
            script_names = [os.path.splitext(f)[0] for f in files]
            return script_names
        except Exception as e:
            print(f"Error listing scripts: {e}")
            return []

if __name__ == "__main__":
    storage = FileStorage()

    # Example usage
    script_data = {
        "blocks": [
            {
                "type": "Mouse Block",
                "description": "Click at specific location",
                "details": {"action": "click", "coordinates": (100, 200)}
            },
            {
                "type": "Keyboard Block",
                "description": "Type a message",
                "details": {"key_sequence": "Hello, World!"}
            },
            {
                "type": "Wait Block",
                "description": "Wait for a few seconds",
                "details": {"duration": 3}
            }
        ]
    }

    # Save script
    storage.save_hotkey_script("example_script", script_data)

    # Load script
    loaded_script = storage.load_hotkey_script("example_script")
    print("Loaded script:", loaded_script)

    # List available scripts
    scripts = storage.list_hotkey_scripts()
    print("Available scripts:", scripts)

    # Delete script
    storage.delete_hotkey_script("example_script")
