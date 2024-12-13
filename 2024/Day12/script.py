def convert_to_graph(input_str):  
    return [list(row.strip()) for row in input_str.strip().split('\n')] 

def find_connected(graph, start_row, start_col, char):  
    if (start_row < 0 or start_row >= len(graph) or  
        start_col < 0 or start_col >= len(graph[0]) or  
        graph[start_row][start_col] != char):  
        return 0, 0  

    visited = set()  
    stack = [(start_row, start_col)]  
    area = 0  
    perimeter = 0  

    while stack:  
        row, col = stack.pop()  

        if (row, col) in visited:  
            continue  

        visited.add((row, col))  
        area += 1  

        # Check all adjacent cells  
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
            new_row, new_col = row + dr, col + dc  

            # If out of bounds, add to perimeter  
            if (new_row < 0 or new_row >= len(graph) or  
                new_col < 0 or new_col >= len(graph[0])): 
                perimeter += 1  
                continue  

            # If different character, add to perimeter  
            if graph[new_row][new_col] != char:  
                perimeter += 1  
                continue  

            # If same character and not visited, add to stack  
            if (new_row, new_col) not in visited:  
                stack.append((new_row, new_col))  

    return area, perimeter  

def find_regions(graph):  
    regions = []  
    processed = set()  

    for row in range(len(graph)):  
        for col in range(len(graph[0])):  
            if (row, col) not in processed:  
                char = graph[row][col]  
                area, perimeter = find_connected(graph, row, col, char)  
                if area > 0:  
                    regions.append((char, area, perimeter))  
                    # Mark all cells of this region as processed  
                    stack = [(row, col)]  
                    while stack:  
                        r, c = stack.pop()  
                        if (r, c) not in processed:  
                            processed.add((r, c))  
                            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
                                nr, nc = r + dr, c + dc  
                                if (0 <= nr < len(graph) and 
                                    0 <= nc < len(graph[0]) and  
                                    graph[nr][nc] == char):  
                                    stack.append((nr, nc))  

    return regions  

# Test the code  
input_str = '''AAAA
BBCD
BBCC
EEEC'''


# input_str = '''OOOOO  
# OXOXO  
# OOOOO  
# OXOXO  
# OOOOO''' 

# input_str = '''RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE'''

# with open('input.txt', 'r') as file:
#     input_str = file.read()

graph = convert_to_graph(input_str)  
regions = find_regions(graph) 
print(regions)
print(sum(area * perimeter for char, area, perimeter in regions))  