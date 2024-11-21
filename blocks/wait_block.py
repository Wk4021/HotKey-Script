from .block_base import BlockBase
import time

class WaitBlock(BlockBase):
    def __init__(self, duration, description="Wait for a specified duration"):
        """
        Initialize a WaitBlock with a specified duration in seconds.
        """
        super().__init__(block_type="Wait Block", description=description)
        self.duration = duration

    def execute(self):
        """
        Execute the wait action for the specified duration.
        """
        print(f"Waiting for {self.duration} seconds...")
        time.sleep(self.duration)
        print("Wait completed.")

    def __str__(self):
        """
        String representation of the WaitBlock.
        """
        return f"{super().__str__()}, Duration: {self.duration} seconds"

# Example usage of WaitBlock
if __name__ == "__main__":
    # Create a WaitBlock instance
    block = WaitBlock(3)
    print(block)
    block.execute()