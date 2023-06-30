from account import Account

#since a Savings Account is an Account, we can carry over Account methods/attributes over using .super()
#we can also add a new paramater specific for this child class: interest rate
class SavingsAccount(Account):
    def __init__(self, account_num, account_holder, holder_address, account_balance, interest_rate):
        super().__init__(account_num, account_holder, holder_address, account_balance)
        self.interest_rate = interest_rate

    #calculates and displays projected annual interest given the amount of years
    def project_annual_interest(self, years):

        growth = self.account_balance
        for n in range(years):
            growth += (growth * self.interest_rate)

        print("In " + str(years) + " years, your account balance will be: " + str(growth) + "\n")

    #displays account balance and interest rate
    def balance_inquiry(self):
        print("Your current balance is " + str(self.account_balance) + " and your interest rate is: " + str(self.interest_rate) + "\n" )

    #changes interest rate
    def change_interest_rate(self, rate):
        self.interest_rate = rate