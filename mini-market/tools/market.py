import main
from services import db

def add():
    item_code = input("Input item code: ")
    item_name = input("Input item name: ")
    item_price = int(input("Input item price: "))
    item_stock = int(input("Input item stock: "))

    db.inser_item(item_code, item_name, item_price, item_stock)

def check():
    items = db.check_item()
    for item in items:
        item_code = item[1]
        item_name = item[2]
        item_price = item[3]
        item_stock = item[4]
        print(f'\nCode: {item_code}\nName : {item_name}\nPrice : Rp.{item_price}\nStock : {item_stock}')

def start():
    while True:
        print('\nWelcome to Mini Market\n')
        menu = int(input('Select Menu:\n1. Add Item\n2. Check Item\n3. Back\n\nPlease select : '))

        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            print("Please select an existing number!")


if __name__ == '__main__':
    start()