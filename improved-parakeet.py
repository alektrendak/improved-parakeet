import sys

code = ""


def read_file(file_path):
    global code
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 improved-parakeet.py <file_path>")
    else:
        read_file(sys.argv[1])
        print(code)
