class Bus:

    def __init__(self,Bus_name):# constructor value (parameterise constructor)
        self.Bus_name=Bus_name
    def start(self):
        print('Bus is strated')
    
    def stop(self):
        print('Bus is stoped')

b=Bus('Volvo')
print(b.Bus_name) # variable created but no value is assigned

b1=Bus('TATA')
print(b1.Bus_name) # variable created but no value is assigned

b2=Bus('TOYOTA')
print(b2.Bus_name) # variable created but no value is assigned


    