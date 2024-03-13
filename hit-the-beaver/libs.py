import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_NAME) + 6)
    
    print(style)
    print(f"** {PC_NAME} **")
    print(style)
    
def exit_program():
    print('Program will be stop')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program was successfully stoped')
    exit()
    
if __name__ == '__main__':
    welcome_message()
    exit_program()