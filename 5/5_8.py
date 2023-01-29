user_names = ['Admin','U1', 'U2', 'U3', 'U4', 'Joe']



if len(user_names):
       

  for x in user_names:
    if x == user_names[0]:
        print('Hello admin, would you like to view your portfolio today?')
    else:
        print('Hello', x, 'thank you for logging in once more')

else:
    print('We need to find some users!')
