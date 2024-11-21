from .block_base import BlockBase
import pyautogui

class MouseBlock(BlockBase):
    def __init__(self, action, coordinates=None, description="Perform mouse action"):
        """
        Initialize a MouseBlock with an action and optional coordinates.
        """
        super().__init__(block_type="Mouse Block", description=description)
        self.action = action
        self.coordinates = coordinates

    def execute(self):
        """
        Execute the mouse action (click, double click, right click, etc.).
        """
        if self.action == "click":
            if self.coordinates:
                x, y = self.coordinates
                print(f"Clicking at coordinates: ({x}, {y})")
                pyautogui.click(x, y)
            else:
                print("Clicking at current mouse position")
                pyautogui.click()
        elif self.action == "double_click":
            if self.coordinates:
                x, y = self.coordinates
                print(f"Double clicking at coordinates: ({x}, {y})")
                pyautogui.doubleClick(x, y)
            else:
                print("Double clicking at current mouse position")
                pyautogui.doubleClick()
        elif self.action == "right_click":
            if self.coordinates:
                x, y = self.coordinates
                print(f"Right clicking at coordinates: ({x}, {y})")
                pyautogui.rightClick(x, y)
            else:
                print("Right clicking at current mouse position")
                pyautogui.rightClick()
        else:
            print(f"Unknown action: {self.action}")

    def __str__(self):
        """
        String representation of the MouseBlock.
        """
        coord_str = f" at coordinates: {self.coordinates}" if self.coordinates else " at current position"
        return f"{super().__str__()}, Action: {self.action}{coord_str}"

# Example usage of MouseBlock
if __name__ == "__main__":
    # Create a MouseBlock instance
    block = MouseBlock("click", (150, 250))
    print(block)
    block.execute()