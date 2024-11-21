import pyautogui
import tkinter as tk
from tkinter import ttk

class CoordinateFinder:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Create a frame for the coordinate finder tool
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Label to display instructions
        self.instructions_label = ttk.Label(self.frame, text="Press the button below and move your mouse to the desired location to find coordinates.")
        self.instructions_label.pack(pady=5)

        # Button to start finding coordinates
        self.find_button = ttk.Button(self.frame, text="Find Coordinates", command=self.find_coordinates)
        self.find_button.pack(pady=5)

        # Label to display found coordinates
        self.coordinates_label = ttk.Label(self.frame, text="Coordinates: (x, y)")
        self.coordinates_label.pack(pady=5)

    def find_coordinates(self):
        """
        Get the current mouse position and display the coordinates.
        """
        # Wait for 3 seconds to allow the user to move their mouse to the desired location
        self.root.after(3000, self.get_mouse_position)
        self.instructions_label.config(text="Move your mouse to the desired location within 3 seconds.")

    def get_mouse_position(self):
        # Get mouse coordinates using pyautogui
        x, y = pyautogui.position()
        self.coordinates_label.config(text=f"Coordinates: ({x}, {y})")
        self.instructions_label.config(text="Press the button below to find coordinates again.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Coordinate Finder Tool")
    root.geometry("400x200")

    # Create CoordinateFinder instance
    coordinate_finder = CoordinateFinder(root)

    root.mainloop()
