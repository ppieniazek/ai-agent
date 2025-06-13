import os


def get_files_info(working_directory, directory=None):
    if not os.path.exists(working_directory):
        return f'Error: "{working_directory}" directory does not exist!'
    abs_work_dir = os.path.abspath(working_directory)

    if directory is not None:
        abs_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not os.path.exists(abs_dir):
            return f'Error: "{directory}" directory does not exist!'
        if not abs_dir.startswith(abs_work_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_dir):
            return f'Error: "{directory}" is not a directory'
    else:
        abs_dir = abs_work_dir
    try:
        dir_contents = []
        for file in os.listdir(abs_dir):
            abs_file_path = os.path.join(abs_dir, file)
            dir_contents.append(
                f"- {file}: file_size={os.path.getsize(abs_file_path)} bytes, is_dir={os.path.isdir(abs_file_path)}"
            )
        return "\n".join(dir_contents)
    except Exception as e:
        return f"Error: {e}"
