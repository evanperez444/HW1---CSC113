class SavingsAccount(Account):

    def __init__(self, account_balance, interest_rate):
        self.account_balance = account_balance
        self.interest_rate = interest_rate

    def deposit(self,deposit_amount):
        self.account_balance += deposit_amount

    def withdrawal(self,withdrawal_amount):
        self.account_balance -= withdrawal_amount
        print(str(withdrawal_amount) + "has been withdrawn from your account")

    def balance_inquiry(self):
        print("Your current balance is " + str(self.account_balance))


