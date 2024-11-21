import tkinter as tk
from tkinter import ttk

def launch_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Hotkey Script Playground")
    root.geometry("800x600")

    # Create a frame for the block playground
    playground_frame = ttk.Frame(root, padding="10")
    playground_frame.pack(fill=tk.BOTH, expand=True)

    # Add a label to the playground
    label = ttk.Label(playground_frame, text="Drag and drop blocks here to create your automation flow", anchor=tk.CENTER)
    label.pack(fill=tk.BOTH, expand=True)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    launch_ui()
