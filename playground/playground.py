import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from blocks.block_base import BlockBase
from blocks.coordinate_block import CoordinateBlock
from blocks.keyboard_block import KeyboardBlock
from blocks.mouse_block import MouseBlock
from blocks.wait_block import WaitBlock


class Playground:
    def __init__(self, root):
        self.root = root
        self.setup_playground()
        self.blocks = []  # List to keep track of all blocks in the playground
        self.connections = []  # List to track connections between blocks

    def setup_playground(self):
        # Create a frame for the playground
        self.playground_frame = ttk.Frame(self.root, padding="10")
        self.playground_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas inside the playground frame
        self.canvas = Canvas(self.playground_frame, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add a label at the top
        self.instructions = ttk.Label(self.playground_frame, text="Connect blocks here to create your automation flow.")
        self.instructions.pack(side=tk.TOP, pady=5)

        # Event bindings to allow connecting blocks
        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Track the connections
        self.lines = []
        self.current_line = None

    def add_block(self, block_instance, x, y):
        """
        Add a block to the playground at specified coordinates.
        """
        block_name = block_instance.block_type
        block = self.canvas.create_rectangle(x, y, x + 120, y + 50, fill="blue", tags=block_name)
        text = self.canvas.create_text(x + 60, y + 25, text=block_name, fill="white", tags=block_name)
        
        # Store the block instance and add to block list
        self.blocks.append(block_instance)

    def on_click(self, event):
        # Start drawing a line to connect blocks
        self.current_line = self.canvas.create_line(event.x, event.y, event.x, event.y, fill="black", width=2)

    def on_drag(self, event):
        # Update the end of the current line while dragging
        if self.current_line:
            coords = self.canvas.coords(self.current_line)
            self.canvas.coords(self.current_line, coords[0], coords[1], event.x, event.y)

    def on_release(self, event):
        # Stop drawing the line and save it
        if self.current_line:
            self.lines.append(self.current_line)
            self.current_line = None
            # Here we could implement logic to determine which blocks are connected by the line
            # and add those connections to self.connections

    def get_execution_order(self):
        """
        Determine the execution order of blocks based on connections.
        """
        # Placeholder for execution order logic based on connections
        # Currently, we return the blocks in the order they were added
        return self.blocks

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Playground Example")
    root.geometry("1000x700")
    playground = Playground(root)

    # Example of adding blocks to the playground
    playground.add_block(MouseBlock("click"), 100, 100)
    playground.add_block(KeyboardBlock("Hello"), 300, 100)
    playground.add_block(WaitBlock(2), 500, 100)
    playground.add_block(CoordinateBlock((150, 200)), 700, 100)

    root.mainloop()
