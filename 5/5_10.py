current_users = ['Nate', 'Tree', 'Joe', 'Styan', 'Man','Jeff']



copy_lower = [x.lower() for x in current_users]
copy_upper = [x.upper() for x in current_users]


new_users = ['TREE', 'man', 'David', 'Sam', 'Broseph']

for i in new_users:
      if (i in current_users) | (i in copy_lower) | (i in copy_upper):
           print('Unfortinatly, the username', i, 'is currently unavalable.\nPlease enter new username\n')
      else:
        print('Congragulations! This username is avalable!\n')



