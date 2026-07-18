from functions.write_file import write_file

if __name__ == "__main__":
    test_cases = (
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    )
    for test_case in test_cases:
        print("\nTest case:", test_case)
        print(write_file(*test_case))
