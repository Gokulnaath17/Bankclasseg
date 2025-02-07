class BalanceException(Exception):
    pass

class Bankaccount:
    def __init__(self,amount,name):
        self.balance=amount
        self.accname=name
        print(f'\nAccount created for {self.accname} \nCurrent balance is {self.balance:.2f}')
    
    def get_balance(self):
        print(f'\nAccount name {self.accname}\nBalance {self.balance:.2f}')
    
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
    def transfer(self,amount,receiver):
        try:
            print('\n****************')
            self.viable_transaction(amount)
            self.withdraw(amount)
            receiver.deposit(amount)
            print('\n Transfer complete')
        except BalanceException as error:
            print('\nTransaction failed')
            print(error)
class Interest(Bankaccount):
    def deposit(self, val):
        self.balance+=(val+val*0.05)
        self.get_balance()
class Savings(Interest):
    def __init__(self, amount, name):
        super().__init__(amount, name)
        self.fee=5
    def withdraw(self, amount):
        self.total_withdraw=amount+self.fee
        try:
            self.viable_transaction(self.total_withdraw)
            self.balance-=(self.total_withdraw)
            print('Transcation complete')
            self.get_balance()
        except BalanceException as error:
            print('Transaction failed')
            print(error)

    def transfer(self, amount, receiver):
            total_transfer = amount + self.fee 
            try:
                print('\n****************')
                self.viable_transaction(total_transfer)  
                self.withdraw(amount) 
                receiver.deposit(amount) 
                print('\nTransfer complete')
            except BalanceException as error:
                print('\nTransaction failed')
                print(error)
            
