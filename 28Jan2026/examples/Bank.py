class Account:
    accounttype="" # class attribute 
    
    def __init__(self,account_name,amount):
        self.account_name=account_name
        self.amount=amount
    
    def credit(self,amount):
        if self.amount>=amount:
            self.amount-=amount
        else:
            print('Insufficient balance')  
    
    def debit(self,amount):
        self.amount+=amount
    
    def display(self):
        print(f'Account name {self.account_name} and balance amount is {self.amount}')
    
    def get_balance(self):
        return self.amount
    
    def __str__(self): # method overload 
        return f'🚨 Account name {self.account_name} and balance amount is {self.amount}'



a1=Account("10001",5000.00)
#a1.display()
print(a1)
a1.credit(1000)
print(a1)

#a1.display()
a1.debit(15000)
print(a1)

#a1.display()
print(a1.get_balance())
a1.credit(20000)
print(a1)



