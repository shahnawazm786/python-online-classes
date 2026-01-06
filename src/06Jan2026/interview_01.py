sentence="Python is a programming language Python is high level language Python used in data science and data analytics and machine learning and django"

# split sentence into word
words=sentence.split(' ')
print(words)
word_count={} # empty 
for word in words:
    #print(word)
    word_count[word]=word_count.get(word,0)+1
    
print(word_count)
print('Showing only duplicate word')
for K,val in word_count.items():
    if val>1:
        print(f'{K} repeated {val} times')

#unique word
print('🌟 🌟 Unique word 🌟 🌟')
for K,val in word_count.items():
    if val==1:
        print(f'{K} repeated {val} times')

