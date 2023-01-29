prompt = 'Please input toppings. \nType quit to finish: '

toppings = []   

active = True
print("type of active is:", type(active))
while active:
    top = input(prompt)

    if top == 'quit':
        print(f'{toppings} are on the pizza.')
        active = False
    else:
        toppings.append(top)
        print(f'\n{top} will be added to your pizza\n')
    
