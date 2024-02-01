import sqlite3

connector = sqlite3.connect('parduotuve.db')
cursor = connector.cursor()

def create_tables(connector: sqlite3.Connection, cursor: sqlite3.Cursor):

    queries = ['''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        price INTEGER
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(25),
        last_name VARCHAR(25)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS bill (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purchase_date_time DATETIME,
        cashier_id INTEGER,
        customer_id INTEGER REFERENCES customer(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS bill_line (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bill_id INTEGER REFERENCES bill(id),
        product_id INTEGER REFERENCES product(id),
        quantity INTEGER
    );
    '''
    ]

    for query in queries:
        cursor.execute(query)

    connector.commit()

def insert_product(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Inserting product')
    name = input('Product name: ')
    price = input('Product price: ')
    cursor.execute('INSERT INTO product (name, price)'
                   'VALUES (?, ?)', (name, price))
    connector.commit()
    print('Done')

def insert_customer(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Inserting customer')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    cursor.execute('INSERT INTO customer (first_name, last_name)'
                   'VALUES (?, ?)', (first_name, last_name))
    connector.commit()
    print('Done')

def product_list(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Product list: ')
    with connector:
        cursor.execute('SELECT * FROM product')
        products = cursor.fetchall()
    for product in products:
        print(f'{product}')

def customer_list(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Customer list: ')
    with connector:
        cursor.execute('SELECT * FROM customer')
        customers = cursor.fetchall()
    for customer in customers:
        print(f'{customer}')

if __name__ == '__main__':
    create_tables(connector, cursor)
    while True:
        choice = input('Enter command (cl or commands for command list): ')
        if choice.lower() in ['cl', 'commands']:
            print('cl, command list')
            print('ip, insert product')
            print('ic, insert customer')
            print('prl, product list')
            print('cul, customer list')
        if choice.lower() in ['ip', 'insert product']:
            insert_product(connector, cursor)
        if choice.lower() in ['ic', 'insert customer']:
            insert_customer(connector, cursor)
        if choice.lower() in ['prl', 'product list']:
            product_list(connector, cursor)
        if choice.lower() in ['cul', 'customer list']:
            customer_list(connector, cursor)

connector.close()