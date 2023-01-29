riv = {"Colorado": "U.S.", "Ganges":"India", "Volga":"Russia" }

for x in riv:
    country = riv[x].title()
    print(f"The river {x} is in {country}")

print('The following rivers are in the dictionary:')
for y in riv:
    print('-', y)

print('The following countries are in the dictionary:')
for z in riv:
    country = riv[z].title()
    print('-',country)