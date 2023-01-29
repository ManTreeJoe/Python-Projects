gender = ['Male', 'Female']

residence = ['Orange County', 'LA County', 'Riverside County']


students = [(x,y) for x in gender for y in residence if x !=y]

print('\n', students, '\n')