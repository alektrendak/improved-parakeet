import sys


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def parse_brackets(code):
    bracket_map = {}
    stack = []
    for i, char in enumerate(code):
        if char == "[":
            stack.append(i)
        elif char == "]":
            if len(stack) == 0:
                print("Error: Unbalanced brackets")
                return
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    if len(stack) > 0:
        print("Error: Unbalanced brackets")
    return bracket_map


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 improved-parakeet.py <file_path>")
    else:
        code = read_file(sys.argv[1])
        bracket_map = parse_brackets(code)
        print(code)
