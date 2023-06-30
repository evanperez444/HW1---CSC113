class Account:
    #contructor for account class, takes in paramters:
    #-The account number
    #-The account holder's name
    #-The account holder's address
    #-The account balance
    def __init__(self, account_num, account_holder, holder_address, account_balance):
        self.account_num = account_num
        self.account_holder = account_holder
        self.holder_address = holder_address
        self.account_balance = account_balance

    #depoist method takes the deposit amount and adds it to the account balance
    def deposit(self,deposit_amount):
        self.account_balance += deposit_amount
        print("You deposited " + "$" + str(deposit_amount)+ "\n")

    #withdrawal method takes the withdrawal amount and subtracts it from the account balance
    #will not withdrawal if:
    #1.Account balance is 0 or less
    #2.Withdrawal amount makes the account balance less than zero
    def withdrawal(self,withdrawal_amount):
        if self.account_balance > 0 and self.account_balance - withdrawal_amount >= 0:
            self.account_balance -= withdrawal_amount
            print("$" + str(withdrawal_amount) + " has been withdrawn from your account" + "\n")
        else:
            print("Withdrawl Failed: Insuffucient Funds\n")

    #displays the current account balance
    def balance_inquiry(self):
        print("Your current balance is " + str(self.account_balance)+ "\n")

    #displays all account information
    def display(self):
        print("---------------------------------------------------------")
        print("Account Number: " + str(self.account_num))
        print("Acount Holder: " + str(self.account_holder))
        print("Holder Address: " + str(self.holder_address))
        print("Account Balance: " + str(self.account_balance) + "\n")
        print("---------------------------------------------------------")
