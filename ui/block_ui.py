import tkinter as tk
from tkinter import ttk, Canvas, simpledialog, messagebox
from blocks.coordinate_block import CoordinateBlock
from blocks.keyboard_block import KeyboardBlock
from blocks.mouse_block import MouseBlock
from blocks.wait_block import WaitBlock

class BlockUI:
    SNAP_THRESHOLD = 30  # Distance threshold for snapping blocks

    def __init__(self, root):
        self.root = root
        self.blocks = []  # List of tuples (canvas_id, block_instance)
        self.setup_ui()

    def setup_ui(self):
        # Create a canvas for the playground area that expands with the window
        self.canvas = Canvas(self.root, bg="lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add Start and Stop buttons
        start_button = ttk.Button(self.root, text="Start", command=self.start_execution)
        start_button.pack(side=tk.LEFT, padx=10, pady=5)

        stop_button = ttk.Button(self.root, text="Stop", command=self.stop_execution)
        stop_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Add instructions label
        instructions = ttk.Label(self.root, text="Drag and drop blocks to create your automation flow.")
        instructions.pack(side=tk.BOTTOM, pady=5)

        # Add example blocks in a horizontal layout
        self.create_static_block("Mouse Block", 50, 50, MouseBlock("click"))
        self.create_static_block("Keyboard Block", 200, 50, KeyboardBlock("Hello, World!"))
        self.create_static_block("Wait Block", 350, 50, WaitBlock(3))
        self.create_static_block("Coordinate Block", 500, 50, CoordinateBlock((100, 200)))

    def create_static_block(self, block_name, x, y, block_instance):
        """Create a static block that can be used to generate copies in the playground."""
        # Create a static block for the user to copy
        block = self.canvas.create_rectangle(x, y, x + 120, y + 50, fill="blue", tags=block_name)
        text = self.canvas.create_text(x + 60, y + 25, text=block_name, fill="white", tags=block_name)

        # Bind mouse events for dragging and copying
        self.canvas.tag_bind(block_name, "<ButtonPress-1>", lambda e, b=block_instance: self.create_draggable_block(e, b))

    def create_draggable_block(self, event, block_instance):
        """Create a draggable copy of the block."""
        # Determine the starting position for the new block
        x, y = event.x, event.y
        block_name = block_instance.__class__.__name__

        # Create a new draggable block on the canvas
        block = self.canvas.create_rectangle(x, y, x + 120, y + 50, fill="green", tags="draggable")
        text = self.canvas.create_text(x + 60, y + 25, text=block_name, fill="white", tags="draggable")

        # Store the block instance for later use
        self.blocks.append((block, block_instance))

        # Bind mouse events for dragging the new block
        self.canvas.tag_bind("draggable", "<ButtonPress-1>", self.on_block_press)
        self.canvas.tag_bind("draggable", "<B1-Motion>", self.on_block_drag)
        self.canvas.tag_bind("draggable", "<ButtonPress-3>", lambda e, b=block_instance: self.edit_block_settings(b))

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

        # Move the block and associated text
        items = self.canvas.find_withtag(tk.CURRENT)
        for item in items:
            self.canvas.move(item, dx, dy)

        # Optional: Snap blocks if needed (can be enhanced later)
        self.check_snap(items[0])

    def check_snap(self, block_id):
        """Snap blocks together if they are close enough."""
        x, y = self.canvas.coords(block_id)[0:2]

        for other_block, _ in self.blocks:
            if other_block == block_id:
                continue

            other_x, other_y = self.canvas.coords(other_block)[0:2]

            # Check if the block is close enough to snap horizontally to another block
            if abs(x - (other_x + 130)) < self.SNAP_THRESHOLD and abs(y - other_y) < self.SNAP_THRESHOLD:
                dx = (other_x + 130) - x
                dy = other_y - y
                self.canvas.move(block_id, dx, dy)

    def edit_block_settings(self, block_instance):
        """Open a dialog to edit settings for a given block."""
        if isinstance(block_instance, MouseBlock):
            action = simpledialog.askstring("Edit Mouse Block", "Enter new action (e.g., click, double-click):")
            if action:
                block_instance.action = action
        elif isinstance(block_instance, KeyboardBlock):
            keys = simpledialog.askstring("Edit Keyboard Block", "Enter new keys to type:")
            if keys:
                block_instance.keys = keys
        elif isinstance(block_instance, WaitBlock):
            duration = simpledialog.askinteger("Edit Wait Block", "Enter new duration (seconds):")
            if duration is not None:
                block_instance.duration = duration
        elif isinstance(block_instance, CoordinateBlock):
            x = simpledialog.askinteger("Edit Coordinate Block", "Enter new X coordinate:")
            y = simpledialog.askinteger("Edit Coordinate Block", "Enter new Y coordinate:")
            if x is not None and y is not None:
                block_instance.coordinates = (x, y)

    def start_execution(self):
        messagebox.showinfo("Start", "Starting the automation flow.")
        # Logic to start the automation flow (to be implemented)

    def stop_execution(self):
        messagebox.showinfo("Stop", "Stopping the automation flow.")
        # Logic to stop the automation flow (to be implemented)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Block UI Playground")
    root.geometry("1200x800")
    block_ui = BlockUI(root)
    root.mainloop()
