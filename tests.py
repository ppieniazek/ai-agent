from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

get_files_info_cases = (
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
    ("non_existing", None),
    ("/", "am_i_here?"),
)

for work_dir, end_dir in get_files_info_cases:
    print(f'CASE: working_directory="{work_dir}", directory="{end_dir}"')
    print(get_files_info(work_dir, end_dir), end="\n\n")

get_file_content_cases = (
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
)

for work_dir, file_path in get_file_content_cases:
    print(f'CASE: working_directory="{work_dir}", file_path="{file_path}"')
    print(get_file_content(work_dir, file_path), end="\n\n")
