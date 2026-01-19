# default parameter
def calc(num1,num2=5):
    result = num1 + num2
    print(f'Sum is \t {result}')

calc(1000,2000) # num2 is overwritten by 2000 
calc(900) # 905

print(calc(100,200))