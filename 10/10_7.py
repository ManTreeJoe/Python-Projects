print('Input two numbers when prompted below.')
print('If you would like to quit, enter "q"\n')

while True:
    

    try:
        a = input('First number: ') 

        if a == 'q':
            break

        a = int(a)


        b = input('Second number: ')
        if b == 'q':
            break

        b = int(b) 


    except ValueError:
        print('tHaTs nOT A nuMbEr!\n')

    else:
        total = a + b
        print(f'{a} + {b} = {total}')
