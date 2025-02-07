class BalanceException(Exception):
    pass

class Bankaccount:
    def __init__(self,amount,name):
        self.balance=amount
        self.accname=name
        print(f'\nAccount created for {self.accname} \nCurrent balance is {self.balance}')
    
    def get_balance(self):
        print(f'\nAccount name {self.accname}\nBalance {self.balance}')
    
    def deposit(self,val):
        self.balance+=val
        print(f'\nDeposit succesfull')
        self.get_balance()
    
    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f'\nInsufficient funds \navailable balance {self.balance}')
    def withdraw(self,withdraw):
        try:
            self.viable_transaction(withdraw)
            self.balance-=withdraw
            print('\nTransaction succesfully completed')
            self.get_balance()
        except BalanceException as error:
            print('\nTransaction failed')
            print(error)

           
