import pprint


def welcome():
    """welcome message"""
    print("Welcome to Terminal Trader")

def main_menu_options():
    """main menu options display"""
    print("1. Create Account")
    print("2. Log In")
    print("3. Exit")

def menu_input():
    """input for menus"""
    return input("Your choice: ")

def bad_input():
    """generic bad input display"""
    print("Bad input, please try again")

def bad_credentials():
    """invalid login info message"""
    print("Invalid credentials")

def new_account_inputs():
    """inputs for accounts table- username, first name, last name, account_id, pass_hash, balance"""
    user_input = input("Username: ")
    fn_input = input("First name: ")
    ln_input = input("Last name: ")
    acc_id_input = input("Account ID: ")
    password_input = input("Password: ")
    balance_input = float(input("Starting balance: "))
    return (dict({'username' : user_input, 'firstname' : fn_input, 'lastname' : ln_input, 'account_id' : acc_id_input, 'pass_hash' : password_input, 'balance' : balance_input}))

def existing_username():
    """display for trying to create a username that already exists"""
    print("User already exists in accounts table")

def balance_needs_float():
    """bad user input when creating account"""
    print("Account balance must be a float")

def trader_menu():
    """post-login menu display"""
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Check Positions")
    print("4. Lookup Price")
    print("5. Buy Order")
    print("6. Sell Order")
    print("7. Order History")
    print("8. Log Out")

def login_inputs():
    """username/password inputs for login"""
    user_input = input("Username: ")
    password_input = input("Password: ")
    return (user_input, password_input)

def account_balance(balance):
    """print statement for account balance"""
    print("Account balance:", balance)

def deposit_input():
    """input amount to deposit"""
    dep_input = input("Amount to deposit: ")
    return dep_input

def print_positions(positions):
    """print current account's positions"""
    print(positions)

def ticker_input():
    """input for stock names"""
    tick_input = input("Stock: ")
    return tick_input

def print_lookup_price(price):
    """prints the price per share of a stock"""
    print(price)

def buy_amount():
    """number of shares of a stock to buy"""
    buy_input = input("Number of shares to buy: ")
    return buy_input

def sell_amount():
    """number of shares of a stock to sell"""
    sell_input = input("Number of shares to sell: ")
    return sell_input

def trade_history(trades):
    """print user's trade history"""
    pprint.pprint(trades)

def bad_buy():
    """invalid combination for a buy order"""
    print("Either incorrect stock symbol or not enough cash")

def bad_sell():
    """invalid combination for a sell order"""
    print("Either incorrect stock symbol or not enough shares")

def bad_stock_input():
    """invalid stock symbol"""
    print("Not a value stock symbol")