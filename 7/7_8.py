sammy_orders = ['BLT', 'Ham n Cheese sammy', 'PB & J', 'Tuna sammy', 'Egg Mc Muffin']

finished_sammies = []

while sammy_orders:
    current_sammy =  sammy_orders.pop()
    print('Your '+ current_sammy +' is currelntly being made.\n')
    finished_sammies.append(current_sammy)
print('\n')
for sammy in finished_sammies:
    print('Your ' + sammy + ' has been completed to perfection.\n')





