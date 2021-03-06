import chardet
import json
import os

def load_data(json_file_path):
    if not os.path.exists(json_file_path):
        return None
    encoding = detect_encoding(json_file_path)
    with open(json_file_path, 'r', encoding=encoding) as file_handler:
        return json.load(file_handler)

def detect_encoding(file_path):
    with open(file_path, 'rb') as file_handler:
        encoding = chardet.detect(file_handler.readline())
        return encoding['encoding']
              
def pretty_print_json(json_content):
    return json.dumps(json_content, indent=4, sort_keys=True, ensure_ascii=False)

    
if __name__ == '__main__':
    file_path = input('Enter file path: ')
    json_content = load_data(file_path)
    if json_content:
        print(pretty_print_json(json_content))
    else:
        print('\nThe file or the file path does not exist.')
