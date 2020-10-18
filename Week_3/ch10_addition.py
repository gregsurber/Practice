print("Give me two numbers, and I will add them for you./n")
print("Enter 'q' to quit.")


while True:
    first_num = input("Enter your first number: ")  # gets first number from user
    if first_num == 'q':    # if the user wants to quit, they can put in a 'q' here
        break               # if they put in a 'q', the program ends
    second_num = input("Enter your second number: ")    # gets second number  from user
    if second_num == 'q':   # if they want to quit, they can put in a 'q'
        break               # if they put in a 'q', the program ends
    try:                    # attempt to do the math (which will fail if they didn't put in 2 integers)
        total = int(first_num) + int(second_num)    # gives the output of the addition
    except ValueError:      # if they put in non-integers, this will catch it
        print("numbers only")   # and tell them to only use numbers
    else:                   # if they put in two integers, this will run
        print(f"The total for those two numbers is: {total}")   # and this will print the total to the screen
