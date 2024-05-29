import json

def print_json_structure(json_obj, indent=0):
    """Recursively print the keys and types in the JSON object."""
    indent_str = '  ' * indent  # Indentation for nested levels

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            print(f"{indent_str}{key}: ({type(value).__name__})")
            if isinstance(value, (dict, list)):
                print_json_structure(value, indent + 1)
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            print(f"{indent_str}[{index}]: ({type(item).__name__})")
            if isinstance(item, (dict, list)):
                print_json_structure(item, indent + 1)

def main():
    # Load JSON from a file
    file_path = 'patternnet.json'  # Replace with your JSON file path
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    # Print the structure of the JSON
    print_json_structure(json_data)
    print(json_data["test"])


main()
