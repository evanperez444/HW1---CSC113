class CheckingAccount(Account):

    account_balance = 0

    def deposit(account_num, deposit_amount, account_balance):
        account_balance += deposit_amount

    def withdrawal(account_num, withdrawal_amount, account_balance):
        account_balance -= withdrawal_amount
        print(str(withdrawal_amount) + "has been withdrawn from your account")

    def balance_inquiry(account_num, account_balance):
        print("Your current balance is " + str(account_balance))

