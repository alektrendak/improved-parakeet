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


def run(code):
    bracket_map = parse_brackets(code)
    tape = [0] * 100000
    address_pointer = 0
    program_pointer = 0
    while program_pointer < len(code):
        instruction = code[program_pointer]
        match instruction:
            case ">":
                address_pointer += 1
            case "<":
                address_pointer -= 1
            case "+":
                tape[address_pointer] += 1
            case "-":
                tape[address_pointer] -= 1
            case ".":
                print(chr(tape[address_pointer]))
            case ",":
                tape[address_pointer] = ord(input())
            case "[":
                if tape[address_pointer] == 0:
                    program_pointer = bracket_map[program_pointer]
            case "]":
                if tape[address_pointer] != 0:
                    program_pointer = bracket_map[program_pointer]
        program_pointer += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 improved-parakeet.py <file_path>")
    else:
        run(read_file(sys.argv[1]))
