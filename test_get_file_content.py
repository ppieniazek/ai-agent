from functions.get_file_content import get_file_content

if __name__ == "__main__":
    test_cases = (
        ("calculator", "lorem.txt"),
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),
    )

    lorem = get_file_content(*test_cases[0])
    print(f"{test_cases[0][1]} length: {len(lorem)}")
    print(f"{test_cases[0][1]} truncated: {'truncated' in lorem}")
    for test_case in test_cases[1:]:
        print(f"\nTest case: {test_case}")
        print(get_file_content(*test_case))
