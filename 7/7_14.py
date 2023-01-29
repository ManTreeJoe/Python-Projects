famous_peeps = []

person = {"first_name":"Tom", "last_name":"Hiddleson", "birth_date": "Feburary 9, 1981", "birth_place":"London, UK", "quote": "Never stop. Never stop fighting. Never stop dreaming"}
famous_peeps.append(person)
person = {'first_name':'Abraham', 'last_name':'Lincoln', 'birth_date':'Febuary 12, 1809', 'birth_place':'Ilinois', 'quote':'Folks are usually about as happy as they make their mind up to be.'}
famous_peeps.append(person)
person = {'first_name':'Nicholae', 'last_name':'Ceausescu', 'birth_date':'January 26, 1918', 'birth_place':'Romania','quote':'The fetus is property of the entire society'}
famous_peeps.append(person) 



for person in famous_peeps:
    name = person['last_name'].title() + ', ' + person['first_name'].title()
    birthDate = person['birth_date'].title()
    birthPlace = person['birth_place'].title()
    quote = person['quote'].title()

    print(f'{name}   {birthDate}  {birthPlace} \n     {quote}\n ')
print('\n')
    