# Turbo Testing 3000

Turbo Testing 3000 is a command-line utility for automated testing of executable programs against multiple input/output test cases. It is designed to streamline the process of validating program correctness and performance, especially useful for competitive programming, algorithm challenges, or batch testing.

## Features

- **Automatic Test Discovery:** Scans `./in` and `./out` directories for `.in` and `.out` files.
- **Batch Execution:** Runs all test cases in sequence, matching input and output files by filename.
- **Performance Timing:** Reports execution time for each test case.
- **Silent Mode:** Optionally suppresses successful test output, showing only failures.
- **Custom Executable:** Specify the path to the executable to be tested.

## Usage

```sh
turbo.exe
```

### Arguments

- `--exec`, `-e`
  Path to the executable file to test. If not provided, you will be prompted to enter it.
- `--silent`, `-s`
  Only prints status if a test case fails.

## Test Case Structure

- Place input files (`*.in`) in the `./in` directory.
- Place corresponding output files (`*.out`) in the `./out` directory.
- Input and output files must have matching filenames (e.g., `test1.in` and `test1.out`).

## Example

```
├── main.py
├── in/
│   ├── test1.in
│   ├── test1a.in
│   ├── test1az.in
│   └── test2.in
├── out/
│   ├── test1.out
│   ├── test1a.out
│   ├── test1az.out
│   └── test2.out
```

## Output

For each test case, the script prints whether it succeeded or failed, along with execution time. At the end, a summary of total successes and failures is displayed.

## Requirements

- Python 3.6+
- The executable to be tested must accept input from stdin and output to stdout.

## License

MIT License

