from HotKeyScript.ui.block_ui import BlockUI
from HotKeyScript.playground.playground import Playground
from HotKeyScript.playground.execution_flow import ExecutionFlow
from HotKeyScript.hotkey_management.hotkey_manager import HotkeyManager
from HotKeyScript.blocks.mouse_block import MouseBlock
from HotKeyScript.blocks.keyboard_block import KeyboardBlock
from HotKeyScript.blocks.wait_block import WaitBlock
from HotKeyScript.blocks.coordinate_block import CoordinateBlock
import tkinter as tk

class Backend:
    def __init__(self, root):
        # Initialize UI components
        self.root = root
        self.block_ui = BlockUI(root)
        self.playground = Playground(root)

        # Initialize block list
        self.blocks = []

        # Set up Hotkey Manager
        self.hotkey_manager = HotkeyManager()

        # Collect blocks from the UI and Playground
        self.collect_blocks_from_ui()

        # Initialize the execution flow
        self.execution_flow = ExecutionFlow(self.blocks)

    def collect_blocks_from_ui(self):
        """
        This function collects blocks from the UI components and playground.
        """
        # Collect blocks from Block UI and Playground
        self.blocks = self.playground.get_execution_order()

    def start_execution_flow(self):
        """
        Start the execution flow using the collected blocks.
        """
        # Determine and execute the flow
        self.execution_flow.determine_flow()
        self.execution_flow.execute()

    def save_script(self, script_name):
        """
        Save the current hotkey script.
        """
        script_data = {
            "blocks": [
                {
                    "type": block.block_type,
                    "description": block.get_description(),
                    "details": block.__dict__  # Save additional details of the block
                } for block in self.blocks
            ]
        }
        self.hotkey_manager.create_hotkey_script(script_name, script_data)

    def load_script(self, script_name):
        """
        Load a hotkey script and populate the playground with blocks.
        """
        script_data = self.hotkey_manager.load_hotkey_script(script_name)
        if script_data:
            self.blocks = []  # Clear existing blocks
            for block_data in script_data["blocks"]:
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
                    continue
                self.blocks.append(block)
                # Add block to playground visually
                self.playground.add_block(block, 100, 100)  # Example coordinates

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Backend Example")
    root.geometry("1000x700")

    # Create a Backend instance
    backend = Backend(root)

    # Example usage of saving and loading scripts
    backend.save_script("example_script")
    backend.load_script("example_script")

    # Start execution flow after setting up
    backend.start_execution_flow()

    root.mainloop()
