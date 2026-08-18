import os

def get_file_info(working_directory,directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    if directory is None:
        directory = working_directory
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_dir):
        return f"Error: Directory {directory} is outside the working directory {working_directory}"

    final_response = ""
    contents = os.listdir(abs_directory)
    for item in contents:
        item_path = os.path.join(abs_directory, item)
        is_dir = os.path.isdir(item_path)
        size = os.path.getsize(item_path)
        final_response += f"Name: {item}, Type: {'Directory' if is_dir else 'File'}, Size: {size} bytes\n"
    return final_response

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}