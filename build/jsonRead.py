import json

def readJson():
    file_path = './config/configFile.json'
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

def getFromConfig(nested_key):
    json_data = readJson()
    keys = nested_key.split('.')
    try:
        value = json_data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        print(f"Error: Key '{nested_key}' not found in JSON data.")
        return None

