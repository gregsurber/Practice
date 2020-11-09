def clear_screen():
    # calling these three functions will clear any extra noise from the screen and re-draw the board, with 
    # all moves still showing
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
    print_header()
    board.display()