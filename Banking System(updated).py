from datetime import datetime

accounts = {}
transaction_history = []

MIN_BALANCE = 500
PENALTY_FEE = 50
INTEREST_RATE = 0.05


def line():
    print("╔" + "═" * 54 + "╗")


def footer():
    print("╚" + "═" * 54 + "╝")


def title(text):
    line()
    print(f"║{text.center(54)}║")
    footer()


def divider():
    print("─" * 56)


def register():
    title("CREATE ACCOUNT")

    username = input("Username       : ")

    if username in accounts:
        print("\nUsername already exists.")
        return

    password = input("Password       : ")
    account_type = input("Account Type (Savings/Checking): ").lower()

    if account_type not in ["savings", "checking"]:
        print("\nInvalid account type.")
        return

    accounts[username] = {
        "password": password,
        "type": account_type,
        "balance": 0
    }

    print("\nAccount created successfully.")


def login():
    title("LOGIN ACCOUNT")

    username = input("Username       : ")
    password = input("Password       : ")

    if username in accounts:

        if accounts[username]["password"] == password:
            print("\nLogin successful.")
            banking_menu(username)

        else:
            print("\nIncorrect password.")

    else:
        print("\nAccount not found.")


def deposit(username):
    title("DEPOSIT MONEY")

    try:
        amount = float(input("Deposit Amount : ₱"))

        if amount <= 0:
            print("\nInvalid amount.")
            return

        accounts[username]["balance"] += amount

        transaction_history.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{username} deposited ₱{amount:.2f}"
        )

        print("\nDeposit successful.")
        print(f"Updated Balance: ₱{accounts[username]['balance']:.2f}")

    except ValueError:
        print("\nInvalid input.")


def withdraw(username):
    title("WITHDRAW MONEY")

    try:
        amount = float(input("Withdraw Amount: ₱"))

        if amount <= 0:
            print("\nInvalid amount.")
            return

        if amount > accounts[username]["balance"]:
            print("\nInsufficient balance.")
            return

        accounts[username]["balance"] -= amount

        if accounts[username]["balance"] < MIN_BALANCE:
            accounts[username]["balance"] -= PENALTY_FEE

            print("\nMinimum balance not maintained.")
            print(f"Penalty Fee Applied: ₱{PENALTY_FEE:.2f}")

        transaction_history.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{username} withdrew ₱{amount:.2f}"
        )

        print("\nWithdrawal successful.")
        print(f"Remaining Balance: ₱{accounts[username]['balance']:.2f}")

    except ValueError:
        print("\nInvalid input.")


def transfer_money(username):
    title("TRANSFER MONEY")

    receiver = input("Receiver Username : ")

    if receiver not in accounts:
        print("\nReceiver account not found.")
        return

    if receiver == username:
        print("\nYou cannot transfer to your own account.")
        return

    try:
        amount = float(input("Transfer Amount  : ₱"))

        if amount <= 0:
            print("\nInvalid amount.")
            return

        if amount > accounts[username]["balance"]:
            print("\nInsufficient balance.")
            return

        accounts[username]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        transaction_history.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{username} transferred ₱{amount:.2f} to {receiver}"
        )

        print("\nTransfer successful.")
        print(f"Remaining Balance: ₱{accounts[username]['balance']:.2f}")

    except ValueError:
        print("\nInvalid input.")


def calculate_interest(username):
    title("FUTURE INTEREST CALCULATION")

    if accounts[username]["type"] != "savings":
        print("\nInterest only applies to Savings Account.")
        return

    try:
        years = int(input("Number of Years: "))

        if years <= 0:
            print("\nInvalid number of years.")
            return

        balance = accounts[username]["balance"]

        future_interest = balance * INTEREST_RATE * years
        future_total = balance + future_interest

        divider()

        print(f"Current Balance : ₱{balance:.2f}")
        print(f"Interest Rate   : 5% per year")
        print(f"Years           : {years}")
        print(f"Future Interest : ₱{future_interest:.2f}")
        print(f"Estimated Total : ₱{future_total:.2f}")

        divider()

        transaction_history.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{username} calculated future interest"
        )

    except ValueError:
        print("\nInvalid input.")


def show_balance(username):
    title("ACCOUNT DETAILS")

    print(f"Username      : {username}")
    print(f"Account Type  : {accounts[username]['type'].title()}")
    print(f"Balance       : ₱{accounts[username]['balance']:.2f}")


def show_transaction_history():
    title("TRANSACTION HISTORY")

    if len(transaction_history) == 0:
        print("No transactions available.")

    else:
        for transaction in transaction_history:
            print(transaction)


def banking_menu(username):

    while True:

        title(f"WELCOME, {username.upper()}")

        print("[1] Deposit Money")
        print("[2] Withdraw Money")
        print("[3] Transfer Money")
        print("[4] Future Interest Calculation")
        print("[5] Show Balance")
        print("[6] Transaction History")
        print("[7] Logout")

        divider()

        choice = input("Choose Option : ")

        if choice == "1":
            deposit(username)

        elif choice == "2":
            withdraw(username)

        elif choice == "3":
            transfer_money(username)

        elif choice == "4":
            calculate_interest(username)

        elif choice == "5":
            show_balance(username)

        elif choice == "6":
            show_transaction_history()

        elif choice == "7":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice.")


while True:

    title("BANKING SYSTEM")

    print("[1] Register")
    print("[2] Login")
    print("[3] Exit")

    divider()

    choice = input("Choose Option : ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        title("THANK YOU FOR USING THE SYSTEM")
        break

    else:
        print("\nInvalid choice.")