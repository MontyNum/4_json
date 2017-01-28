# Pretty print for a json file
This script provides a capability to “pretty-print” arbitrary json file.

**load_data(***filepath***)** 

    Downloads data.json from the file path directory and returns deserialized a Python object.

**pretty_print_json(***data***)**

    The function implements pretty printing, where data is a Python object.

# Usage

Entering the path of the interesting json file:

    file_path = 'c://file_derectory//file_name.json'

Loading the data:

    json_content = load_data(file_path)
    
Pretty printing:

    print(pretty_print_json(json_content))
    
