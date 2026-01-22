st="Python is scripting language."
st1="Python is high level language"
flag=st.startswith("Python") # return True | False
print(flag)
flag=st.startswith("P") # return True | False
print(flag)
flag=st.startswith("thon") # return True | False
print(flag)

print('==== endswith() ====')
ends_with_flag=st.endswith('.') # return True | False
print(ends_with_flag) # True
ends_with_flag=st1.endswith('.') # return True | False
print(ends_with_flag) # False
