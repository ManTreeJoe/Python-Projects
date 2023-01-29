all_users = ["It's", 'Tree', 'Man']

all_users.append('Joe')

untrusted_users = ["It's", 'Nate']

trusted_users = []

for users in all_users:
    if users not in untrusted_users:
        trusted_users.append(users)

for users in trusted_users:
    print('\n', users)

#set

all_users = {"It's", 'Joe', 'Man', 'Tree', 'Nate'}

untrusted_users = {'Joe', 'Stan'}

trusted_users = []

trusted_users = all_users - untrusted_users

print('\n', trusted_users)
