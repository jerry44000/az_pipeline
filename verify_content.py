# verify_content.py
import os
import json

def check_json_content(filename):
    if not os.path.isfile(filename):
        return False

    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            if 'content' in data and isinstance(data['content'], bool):
                return data['content']
        except json.JSONDecodeError:
            pass

    return False

if __name__ == "__main__":
    file_to_check = "sample_file.json"
    result = check_json_content(file_to_check)
    print(f"Content is : {result}")
