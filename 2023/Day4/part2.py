def parse_card(line):
    card_part, numbers_part = line.split(':')
    # Extract actual card number from "Card N:"
    card_num = int(card_part.split()[1])
    winning_numbers, my_numbers = numbers_part.split('|')

    winning_set = set(int(num) for num in winning_numbers.split())
    my_set = set(int(num) for num in my_numbers.split())

    return card_num, winning_set, my_set

def calculate_points_and_copies(filename):
    total_points = 0
    card_counts = {}  # Track number of each card
    card_matches = {}  # Store matches for each card
    max_card_num = 0

    # First pass: Calculate points and store matches
    with open(filename, 'r') as file:
        for line in file:
            card_num, winning_set, my_set = parse_card(line)
            matches = len(winning_set & my_set)
            max_card_num = max(max_card_num, card_num)

            # Calculate points for part 1
            if matches > 0:
                total_points += 2 ** (matches - 1)

            # Store matches and initialize card count
            card_matches[card_num] = matches
            card_counts[card_num] = 1

    # Process copies
    for card_num in range(1, max_card_num + 1):
        current_copies = card_counts[card_num]
        matches = card_matches[card_num]

        # Add copies to subsequent cards
        for i in range(matches):
            next_card = card_num + i + 1
            if next_card in card_counts:
                card_counts[next_card] += current_copies

    total_cards = sum(card_counts.values())

    return total_points, total_cards

# Read and process the input
filename = 'input.txt'
points, total_scratchcards = calculate_points_and_copies(filename)

print(f"Part 1 - Total points: {points}")
print(f"Part 2 - Total scratchcards: {total_scratchcards}")
