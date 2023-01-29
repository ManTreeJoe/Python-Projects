line = '_________________________'
#list of places i would visit
places_to_go = ['Romania', 'Germany', 'Switzerland', 'Zion, California', 'Japan', 'Mammoth, California']

#printing the list
print(places_to_go, '\n')
print(line)

#sorting list alphabetically
alph = sorted(places_to_go)

print(alph)
print(line)

#printing original list
print('Original List')
print(places_to_go, '\n')

#divider line
print(line)

#reversing order of list
places_to_go.reverse()

print('Reversed List')
print(places_to_go,'\n')

#divider line
print(line)

#returning list to original form
places_to_go.reverse()

print('Original List')
print(places_to_go)

#divider line
print(line)

#removing first variable in list after alphabetized
places_to_go.remove(sorted(places_to_go)[0])

print('Removed first variable in list after alphabetized')
print(places_to_go)

#divider line
print(line)

#alphabetizing list
places_to_go.sort()

print('Alphabetized')
print(places_to_go)

#divider line
print(line)

#reverse alphabetical order
places_to_go.sort(reverse = True)

print('Reverse alphabetical order')
print(places_to_go)

#divider line
print(line)
