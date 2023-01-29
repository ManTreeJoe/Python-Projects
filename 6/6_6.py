fav_lang = {'Nathan':'python', 'Jake':'Python', 'Andrei':'java script', 'phil':'c#'}

peeps = ['Nathan', 'Jake', 'Andrei', 'Phil', 'Michael', 'John']

for name in peeps:
    if name in fav_lang.keys():
        print(f"\nThank you {name} for taking the survey.") 
    else:
       print(f"\n{name}, what is your favorite coding language?")