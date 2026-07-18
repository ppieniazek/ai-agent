import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_target = os.path.normpath(os.path.join(abs_wd, directory))
        valid_target = os.path.commonpath([abs_wd, abs_target]) == abs_wd
        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        files_info: list[str] = []
        for item in os.listdir(abs_target):
            abs_item = os.path.join(abs_target, item)
            files_info.append(
                f"- {item}: file_size={os.path.getsize(abs_item)} bytes, is_dir={os.path.isdir(abs_item)}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
