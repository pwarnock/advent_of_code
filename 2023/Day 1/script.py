import re
import os

words_to_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_numbers(text):
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    matches = re.finditer(pattern, text)
    numbers = []

    for match in matches:
        pos = match.start()
        # Check for word numbers
        found_word = False
        for word in words_to_numbers.keys():
            if text[pos:].startswith(word):
                numbers.append(word)
                found_word = True
                break
        # Check for digits - only if no word was found
        if not found_word and text[pos].isdigit():
            numbers.append(text[pos])

    return numbers

def main():
    total_calibration_value = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, 'input.txt')

    with open(input_file_path, 'r') as file:
        for line in file:
            valid_digits = find_numbers(line.strip())
            if valid_digits:
                first_digit = valid_digits[0]
                last_digit = valid_digits[-1]

                # Convert to numbers using the dictionary for words
                first_value = words_to_numbers[first_digit] if first_digit.isalpha() else int(first_digit)
                last_value = words_to_numbers[last_digit] if last_digit.isalpha() else int(last_digit)

                # Concatenate the two values
                calibration_value = int(f"{first_value}{last_value}")

                # Debugging output
                print(f"Line: {line.strip()} First: {first_digit} Last: {last_digit} Value: {calibration_value}")

                total_calibration_value += calibration_value

    print("Total Calibration Value:", total_calibration_value)

if __name__ == "__main__":
    main()