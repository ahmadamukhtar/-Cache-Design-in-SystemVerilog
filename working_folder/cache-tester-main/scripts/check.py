import argparse

def compare_files(file1_path, file2_path):
    """
    Compare two files line by line.

    Parameters:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.
    """
    diffs = 0
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

        if len(file1_lines) != len(file2_lines):
            print("Files have different number of lines.")
            return

        for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines)):
            if line1.strip() != line2.strip():
                diffs = diffs + 1
                print(f"Line {i + 1} differs:")
                print(f"{file1_path}: {line1.strip()}")
                print(f"{file1_path}: {line2.strip()}")
                print()
        
        print(f"Tests Completed \nDifferences -> {diffs}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two files line by line.')
    parser.add_argument('file1', type=str, help='Path to the first file')
    parser.add_argument('file2', type=str, help='Path to the second file')

    args = parser.parse_args()

    compare_files(args.file1, args.file2)
