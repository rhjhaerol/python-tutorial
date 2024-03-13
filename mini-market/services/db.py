import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_market"
)

def inser_item(item_code, item_name, item_price, item_stock):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO item_tbl (item_code, item_name, item_price, item_stock) \
                   VALUES (%s, %s, %s, %s)", (item_code, item_name, item_price, item_stock))
    mydb.commit()

    if cursor.rowcount > 0:
        print("\nData added successfully!")
    else:
        print("\nData failed to added!")

def check_item():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM item_tbl")
    
    return cursor.fetchall()