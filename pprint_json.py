import chardet
import json
import sys
import os

def load_data(json_file_path):
    if not os.path.exists(json_file_path):
        print('There is no such path or file. Exiting...')
        sys.exit()
    with open(json_file_path, 'rb') as file_handler:
        encoding = chardet.detect(file_handler.readline())['encoding']
    with open(json_file_path, 'r', encoding=encoding) as file_handler:
        return json.load(file_handler)
              
def pretty_print_json(json_content):
    print(json.dumps(json_content, indent=4, sort_keys=True, ensure_ascii=False))

    
if __name__ == '__main__':
    file_path = input('Enter file path: ')
    json_content = load_data(file_path)
    pretty_print_json(json_content)
