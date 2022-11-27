class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
              
    def deposit(self, blncAdd):
        self.balance += blncAdd
        
    def withdraw(self, blnsWth):
        if self.balance >= blnsWth:
            self.balance -= blnsWth
            print('Accepted')
        else:
            print('Declined')