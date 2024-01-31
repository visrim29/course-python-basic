import sqlite3

connector = sqlite3.connect('schema.db')
cursor = connector.cursor()

query = ['''
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

cursor.execute.__sql: list(query)
connector.commit()
connector.close()