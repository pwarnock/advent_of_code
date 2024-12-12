from collections import deque

def find_trailhead_info(matrix):
    rows, cols = len(matrix), len(matrix[0])
    total_score = 0
    total_rating = 0
    starting_points = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                starting_points.add((i, j))
                total_score += count_valid_paths(matrix, i, j)  
                total_rating += count_valid_paths(matrix, i, j, count_visited=False)
    return total_score, total_rating

def count_valid_paths(matrix, start_r, start_c, count_visited=True):
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start_r, start_c, 0)])
    paths_found = 0
    visited = set()

    while queue:
        r, c, current_val = queue.popleft()

        if (r, c) in visited:
            continue
        
        count_visited and visited.add((r, c))
        
        if matrix[r][c] != current_val:
            continue

        if matrix[r][c] == 9:
            paths_found += 1
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == current_val + 1:
                    queue.append((nr, nc, current_val + 1))
    
    return paths_found

def convert_to_matrix(input_str):
    lines = input_str.strip().split('\n') 
    # Convert each line into a list of integers  
    matrix = [[int(char) for char in line] for line in lines] 

    return matrix


input_str = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

with open('input.txt', 'r') as f:
    input_str = f.read()

matrix = convert_to_matrix(input_str)

total_score, trailhead_rating = find_trailhead_info(matrix)
print(f"Total Score: {total_score}")
print(f"Trailhead Rating: {trailhead_rating}")