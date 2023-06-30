class Account:

    def __init__(self, account_num, account_holder, holder_address, account_balance):
        self.account_num = account_num
        self.account_holder = account_holder
        self.holder_address = holder_address
        self.account_balance = account_balance

    def deposit(self,deposit_amount):
        self.account_balance += deposit_amount
        print("You deposited " + "$" + str(deposit_amount)+ "\n")

    def withdrawal(self,withdrawal_amount):
        self.account_balance -= withdrawal_amount
        print("$" + str(withdrawal_amount) + " has been withdrawn from your account" + "\n")

    def balance_inquiry(self):
        print("Your current balance is " + str(self.account_balance)+ "\n")

    def display(self):
        print("---------------------------------------------------------")
        print("Account Number: " + str(self.account_num))
        print("Acount Holder: " + str(self.account_holder))
        print("Holder Address: " + str(self.holder_address))
        print("Account Balance: " + str(self.account_balance) + "\n")
        print("---------------------------------------------------------")
