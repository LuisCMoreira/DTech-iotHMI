import json

def read_json_file():
    file_path = 'configFile.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{file_path}': {e}")
        return None

def get_value_from_nested_key(nested_key):
    json_data = read_json_file()
    keys = nested_key.split('.')
    try:
        value = json_data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        print(f"Error: Key '{nested_key}' not found in JSON data.")
        return None

