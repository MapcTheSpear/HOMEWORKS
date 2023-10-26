import sqlite3

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


def create_tablet(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_products(connection, product: tuple):
    sql = '''
        INSERT INTO products
        (product_title, price, quantity)
        VALUES (? ,? ,?)
        '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def add_products(connection):
    productss = [
        ("NVIDIA 3080", 500, 25),
        ("STEAMDECK", 550, 50),
        ("NINTENDO SWITCH", 670, 70),
        ("INTEL CORE I5", 999, 100),
        ("GAMER CHAIR", 250, 20),
        ("LOTION", 25, 120),
        ("MOUSE PAD", 10.20, 900),
        ("KEYBOARD", 90.15, 800),
        ("MONITOR", 250, 150),
        ("PLAYSTAION 5", 350, 12),
        ("XBOX SERIES X", 300, 13),
        ("JOYSTICK", 20.99, 50),
        ("CABLES", 12.99, 1200),
        ("MACBOOK", 650, 5),
        ("THUNDEROBOT", 698, 10)
    ]
    for producty in productss:
        create_products(connection, producty)

def update_quantity(connection, product_id, new_quantity):
    sql = '''UPDATE products SET quantity= ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_quantity, product_id))
    connection.commit()

def update_price(connection, product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, product_id))
    connection.commit()

def delete_product(connection, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (product_id,))
    connection.commit()

def select_products(connection):
    sql = '''SELECT * FROM products'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def select_product_by_price_and_quantity(connection, price, quantity):
    sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products_by_title(connection, title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (title, ))
    rows = cursor.fetchall()
    print(f"Products found by name {title}")
    for row in rows:
        print(row)


connection = create_connection("hw.db")

sql_create_products_tablet = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
);
'''

if connection:
    print("The connection is succesful.")
    create_tablet(connection, sql_create_products_tablet)
    # add_products(connection)
    delete_product(connection, 15)
    update_quantity(connection, 1, 100)
    update_price(connection, 2, 3000)
    # select_products(connection)
    # select_product_by_price_and_quantity(connection, 100, 5)
    search_products_by_title(connection, '%NVIDIA%')
    connection.close()

