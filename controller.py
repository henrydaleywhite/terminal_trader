import model
import view
# TODO update print statements for trader menu 3 + 7

def main_menu():
    """main menu for account creation/login"""
    while True:
        print()
        view.welcome()
        print()
        view.main_menu_options()
        try:
            mm_choice = int(view.menu_input())
        except ValueError:
            view.bad_input()
            continue
        if mm_choice not in (1, 2, 3):
            view.bad_input()
        # new user
        elif mm_choice == 1:
            # returns username, first name, last name, account_id, pass_hash, balance
            try:
                create_inputs = view.new_account_inputs()
            except ValueError:
                view.balance_needs_float()
                continue
            account = model.Account(create_inputs)
            account.set_hashed_password(account.pass_hash)
            account.save()
        # login
        elif mm_choice == 2:
            # returns a tuple of username, password
            login_inputs = view.login_inputs()
            account = model.Account(username=login_inputs[0], password=login_inputs[1])
            if account:
                return account
            view.bad_credentials()
        else:
            break

def trader_menu(account):
    """menu for options available post-login"""
    while True:
        print()
        view.trader_menu()
        try:
            trader_input = int(view.menu_input())
        except ValueError:
            view.bad_input()
            continue
        if trader_input not in range(1,9):
            view.bad_input()
        # check balance
        elif trader_input == 1:
            view.account_balance(account.balance)
        # deposit money
        elif trader_input == 2:
            try:
                deposit_amount = float(view.deposit_input())
            except ValueError:
                view.bad_input()
                continue
            account.balance += deposit_amount
            account.save()
        # check positions
        elif trader_input == 3:
            view.print_positions(account.get_positions())
        # lookup price
        elif trader_input == 4:
            try:
                ticker_symbol = view.ticker_input()
                stock_price = model.lookup_price(ticker_symbol)
                view.print_lookup_price(stock_price)
            except ValueError:
                view.bad_stock_input()
        # buy order
        elif trader_input == 5:
            buy_ticker_symbol = view.ticker_input()
            try:
                buy_quantity = int(view.buy_amount())
            except:
                view.bad_input()
                continue
            try:
                account.buy(buy_ticker_symbol, buy_quantity)
            except ValueError:
                view.bad_buy()
        # sell order
        elif trader_input == 6:
            sell_ticker_symbol = view.ticker_input()
            try:
                sell_quantity = int(view.sell_amount())
            except:
                view.bad_input()
                continue
            try:
                account.sell(sell_ticker_symbol, sell_quantity)
            except ValueError:
                view.bad_sell()
        # order history
        elif trader_input == 7:
            view.trade_history(account.get_trades())
        # log out
        elif trader_input == 8:
            break

if __name__ == "__main__":
    while True:
        results = main_menu()
        if not results:
            break
        trader_menu(results)