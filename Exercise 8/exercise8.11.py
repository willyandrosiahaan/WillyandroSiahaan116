
def message(show_message, send_message):
    while show_message:
        current_message = show_message.pop()
        print(f"Sending message: {current_message}")
        send_message.append(current_message)


def show_sent_messages(send_message):
    print("\nThe following messages have been sent:")
    for message in send_message:
        print(message)


show_message = ['Hello', 'How are you?', 'Goodbye']
send_message = []

message(show_message.copy(), send_message)

print("\nOriginal messages:")
print(show_message)

print("\nSent messages:")
print(send_message)

show_sent_messages(send_message)
