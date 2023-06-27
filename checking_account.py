class CheckingAccount:
    account_num = 0
    account_holder = ""
    account_balance = 0

    def deposit(account_num, deposit_amount, account_balance=None):
        account_balance += deposit_amount

    def withdrawal(account_num, withdrawal_amount):
        account_balance -= withdrawal_amount

    def balance_inquiry(account_num):
        print("Your current balance is " + str(account_balance))

