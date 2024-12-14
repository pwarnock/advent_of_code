import re

input = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

with open('input.txt', 'r') as file:
    input = file.read()


class Cost:
    A = 3
    B = 1

class Button:
    def __init__(self, name, x, y, cost):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.cost = cost
    
    def __str__(self):
        return f"Button {self.name}(x={self.x}, y={self.y}, cost={self.cost})"

class PrizeLocation:
    def __init__(self, x, y, offset=0):
        self.x = int(x) + offset 
        self.y = int(y) + offset 
    
    def __str__(self):
        return f"Prize(x={self.x}, y={self.y})"

class Machine:
    def __init__(self, buttonA: Button, buttonB: Button, prize_location: PrizeLocation):
        self._buttonA = buttonA
        self._buttonB = buttonB
        self._prize_location = prize_location
    
    @property
    def buttonA(self) -> Button:
        return self._buttonA

    @buttonA.setter
    def buttonA(self, value: Button):
        self._buttonA = value

    @property
    def buttonB(self) -> Button:
        return self._buttonB

    @buttonB.setter
    def buttonB(self, value: Button):
        self._buttonB = value

    @property
    def prize_location(self) -> PrizeLocation:
        return self._prize_location

    @prize_location.setter
    def prize_location(self, value: PrizeLocation):
        self._prize_location = value

def calculate_button_presses(machine: Machine):
    """
    Calculate the number of times to press buttons A and B to reach the prize.
    Returns (presses_a, presses_b) or (None, None) if no solution exists.
    """
    # We need to solve:
    # a * buttonA.x + b * buttonB.x = prize_location.x
    # a * buttonA.y + b * buttonB.y = prize_location.y
    # where a and b are the number of times to press each button

    # Using matrix algebra:
    # | buttonA.x  buttonB.x | | a | = | prize_location.x |
    # | buttonA.y  buttonB.y | | b |   | prize_location.y |

    determinant = (machine.buttonA.x * machine.buttonB.y - 
                  machine.buttonA.y * machine.buttonB.x)

    if determinant == 0:
        return None, None

    presses_a = (machine.prize_location.x * machine.buttonB.y - 
                 machine.prize_location.y * machine.buttonB.x) / determinant

    presses_b = (machine.buttonA.x * machine.prize_location.y - 
                 machine.buttonA.y * machine.prize_location.x) / determinant

    # Check if we got whole numbers
    if not (presses_a.is_integer() and presses_b.is_integer()):
        return None, None

    # Check if both numbers are non-negative
    if presses_a < 0 or presses_b < 0:
        return None, None

    return int(presses_a), int(presses_b)

def calculate_cost(machine: Machine):
    presses_a, presses_b = calculate_button_presses(machine)
    if presses_a is None or presses_b is None:
        return None, None, None
    cost_a = presses_a * machine.buttonA.cost
    cost_b = presses_b * machine.buttonB.cost
    return cost_a, cost_b, cost_a + cost_b



def generate_machine_records(input_str):
    records = input_str.strip().split('\n\n')
    for record in records:
        lines = record.split('\n')
        
        # Parse Button A
        buttonA_match = re.match(r'^Button A: X\+(\d+), Y\+(\d+)$', lines[0])
        buttonA = buttonA_match.groups()
        
        # Parse Button B
        buttonB_match = re.match(r'^Button B: X\+(\d+), Y\+(\d+)$', lines[1])
        buttonB = buttonB_match.groups()
        
        # Parse Prize Location
        prize_match = re.match(r'^Prize: X=(\d+), Y=(\d+)$', lines[2])
        prize_location = prize_match.groups()
        
        yield buttonA, buttonB, prize_location

machines = []
total_cost = 0

for buttonA, buttonB, prize_location in generate_machine_records(input):
    buttonA = Button('A', buttonA[0], buttonA[1], Cost.A)
    buttonB = Button('B', buttonB[0], buttonB[1], Cost.B)
    prize_location = PrizeLocation(prize_location[0], prize_location[1], offset=10000000000000)
    machine = Machine(buttonA, buttonB, prize_location)
    machines.append(machine)
    presses_a, presses_b = calculate_button_presses(machine)
    cost_a, cost_b, subtotal = calculate_cost(machine)
    if subtotal:
        total_cost += subtotal
    print(f"Button A: {machine.buttonA}")
    print(f"Button B: {machine.buttonB}")
    print(f"Prize Location: {machine.prize_location}")
    print(f"Button A Presses: {presses_a}, Cost: {cost_a}")
    print(f"Button B Presses: {presses_b}, Cost: {cost_b}")
    print(f"Cost to win game: {subtotal}")

print(total_cost)