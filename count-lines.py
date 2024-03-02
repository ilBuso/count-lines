import os

def print_file(file_path, root_path):
    relative_path = os.path.relpath(file_path, root_path)
    print("\t" + os.path.basename(root_path) + os.path.sep + relative_path)

def count_lines_of_code(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if line.strip():
                                total_lines += 1
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError: Unable to read file: {file_path}")
                    continue
                print_file(file_path, directory)
    return total_lines

if __name__ == "__main__":
    directory = input(f"Enter the path to the directory: ")
    print("\n*****\n")
    total_lines = count_lines_of_code(directory)
    print("\n*****\n")
    print("Stats:")
    print(f"\n - Total lines of code: {total_lines}")
    print("\n")
