class SavingsAccount(Account):

    account_balance = 0
    interest_rate = 0


    def deposit(account_num, deposit_amount, account_balance=None):
        account_balance += deposit_amount

    def withdrawal(account_num, withdrawal_amount):
        account_balance -= withdrawal_amount


    def balance_inquiry(account_num):
        print("Your current balance is " + str(account_balance))


