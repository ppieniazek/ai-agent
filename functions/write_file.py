import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if it exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_fp = os.path.normpath(os.path.join(abs_wd, file_path))
        if os.path.commonpath([abs_wd, abs_fp]) != abs_wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_fp):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(abs_fp), exist_ok=True)

        with open(abs_fp, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'
