people = []

person = {"first_name":"Ela", "last_name":"Bupte", "age": "13", "city": "riverside"}
people.append(person)
person = {'first_name':'Jake', 'last_name':'Bodea', 'age':'19', 'city':'fountain valley'}
people.append(person)
person = {'first_name':'Bethany', 'last_name':'marinau', 'age':'17', 'city':'east vale'}
people.append(person) 



for person in people:
    name = person['first_name'].title() + ' ' + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(f"\n{name}, who is {age}, is from {city}")

print('\n')
    