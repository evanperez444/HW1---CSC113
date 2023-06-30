from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount
class Bank:

    def __init__(self, name, acc1_obj, acc2_obj):
        self.name = name
        self.acc1_obj = acc1_obj
        self.acc2_obj = acc2_obj




savings_acc1 = SavingsAccount(1234,"James", "112 Aurora Lane", 20, 0.1)
checking_acc1 = CheckingAccount(1234,"James", "112 Aurora Lane", 60)

x = Bank("Arvest", savings_acc1, checking_acc1)

checking_acc1.display()

checking_acc1.deposit(60)

checking_acc1.balance_inquiry()

checking_acc1.withdrawal(40)

checking_acc1.balance_inquiry()



savings_acc1.display()

savings_acc1.project_annual_interest(10)



