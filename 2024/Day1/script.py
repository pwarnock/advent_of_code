import os

def read_input(data):
    """Parses the input data into two lists."""
    left_list = []
    right_list = []
    for line in data.strip().splitlines():
        if line.strip():  # Skip empty lines
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    """Calculates the total distance between two lists."""

    # Calculate distances for each pair
    total_distance = 0

    for i in range(len(left_list)):
        left_val = left_list[i]
        right_val = right_list[i]
        distance = abs(left_val - right_val)
        total_distance += distance

    return total_distance

def calculate_similarity_score(left_list, right_list):
    similarity_score = 0

    for x in left_list:
        similarity_score += x * right_list.count(x)

    return similarity_score


def main(data):
    # Parse the input into two lists
    left_list, right_list = read_input(data)

    # Calculate the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    similarity_score = calculate_similarity_score(left_list, right_list)

    print(f"\nTotal distance: {total_distance}")
    print(f"\nSimilarity Score: {similarity_score}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'input.txt'), "r") as file:
        data = file.read()
    main(data)