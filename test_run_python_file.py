from functions.run_python_file import run_python_file

if __name__ == "__main__":
    test_cases = (
        ("calculator", "main.py", None),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py", None),
        ("calculator", "../main.py", None),
        ("calculator", "nonexistent.py", None),
        ("calculator", "lorem.txt", None),
    )
    for test_case in test_cases:
        print(f"Testing case: {test_case}")
        print(run_python_file(*test_case))
