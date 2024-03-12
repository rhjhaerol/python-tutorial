from libs import welcome_message, exit_program
from games import games

def menu():
    user_option = int(input("Menu Program:\n1. Games\n2. Exit\n\nPlease select: "))
    
    if user_option == 1:
        games.start()
    elif user_option == 2:
        exit_program()
    else:
        print('You can only choose what is available on the menu!')

def main():
    welcome_message()
    menu()
    
if __name__ == '__main__':
    main()