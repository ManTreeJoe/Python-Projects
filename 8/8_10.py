messages = ['AAAAAAAAAAAAaaaaaaaAAAAA', 'You best not let me fall, for your sake', 'It is time', 'Just Follow the yellow brick road']
sent_messages = []

def show_messages(messages):
    print("Showing all messages: ")
    for message in messages:
        print(message)
print('\n')
def send_messages(messages, sent_messages):
    
    print("\nSending messages:")
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)


    

show_messages(messages)

send_messages(messages, sent_messages)

print('\nEnd products:')
print(messages, '\n')
print(sent_messages)

print('\n')