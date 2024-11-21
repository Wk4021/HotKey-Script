from blocks.block_base import BlockBase
import pyautogui

class CoordinateBlock(BlockBase):
    def __init__(self, coordinates, description="Click at specified coordinates"):
        """
        Initialize a CoordinateBlock with coordinates (x, y).
        """
        super().__init__(block_type="Coordinate Block", description=description)
        self.coordinates = coordinates

    def execute(self):
        """
        Execute the action of clicking at the specified coordinates.
        """
        x, y = self.coordinates
        print(f"Clicking at coordinates: ({x}, {y})")
        pyautogui.click(x, y)

    def __str__(self):
        """
        String representation of the CoordinateBlock.
        """
        return f"{super().__str__()}, Coordinates: {self.coordinates}"

# Example usage of CoordinateBlock
if __name__ == "__main__":
    # Create a CoordinateBlock instance
    block = CoordinateBlock((100, 200))
    print(block)
    block.execute()
