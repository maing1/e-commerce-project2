import sqlite3

CONN = sqlite3.connect('customer.db')
CURSOR = CONN.cursor()
