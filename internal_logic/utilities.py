import os
import json

def ensure_directory_exists(path):
    """
    Ensure that the directory at the specified path exists.
    If it does not exist, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def save_json(file_path, data):
    """
    Save data to a JSON file.
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")


def load_json(file_path):
    """
    Load data from a JSON file.
    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            print(f"Data successfully loaded from {file_path}")
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return None


def format_coordinates(x, y):
    """
    Format coordinates (x, y) into a string representation.
    """
    return f"({x}, {y})"


def delay_execution(seconds):
    """
    Delay the execution by a specified number of seconds.
    """
    import time
    print(f"Delaying execution for {seconds} seconds...")
    time.sleep(seconds)
    print("Resuming execution.")

if __name__ == "__main__":
    # Example usage of utilities
    ensure_directory_exists("example_folder")
    save_json("example_folder/data.json", {"example_key": "example_value"})
    loaded_data = load_json("example_folder/data.json")
    if loaded_data:
        print(loaded_data)
    print(format_coordinates(100, 200))
    delay_execution(2)
