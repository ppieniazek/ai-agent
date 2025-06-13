import os


def get_file_content(working_directory, file_path):
    if not os.path.exists(working_directory):
        return f'Error: "{working_directory}" directory does not exist!'

    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_work_dir, file_path))
    if not os.path.exists(abs_file_path):
        return f'Error: "{abs_file_path}" directory does not exist!'

    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == 10000:
                file_content_string += (
                    f'...File "{file_path}" truncated at 10000 characters'
                )
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
