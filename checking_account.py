from account import Account
#since a Checkings Account is an Account, we can carry over Account methods/attributes over using .super()
#there isn't anything we really need to add for a checking account
class CheckingAccount(Account):
    def __init__(self, account_num, account_holder, holder_address, account_balance):
        super().__init__(account_num, account_holder, holder_address, account_balance)
