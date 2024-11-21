import tkinter as tk
from tkinter import ttk

class CustomTheme:
    def __init__(self, root):
        self.root = root
        self.setup_theme()

    def setup_theme(self):
        # Create a custom style for ttk widgets
        style = ttk.Style()
        
        # Set a theme
        style.theme_use("clam")
        
        # Customize button appearance
        style.configure("TButton", 
                        background="#4CAF50", 
                        foreground="white", 
                        font=("Helvetica", 12, "bold"), 
                        padding=10)
        
        # Customize label appearance
        style.configure("TLabel", 
                        background="#f0f0f0", 
                        foreground="#333", 
                        font=("Helvetica", 10))
        
        # Customize frame appearance
        style.configure("TFrame", 
                        background="#e0e0e0")
        
        # Customize canvas appearance (if needed)
        self.root.configure(bg="#e0e0e0")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Theme Example")
    root.geometry("400x300")
    
    # Apply custom theme
    custom_theme = CustomTheme(root)
    
    # Add some widgets to see the theme
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    label = ttk.Label(frame, text="This is a custom-themed label.")
    label.pack(pady=10)
    
    button = ttk.Button(frame, text="Click Me")
    button.pack(pady=10)
    
    root.mainloop()
