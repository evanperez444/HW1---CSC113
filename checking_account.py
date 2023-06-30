from account import Account
class CheckingAccount(Account):
    def __init__(self, account_num, account_holder, holder_address, account_balance):
        super().__init__(account_num, account_holder, holder_address, account_balance)
