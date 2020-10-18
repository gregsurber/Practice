filename = 'guest_book.txt'
guest_name = input("What is your name? ")
with open(filename, 'a') as file_object:
    file_object.write(guest_name + '\n')
