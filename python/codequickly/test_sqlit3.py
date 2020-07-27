# ======
# SQLite 
# ======

import sqlite3

# Connect
# =======

connection = sqlite3.connect('test_sqlite3.db')

c = connection.cursor()

# Writer
# ======

c.execute("CREATE TABLE IF NOT EXISTS table1(hats, shirts, pants, shoes, glasses)")

c.execute("INSERT INTO table1 VALUES('Baseball', 'Henley', 'Khakis', 'Sneakers', 'Sunglasses')")

connection.commit()

# Reader
# ======

c.execute("SELECT * FROM table1")

fetchedData = c.fetchall()

print(fetchedData)

# Disconnect
# ==========

c.close()

connection.close()
