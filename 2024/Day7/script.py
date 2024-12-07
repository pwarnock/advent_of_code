
input = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

with open('input.txt') as f:
    input = f.read()

lines = input.split('\n')
parsed_input = []
for line in lines:
    parts = line.split(': ')
    key = int(parts[0])
    values = list(map(int, parts[1].split()))
    parsed_input.append((key, values))

valid_keys = {}

total = 0
for key, values in parsed_input:
    from itertools import product

    operations = ['+', '*', '||']
    permutations = list(product(operations, repeat=len(values)-1))
    for permutation in permutations:
        result = values[0]
        for i, value in enumerate(values[1:]):
            if permutation[i] == '+':
                result += value
            elif permutation[i] == '*':
                result *= value
            elif permutation[i] == '||':
                result = int(f'{result}{value}')
        if result == key:
            print(f"Expression: {' '.join(map(str, values))} {' '.join(permutation)} = {key}")
            valid_keys[key] = result

total += sum(valid_keys.values())
print(total)

