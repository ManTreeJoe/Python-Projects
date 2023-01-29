fav_pizza = ['peperoni', 'barbecue', 'ham and hotsause']

for pizza in fav_pizza:
    print(pizza)


for pizza in fav_pizza:
    print('I enjoy eating', pizza, 'pizza')

msg = 'Pizza is amazing.'

print(msg)

msg = 'My favorites are'


print(msg, fav_pizza[0],',', fav_pizza[1],'&,', fav_pizza[2], "\nI'm in love with pizza\n")


friend_pizza = fav_pizza.copy()


fav_pizza.insert(0, 'breakfast')

friend_pizza.insert(0,'hawaiian')


print('My favorite pizzas are:')
for pizza in fav_pizza:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

    