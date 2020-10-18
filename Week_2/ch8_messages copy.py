def show_messages(unsent_messages, sent_messages):
    """
    Simulate sending messages and moving sent messages to sent_messages when complete
    """
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    """
    Show all sent messages
    """
    print("\nThe following messages were sent:")
    for sent_message in sent_messages:
        print(sent_message)


unsent_messages = ['Never stop looking up.','Love, not hate.','Life is a mystery.','Stay positive.','You inspire me.','All you need is love.']
sent_messages = []

show_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)

print(f"These are the messages in before being sent: {unsent_messages}.")
print(f"These are the messages that were sent: {sent_messages}.")