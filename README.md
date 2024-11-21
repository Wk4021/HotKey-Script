# Hotkey Script Playground

The Hotkey Script Playground is a Python tool for creating automation workflows via a visual drag-and-drop interface. Users can design custom hotkey scripts with blocks like keyboard actions, mouse clicks, and timers, then save and execute these workflows, simplifying repetitive tasks without coding.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)

## Introduction
The Hotkey Script Playground allows users to create powerful automation scripts with ease. Whether you want to automate repetitive tasks or create customized workflows, this tool makes it possible without writing code. Just drag and drop blocks like keyboard inputs, mouse clicks, timers, and more to create custom workflows that can be saved, modified, and executed as needed.

## Features
- **Drag-and-Drop Interface**: Easily create automation workflows by dragging functional blocks onto the canvas.
- **Block Types**: Includes actions like mouse clicks, keyboard inputs, coordinate tracking, and wait timers.
- **Script Management**: Save, load, and delete automation workflows for reuse.
- **No Coding Required**: Build powerful hotkey scripts visually without writing a single line of code.

## Setup
To get started with the Hotkey Script Playground, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/username/HotkeyScriptPlayground.git
   cd HotkeyScriptPlayground
   ```

2. **Install Dependencies**
   Make sure Python 3.8+ is installed. Then install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Project Structure**
   The repository has the following structure:
   ```
   HotkeyScriptPlayground/
   ├── main.py
   ├── ui/
   ├── blocks/
   ├── playground/
   ├── hotkey_management/
   ├── internal_logic/
   ├── assets/
   └── requirements.txt
   ```

   Ensure all folders contain an `__init__.py` file so they are recognized as Python packages.

## How to Run
To run the Hotkey Script Playground:

1. **Navigate to the Parent Directory**
   ```sh
   cd path/to/HotkeyScriptPlayground
   ```

2. **Run the Project**
   Use Python to run the main module:
   ```sh
   python -m HotkeyScriptPlayground.main
   ```

3. **User Interface**
   The application will open a GUI window. You can start creating automation workflows by dragging blocks from the toolbar onto the canvas and connecting them to define the flow.

## Usage
- **Add Blocks**: Click and drag blocks (e.g., mouse, keyboard, wait) from the sidebar to the playground area.
- **Connect Blocks**: Link blocks together to define the execution sequence.
- **Save Workflows**: Save your custom workflow for future use.
- **Load Workflows**: Load previously saved workflows to continue editing or running them.
- **Execute**: Use a hotkey or button to run the workflow.

## Customization
If you need to add new types of blocks or change the behavior of existing ones, follow these steps:
- **Create a New Block**: Add a new Python file in the `blocks/` directory and define your new block class, inheriting from `BlockBase`.
- **Update UI**: Update `block_ui.py` to include the new block type in the drag-and-drop interface.
- **Update Backend**: Modify `backend.py` to ensure the new block can be saved, loaded, and executed properly.

## Troubleshooting
- **Import Errors**: Make sure you are running the project from the directory **above** `HotkeyScriptPlayground` and use the `-m` flag to run it as a module.
- **Missing Packages**: Ensure all required packages are installed using `pip install -r requirements.txt`.
- **File Not Found**: Ensure all directories contain `__init__.py` files, and that you are using absolute imports within the project.

Feel free to open issues or contribute to the project to improve functionality. Enjoy automating with ease!

