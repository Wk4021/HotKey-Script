import keyboard
import time

class HotkeyRunner:
    def __init__(self, blocks):
        # Initialize with a list of blocks to be executed
        self.blocks = blocks

    def run(self):
        """
        Execute the blocks in the specified order when a hotkey is pressed.
        """
        print("Press 'ctrl+shift+r' to run the automation flow...")
        keyboard.add_hotkey('ctrl+shift+r', self.execute_blocks)
        keyboard.wait('esc')  # Keep the program running until 'esc' is pressed

    def execute_blocks(self):
        """
        Execute all the blocks sequentially.
        """
        print("Executing hotkey automation...")
        for block in self.blocks:
            block.execute()
        print("Automation completed.")

# Example BlockBase class to demonstrate execution
class BlockBase:
    def __init__(self, block_type, delay=0):
        self.block_type = block_type
        self.delay = delay

    def execute(self):
        print(f"Executing block: {self.block_type}")
        if self.delay > 0:
            time.sleep(self.delay)

if __name__ == "__main__":
    # Example usage with mock blocks
    block1 = BlockBase("Mouse Click", delay=1)
    block2 = BlockBase("Keyboard Input", delay=2)
    block3 = BlockBase("Wait", delay=3)

    blocks = [block1, block2, block3]

    # Create HotkeyRunner instance and start listening for hotkey
    runner = HotkeyRunner(blocks)
    runner.run()
