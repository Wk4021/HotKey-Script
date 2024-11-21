from blocks.block_base import BlockBase
import pyautogui

class KeyboardBlock(BlockBase):
    def __init__(self, key_sequence, description="Type specified keys"):
        """
        Initialize a KeyboardBlock with a sequence of keys to type.
        """
        super().__init__(block_type="Keyboard Block", description=description)
        self.key_sequence = key_sequence

    def execute(self):
        """
        Execute the action of typing the specified key sequence.
        """
        print(f"Typing key sequence: {self.key_sequence}")
        pyautogui.typewrite(self.key_sequence)

    def __str__(self):
        """
        String representation of the KeyboardBlock.
        """
        return f"{super().__str__()}, Key Sequence: {self.key_sequence}"

# Example usage of KeyboardBlock
if __name__ == "__main__":
    # Create a KeyboardBlock instance
    block = KeyboardBlock("Hello, World!")
    print(block)
    block.execute()
