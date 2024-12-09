import re

with open('input.txt', 'r') as f:
    diskmap = [int(char) for char in f.read().strip()]

# diskmap = [int(char) for char in '12345']
# diskmap = [int(char) for char in '2333133121414131402']
# print('Initial diskmap:', ''.join(map(str, diskmap)))  

blockmap = []  

# Create initial blockmap  
for k, v in enumerate(diskmap):  
    if k % 2 == 0:  
        blockmap.extend([k // 2] * v)  # Use k // 2 as file_id  
    else:  
        blockmap.extend(['.'] * v)  

print('Initial blockmap:', ''.join(map(str, blockmap)))  

# Two-pointer approach to rearrange  
left = 0  
right = len(blockmap) - 1  

while left < right:  
    # Move left pointer to the right until we find a dot  
    while left < right and isinstance(blockmap[left], int):  
        left += 1  
    # Move right pointer to the left until we find a number  
    while left < right and blockmap[right] == '.':  
        right -= 1  
    # Swap if left is still less than right  
    if left < right:  
        blockmap[left], blockmap[right] = blockmap[right], blockmap[left]  

print('Final blockmap:', ''.join(map(str, blockmap)))  

def calculate_checksum(blockmap):
    checksum = 0
    for i, char in enumerate(blockmap):
        if char != '.':
            checksum += int(char) * i
    return checksum

checksum = calculate_checksum(blockmap)
print('Checksum:', checksum)

