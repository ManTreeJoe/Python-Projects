
prompt = 'Please enter age '
prompt += "\nIf finished, enter '0.1': "




while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print('\nYour ticket is free of charge.\n Enjoy the movie!\n')

    elif age < 13:
        print('\nYour ticket will be $10.\n Enjoy the movie!\n')

    else:
        print('\nYour ticket will be $15.\n Enjoy the movie!\n')

    
