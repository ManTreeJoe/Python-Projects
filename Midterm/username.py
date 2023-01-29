

# put your function here
def makeusername(first,last):
    first = firstname.title()
    last = lastname.title()
    username = last[0:3] + first[0:3] +'7'
    return username

    


firstname = input("Give me a first name: ")
lastname = input("Give me a last name: ")

print("Computer System name is:", makeusername(firstname,lastname))