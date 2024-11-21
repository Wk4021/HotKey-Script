import tkinter as tk
from tkinter import ttk, Canvas
from blocks.block_base import BlockBase
from blocks.coordinate_block import CoordinateBlock
from blocks.keyboard_block import KeyboardBlock
from blocks.mouse_block import MouseBlock
from blocks.wait_block import WaitBlock

class BlockUI:
    def __init__(self, root):
        self.root = root
        self.blocks = []  # Initialize the blocks list to keep track of all blocks added to the playground
        self.block_positions = {}  # Keep track of original positions of blocks for resizing calculations
        self.setup_ui()
        
        # Bind the window resize event to handle resizing
        self.root.bind("<Configure>", self.on_window_resize)

    def setup_ui(self):
        # Create a canvas for the playground area
        self.canvas = Canvas(self.root, bg="lightgray", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add instructions label
        instructions = ttk.Label(self.root, text="Drag and drop blocks here to create your automation flow.")
        instructions.pack(side=tk.TOP, pady=5)

        # Add example blocks
        self.create_draggable_block("Mouse Block", 50, 50, MouseBlock("click"))
        self.create_draggable_block("Keyboard Block", 50, 120, KeyboardBlock("Hello, World!"))
        self.create_draggable_block("Wait Block", 50, 190, WaitBlock(3))
        self.create_draggable_block("Coordinate Block", 50, 260, CoordinateBlock((100, 200)))

    def create_draggable_block(self, block_name, x, y, block_instance):
        # Create a draggable block as a rectangle with text
        block = self.canvas.create_rectangle(x, y, x + 120, y + 50, fill="blue", tags=block_name)
        text = self.canvas.create_text(x + 60, y + 25, text=block_name, fill="white", tags=block_name)
        
        # Store the original position for resizing calculations
        self.block_positions[block] = (x, y)

        # Bind mouse events for dragging
        self.canvas.tag_bind(block_name, "<ButtonPress-1>", self.on_block_press)
        self.canvas.tag_bind(block_name, "<B1-Motion>", self.on_block_drag)
        
        # Store the block instance for later use
        self.blocks.append(block_instance)

    def on_block_press(self, event):
        # Store the current position of the block when clicked
        self._drag_data = {"x": event.x, "y": event.y}

    def on_block_drag(self, event):
        # Compute the difference and move the block
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        
        # Update drag data
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        # Move the block
        items = self.canvas.find_withtag(tk.CURRENT)
        for item in items:
            self.canvas.move(item, dx, dy)

    def on_window_resize(self, event):
        # Calculate scaling factors for resizing
        width_scale = event.width / self.canvas.winfo_width()
        height_scale = event.height / self.canvas.winfo_height()

        # Update the canvas size
        self.canvas.config(width=event.width, height=event.height)

        # Rescale and reposition each block
        for block_id, (original_x, original_y) in self.block_positions.items():
            new_x = original_x * width_scale
            new_y = original_y * height_scale
            dx = new_x - original_x
            dy = new_y - original_y

            # Move the blocks proportionally
            self.canvas.move(block_id, dx, dy)

        # Update the canvas size in block_positions
        for block_id in self.block_positions:
            coords = self.canvas.coords(block_id)
            self.block_positions[block_id] = (coords[0], coords[1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Block UI Playground")
    root.geometry("1000x700")
    block_ui = BlockUI(root)
    root.mainloop()
