from functions.get_files_info import get_files_info


def main() -> None:
    test_cases = (
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    )

    for test_case in test_cases:
        print(f"Result for '{test_case[1]}' directory:")
        print(get_files_info(*test_case))


if __name__ == "__main__":
    main()
