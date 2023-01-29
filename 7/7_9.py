sammy_orders = ['Pastrami sammy', 'BLT', 'Ham n Cheese sammy', 'Pastrami sammy', 'PB & J', 'Tuna sammy', 'Egg Mc Muffin', 'Pastrami sammy']

finished_sammies = []

print('Unfortinatly, we have run outy of pastrami sammies\n')

while 'Pastrami sammy' in sammy_orders:
    sammy_orders.remove('Pastrami sammy')

while sammy_orders:
    current_sammy =  sammy_orders.pop()
    print('Your '+ current_sammy +' is currelntly being made.\n')
    finished_sammies.append(current_sammy)
print('\n')
for sammy in finished_sammies:
    print('Your ' + sammy + ' has been completed to perfection.\n')

