from .file_storage import FileStorage
from blocks.coordinate_block import CoordinateBlock
from blocks.keyboard_block import KeyboardBlock
from blocks.mouse_block import MouseBlock
from blocks.wait_block import WaitBlock

class HotkeyManager:
    def __init__(self):
        self.storage = FileStorage()
        self.current_hotkey_script = None

    def create_hotkey_script(self, script_name, script_data):
        """
        Create and save a new hotkey script.
        """
        self.storage.save_hotkey_script(script_name, script_data)
        print(f"Hotkey script '{script_name}' created successfully.")

    def load_hotkey_script(self, script_name):
        """
        Load an existing hotkey script.
        """
        script_data = self.storage.load_hotkey_script(script_name)
        if script_data:
            self.current_hotkey_script = self.deserialize_blocks(script_data["blocks"])
            print(f"Hotkey script '{script_name}' loaded successfully.")
        else:
            print(f"Failed to load hotkey script '{script_name}'.")
        return self.current_hotkey_script

    def delete_hotkey_script(self, script_name):
        """
        Delete an existing hotkey script.
        """
        self.storage.delete_hotkey_script(script_name)
        print(f"Hotkey script '{script_name}' deleted successfully.")

    def list_hotkey_scripts(self):
        """
        List all available hotkey scripts.
        """
        scripts = self.storage.list_hotkey_scripts()
        print("Available hotkey scripts:")
        for script in scripts:
            print(f"- {script}")
        return scripts

    def deserialize_blocks(self, blocks_data):
        """
        Deserialize block data into block instances.
        """
        blocks = []
        for block_data in blocks_data:
            block_type = block_data["type"]
            if block_type == "Mouse Block":
                block = MouseBlock(**block_data["details"])
            elif block_type == "Keyboard Block":
                block = KeyboardBlock(**block_data["details"])
            elif block_type == "Wait Block":
                block = WaitBlock(**block_data["details"])
            elif block_type == "Coordinate Block":
                block = CoordinateBlock(**block_data["details"])
            else:
                print(f"Unknown block type: {block_type}")
                continue
            blocks.append(block)
        return blocks

if __name__ == "__main__":
    manager = HotkeyManager()

    # Example script data
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

    # Create a new hotkey script
    manager.create_hotkey_script("example_script", script_data)

    # List available hotkey scripts
    manager.list_hotkey_scripts()

    # Load a hotkey script
    loaded_blocks = manager.load_hotkey_script("example_script")
    for block in loaded_blocks:
        print(block)

    # Delete a hotkey script
    manager.delete_hotkey_script("example_script")
