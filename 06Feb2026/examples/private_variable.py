class Account:
    def __init__(self,balance,account_type,branch):
        self.__balance=balance
        self.account_type=account_type
        self._branch=branch

a=Account(5000,'Saving Account','New Delhi')
print(a.account_type)
#print(a.__balance)
print(a._branch)




