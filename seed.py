import sqlite3
import hashlib
from model import SALT
import time

conn = sqlite3.connect("ttrader.db")
cur  = conn.cursor()

hasher = hashlib.sha512()
hasher.update((SALT + 'password!').encode('utf-8'))
pass_hash = hasher.hexdigest()

SQL = """INSERT INTO accounts 
    (username, firstname, lastname, 
    account_id, pass_hash, balance) 
    VALUES
    (?, ?, ?, ?, ?, ?); """

cur.execute(SQL, ('carter', 'Carter', 'Adams',
                  '000001', pass_hash, 10000.00))

SQL = """ INSERT INTO positions
    (account_pk, symbol, amount)
    VALUES
    (?, ?, ?); """

cur.execute(SQL, (1, 'tsla', 5))

SQL = """ INSERT INTO trades
    (account_pk, symbol, volume, price, time)
    VALUES
    (?, ?, ?, ?, ?); """

cur.execute(SQL, (1, 'tsla', 5, 100.00, int(time.time())))

conn.commit()
conn.close()
