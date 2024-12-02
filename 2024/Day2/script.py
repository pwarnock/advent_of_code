import os

def read_input(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

def is_valid_difference(diff):
    return 1 <= abs(diff) <= 3

def check_sequence_safety(levels):
    def check_with_skip(skip_index=None):
        is_increasing = None

        for i in range(len(filtered_levels) - 1):
            diff = filtered_levels[i] - filtered_levels[i+1]

            # Check difference range
            if not is_valid_difference(diff):
                return False

            # Check direction consistency
            current_increasing = diff > 0
            if is_increasing is not None and current_increasing != is_increasing:
                return False
            is_increasing = current_increasing

        return True
    
    # Try the sequence as-is
    filtered_levels = levels
    if check_with_skip():
        return True
    
    # Try removing each level once
    for i in range(len(levels)):
        filtered_levels = levels[:i] + levels[i+1:]
        if check_with_skip():
            return True
        
    return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data = read_input(os.path.join(script_dir, 'input.txt'))

    safe = unsafe = 0 

    for report in data:
        levels = list(map(int, report.split()))
        if check_sequence_safety(levels):
            safe += 1
        else:
            unsafe += 1
    
    print(f"Safe sequences: {safe}")
    print(f"Unsafe sequences: {unsafe}")
    
if __name__ == "__main__":
    main()
