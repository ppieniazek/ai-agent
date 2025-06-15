import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    if not os.path.exists(working_directory):
        return f'Error: "{working_directory}" directory does not exist!'

    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not (os.path.isfile(abs_file_path) and abs_file_path.endswith(".py")):
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        response = subprocess.run(
            commands,
            cwd=abs_work_dir,
            capture_output=True,
            timeout=30,
            text=True,
        )
        output = []

        if response.stdout:
            output.append(f"STDOUT:\n{response.stdout}")
        if response.stderr:
            output.append(f"STDERR:\n{response.stderr}")
        if response.returncode != 0:
            output.append(f"Process exited with code {response.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
