guest_list = [ 'Michael B.', 'David G.']

line = '___________________________'

#secont half of invite.
message_1 = ", You have been invited to Nathan's estate for dinner tonight at 6:00 pm."

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )

print(line, '\n')

print("Unfortinatly,", guest_list[1],"will no longer be joining us due to them needing to do a backflip.\n\n")

guest_list[1] = 'Abram of Canon'

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )

print(line, '\n')

msg_table = "I have just recently recieved a larger dining table from an unknown donor. Because of this, I will be inviting more guests for dinner."

print(msg_table, '\n\n')

guest_list.insert(0, 'Charlie Chapmin')
guest_list.insert(2, 'Felix Kjelberg')
guest_list.insert(4, 'Jesus of Nazereth')

#for loop to print invites
for x in guest_list:
    print('Hello', x, message_1,'\n' )

print(line, '\n')

msg_table = "Unfortinatly the new table has been transformed back into a tree meaning I only have room for 2 guest"

print(msg_table,'\n\n')

print('The length of Guest List: ', len(guest_list), '\n')

guest_list.pop(0)
guest_list.pop(0)
guest_list.pop(2)

message_2 = 'you are one of the remaining two guest still invited.'
#for loop to print invites
for x in guest_list:
    print('Hello', x, message_2,'\n' )

print(line, '\n')


guest_list.remove('Abram of Canon')

print(guest_list)

del(guest_list[0])

print(guest_list)
print(line)