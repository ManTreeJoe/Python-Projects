
thou = [range(2, 1001)]

print("\nA list of prime #'s from 1 to 1000:")

for num in range(2,1001):
    prime = True
    for i in range(2,num):
       if(num % i == 0):
           prime = False
           if num in thou:
              thou.remove(num)
           


    if prime:
      print( num)



