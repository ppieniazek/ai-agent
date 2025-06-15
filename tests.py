from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

get_files_info_cases = (
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
    ("non_existing", None),
    ("/", "am_i_here?"),
)


def test_get_files_info():
    for work_dir, end_dir in get_files_info_cases:
        print(f'CASE: working_directory="{work_dir}", directory="{end_dir}"')
        print(get_files_info(work_dir, end_dir), end="\n\n")


get_file_content_cases = (
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
)


def test_get_file_content():
    for work_dir, file_path in get_file_content_cases:
        print(f'CASE: working_directory="{work_dir}", file_path="{file_path}"')
        print(get_file_content(work_dir, file_path), end="\n\n")


get_write_file_cases = (
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
)


def test_write_file():
    for work_dir, file_path, content in get_write_file_cases:
        print(
            f'CASE: working_directory="{work_dir}", file_path="{file_path}", content="{content}"'
        )
        print(write_file(work_dir, file_path, content), end="\n\n")


run_python_file_cases = (
    ("calculator", "main.py"),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
)


def test_run_python_file():
    for work_dir, file_path in run_python_file_cases:
        print(f'CASE: working_directory="{work_dir}", file_path="{file_path}"')
        print(run_python_file(work_dir, file_path), end="\n\n")


if __name__ == "__main__":
    # test_get_files_info()
    # test_get_file_content()
    # test_write_file()
    test_run_python_file()
