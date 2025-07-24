from pathlib import Path
import time
import subprocess
import argparse
from typing import List


def prompt_file_path() -> Path:
    while True:
        file_path = Path(input("Input path of the file you want to test: "))
        if file_path.exists() and file_path.is_file():
            return file_path
        print(f"Invalid file path: {file_path}. Please try again.")


def get_files_by_extension(directory: str, extension: str) -> List[Path]:
    dir_path = Path(directory)

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: Directory '{directory}' does not exist.")
        exit(1)

    files = sorted(f for f in dir_path.iterdir() if f.is_file() and f.suffix == extension)
    return files


def run_test_case(executable: Path, input_file: Path, expected_file: Path, silent: bool, index: int):
    test_input = input_file.read_text().strip()
    expected_output = expected_file.read_text().strip()

    start_time = time.time()
    try:
        result = subprocess.run(
            [str(executable)],
            input=test_input,
            capture_output=True,
            text=True,
            shell=True  # Only necessary if it's a script/command line string
        )
    except Exception as e:
        print(f"{index}. ERROR running subprocess: {e}")
        return False

    actual_output = result.stdout.strip()
    elapsed_ms = int((time.time() - start_time) * 1000)

    success = actual_output == expected_output
    if not silent or not success:
        status = "SUCCESS" if success else "FAILED"
        message = f"{index}. {status} {input_file.stem} in {elapsed_ms}ms"
        if not success:
            message += f"\nExpected: {expected_output}\nReceived: {actual_output}"
        print(message)

    return success


def main():
    parser = argparse.ArgumentParser(description="Test runner for executable against input/output cases.")
    parser.add_argument('--silent', '-s', action='store_true', help="Only prints status if FAILED")
    parser.add_argument('--exec', '-e', type=str, help="Path to the executable")
    args = parser.parse_args()

    executable = Path(args.exec) if args.exec else prompt_file_path()

    if not executable.exists() or not executable.is_file():
        print(f"Error: Executable file '{executable}' does not exist.")
        exit(1)

    input_files = get_files_by_extension("./in", ".in")
    output_files = get_files_by_extension("./out", ".out")

    if len(input_files) != len(output_files):
        print("Error: The number of input and output files does not match.")
        exit(1)

    print(f"Number of test cases: {len(input_files)}")
    
    succes_count = 0
    fail_count = 0

    for i, (in_file, out_file) in enumerate(zip(input_files, output_files)):
        if in_file.stem != out_file.stem:
            print(f"Error: Filename mismatch: {in_file.name} vs {out_file.name}")
            exit(1)

        succes = run_test_case(executable, in_file, out_file, args.silent, i)
        
        if succes:
            succes_count += 1
        else:
            fail_count += 1

    print("TOTAL")
    print(f"SUCCES: {succes_count}")
    print(f"FAILS: {fail_count}")

if __name__ == "__main__":
    main()
