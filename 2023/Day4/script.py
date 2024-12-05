import pandas as pd

#     # Sample data as a string (you would read this from your text file)
#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#     Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#     Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#     Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#     Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#     Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#     """

def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.split('|')
            card_info = parts[0].split(':')[1].strip()
            winning_numbers = pd.DataFrame(list(map(int, card_info.split())))
            my_numbers = pd.DataFrame(list(map(int, parts[1].strip().split())))

            yield winning_numbers, my_numbers

def calculate_points(matches):
    if matches < 1:
        return 0
    return 2 ** (matches - 1)


total_points = 0
file_path = 'input.txt'
for winning_numbers, my_numbers in enumerate(parse_file(file_path)):
    scratchcards = my_winning_numbers = my_numbers[0].isin(winning_numbers[0]).sum()
    points = calculate_points(my_winning_numbers)
    total_points += points
    print(f"Points for {my_winning_numbers} matches: {points}")

    print(f"Total points: {total_points}")