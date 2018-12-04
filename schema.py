import sqlite3

CON = None
CUR = None

def setup(dbname="ttrader.db"):
    global CON
    global CUR
    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

def run():
    SQL = "DROP TABLE IF EXISTS accounts;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE accounts(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        firstname VARCHAR,
        lastname VARCHAR,
        account_id VARCHAR,
        pass_hash VARCHAR(128),
        balance FLOAT,
        CONSTRAINT unique_user_name UNIQUE(username),
        CONSTRAINT unique_account_id UNIQUE(account_id)
        );"""
    
    CUR.execute(SQL)
    
    SQL = "DROP TABLE IF EXISTS trades;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE trades(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        account_pk INTEGER,
        symbol VARCHAR,
        volume INTEGER,
        price FLOAT,
        time INTEGER,
        FOREIGN KEY(account_pk) REFERENCES accounts(pk)
        );"""
    
    CUR.execute(SQL)
    
    SQL = "DROP TABLE IF EXISTS positions;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE positions(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        account_pk INTEGER,
        symbol VARCHAR,
        amount INTEGER,
        FOREIGN KEY (account_pk) REFERENCES accounts(pk),
        CONSTRAINT unique_account_symbol UNIQUE (account_pk, symbol));""" 
    CUR.execute(SQL)
    
    CON.commit()
    CUR.close()
    CON.close()

if __name__ == "__main__":
    setup()
    run()
