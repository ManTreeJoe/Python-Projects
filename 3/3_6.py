guest_list = ['Josh A.', 'Jake B.', 'Michael B.', 'David G.']

#secont half of invite.
message_1 = ", You have been invited to Nathan's estate for dinner tonight at 6:00 pm."

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )

print('______________\n')

print("Unfortinatly,", guest_list[1],"will no longer be joining us.\n\n")

guest_list[1] = 'Abram of Canon'

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )

print('______________\n')

msg_table = "I have just recently recieved a larger dining table from an unknown donor."
"Because of this, I will be inviting more guests for dinner."

print(msg_table, '\n\n')

guest_list.insert(0, 'Charlie Chapmin')
guest_list.insert(2, 'Felix Kjelberg')
guest_list.insert(6, 'Jesus of Nazereth')

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )