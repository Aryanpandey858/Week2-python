"""JSON File Reader: load JSON data and print formatted output."""
import json


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def print_formatted(data, indent=0):
    """Recursively print dictionaries and lists in a readable format."""
    space = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{space}{key}:")
                print_formatted(value, indent + 1)
            else:
                print(f"{space}{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                print(f"{space}-")
                print_formatted(item, indent + 1)
            else:
                print(f"{space}- {item}")
    else:
        print(f"{space}{data}")


def main():
    print("=== JSON File Reader ===")
    filename = input("Enter JSON file name (press Enter for data.json): ").strip()
    if not filename:
        filename = "data.json"

    try:
        data = load_json(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return

    print("\n--- Formatted Output ---")
    print_formatted(data)

    print("\n--- Pretty JSON ---")
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()