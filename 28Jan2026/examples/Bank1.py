class Account:
    accounttype="" # class attribute 
    
    def __int__(self,account_name,amount):
        self.account_name=account_name
        self.amount=amount
    
    def credit(self,amount):
        self.amount-=amount
    
    def debit(self,amount):
        self.amount+=amount
    
    def display(self):
        print(f'Account name {self.account_name} and balance amount is {self.amount}')
    