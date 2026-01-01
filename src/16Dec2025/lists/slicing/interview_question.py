# Write a program to enter any string and check given string is palindrome or not
st=input('Enter any string')
if (st==st[::-1]):
    print(f'{st} is palindrome')
else:
    print(f'{st} is not palindrome')