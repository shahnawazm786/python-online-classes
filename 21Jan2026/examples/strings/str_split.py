st="Python,is,language,Python,is,high,level,language,python,is,used,in,machine,learning"
words=st.split(',') # lreturn list of the element (separate word from given sentence)
print(len(words))
# find out occurance of the given word from the sentence
print(st.find('Python',2)) #index return
cnt=0
print(words)

for x in words:
    if x.upper()=='Python'.upper(): # given and input both - upper case (case - insensitive)
        cnt+=1

print(f'\'Python\' occured -> {cnt}')


# Question - find out the duplicate word from the sentence - interview


