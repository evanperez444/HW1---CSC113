from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount

#The Bank class allows the user to creat a bank object that contains:
#-The name of the bank
#-A checking account
#-A savings account
#*the checking and savings account must be premade since the bank constructor takes 3 arguments: bank name, savings account, checking_account
class Bank:

    def __init__(self, name, acc1_obj, acc2_obj):
        self.name = name
        self.acc1_obj = acc1_obj
        self.acc2_obj = acc2_obj



#create two account objects, savings and checking accounts
savings_acc1 = SavingsAccount(1234,"James", "112 Aurora Lane", 20, 0.1)
checking_acc1 = CheckingAccount(1234,"James", "112 Aurora Lane", 60)

#create a bank object with the two accounts
x = Bank("Arvest Bank", savings_acc1, checking_acc1)
print(x.name + "\n")

#Edit checking account

checking_acc1.display()

checking_acc1.deposit(60)

checking_acc1.balance_inquiry()

checking_acc1.withdrawal(120)

checking_acc1.withdrawal(60) #test withdrawal edge case

checking_acc1.balance_inquiry()


#Edit Savings Account

savings_acc1.display()

savings_acc1.deposit(60)

savings_acc1.balance_inquiry()

savings_acc1.project_annual_interest(10)

savings_acc1.withdrawal(120) #test withdrawal edge case

savings_acc1.withdrawal(60)

savings_acc1.withdrawal(20)

savings_acc1.balance_inquiry()





