from random import choice

series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]

winning_ticket = []

print('\n')

print("And the winning ticket number is...")

while len(winning_ticket) < 4:
    pulled_item = choice(series)


    if pulled_item not in winning_ticket:
        print(f"{pulled_item}!")
        winning_ticket.append(pulled_item)

print('The Winning ticket number is: ', winning_ticket)

print('\n')