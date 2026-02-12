import os

def parse_input(filename):
    """Reads the input file and returns a list of lines/data."""
    input_path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(input_path, 'r') as f:
            # .strip() removes trailing newlines; .splitlines() handles different OS formats
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ Error: {filename} not found in the current directory.")
        return []

def solve_part_1(data):
    """Logic for the first star."""
    result = 0
    # Your logic here
    return result

def solve_part_2(data):
    """Logic for the second star."""
    result = 0
    # Your logic here
    return result

if __name__ == "__main__":
    # Load data
    puzzle_input = parse_input("input.txt")
    
    if puzzle_input:
        print(f"--- Day 01 ---")
        print(f"Part 1 Result: {solve_part_1(puzzle_input)}")
        print(f"Part 2 Result: {solve_part_2(puzzle_input)}")
