import re

with open('input.txt', 'r') as f:
    diskmap = [int(char) for char in f.read().strip()]

# diskmap = [int(char) for char in '12345']
# diskmap = [int(char) for char in '2333133121414131402']
# print('Initial diskmap:', ''.join(map(str, diskmap)))  

blocks = []
blockmap = []
file_id = 0

for k, v in enumerate(diskmap):
    if k % 2 == 0:
        for i in range(v):
            blockmap.append(file_id)
        file_id +=1
    else:
        free_space = k
        for i in range(v):
            blockmap.append('.')

# print('Initial blockmap:', ''.join(map(str, blockmap)))  
iteration = 0

while not re.match(r'^\d+\.+$', ''.join(map(str, blockmap))):
    print(f"\nIteration {iteration}")  


    # Find rightmost number and leftmost dot  
    rightmost_number_idx = None  
    leftmost_dot_idx = None  

    for i in range(len(blockmap)):  
        if blockmap[i] == '.' and leftmost_dot_idx is None:  
            leftmost_dot_idx = i  
        if blockmap[i] != '.' and leftmost_dot_idx is not None:  
            rightmost_number_idx = i    
    # If we found a number after a dot, swap them  
    if rightmost_number_idx is not None and leftmost_dot_idx is not None:  
        left, right = leftmost_dot_idx, rightmost_number_idx
        blockmap[left], blockmap[right] =  blockmap[right], blockmap[left]  
    else:  
        break  # No more swaps needed   
    # print('Current blockmap:', ''.join(map(str, blockmap)))  
    iteration += 1  

# print('Final blockmap:', ''.join(map(str, blockmap)))  

def calculate_checksum(blockmap):
    checksum = 0
    for i, char in enumerate(blockmap):
        if char != '.':
            checksum += int(char) * i
    return checksum

checksum = calculate_checksum(blockmap)
print('Checksum:', checksum)

