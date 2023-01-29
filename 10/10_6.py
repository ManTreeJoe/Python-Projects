print('Input two numbers when prompted below.\n')

try:
   first = input('First number: ') 
   first = int(first)
   sec = input('Second number: ')
   sec = int(sec)

except ValueError:
   print('tHaTs nOT A nuMbEr!')

else:
    total = first + sec
    print(f'{first} + {sec} = {total}')

    