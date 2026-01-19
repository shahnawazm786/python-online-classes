def calculator(symbol,num1,num2):
    if symbol=='+':
        result= num1 + num2
        return symbol,result
    elif symbol=='-':
        result= num1 - num2
        return symbol,result
    elif symbol=='*':
        result= num1 * num2
        return symbol,result
    elif symbol=='/':
        result= num1 / num2
        return symbol,result
    elif symbol=='%':
        result= num1 % num2
        return symbol,result
    else:
        return None

# function call
print(calculator('^',100,200)) 
sym,res=calculator('+',5000,10000)
print(f'{sym} is Calculation performed and result is  {res}')

print(calculator('^',100,200,400)) 

