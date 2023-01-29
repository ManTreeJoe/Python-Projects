from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

print('\n')

d6 = Die()

nums = []

for roll_num in range(10):
    num = d6.roll_dice()
    nums.append(num)

print(f"10 roles of a 6-sided die gets you \nthese numbers: \n{nums}")
print('\n')

d10 = Die(10)

nums = []

for roll_num in range(10):
    num = d10.roll_dice()
    nums.append(num)

print(f"10 roles of a 10-sided die gets you \nthese numbers: \n{nums}")
print('\n')

d20 = Die(20)

nums = []

for roll_num in range(10):
    num = d20.roll_dice()
    nums.append(num)

print(f"10 roles of a 20-sided die gets you \nthese numbers: \n{nums}")
print('\n')
