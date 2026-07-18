import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_fp = os.path.normpath(os.path.join(abs_wd, file_path))
        if os.path.commonpath([abs_wd, abs_fp]) != abs_wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_fp):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_fp.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_fp]
        if args:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=abs_wd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        output: list[str] = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output)

    except Exception as e:
        return f'Error executing Python file "{file_path}": {e} '
