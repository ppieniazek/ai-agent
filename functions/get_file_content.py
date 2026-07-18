import os

from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_fp = os.path.normpath(os.path.join(abs_wd, file_path))
        if os.path.commonpath([abs_wd, abs_fp]) != abs_wd:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_fp):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_fp, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return file_content

    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
