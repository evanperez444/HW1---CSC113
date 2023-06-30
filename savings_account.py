from account import Account
class SavingsAccount(Account):
    def __init__(self, account_num, account_holder, holder_address, account_balance, interest_rate):
        super().__init__(account_num, account_holder, holder_address, account_balance)
        self.interest_rate = interest_rate

    def project_annual_interest(self, years):

        growth = self.account_balance
        for n in range(years):
            growth += (growth * self.interest_rate)

        print("In " + str(years) + " years, your account balance will be: " + str(growth))