str='''The story of the Python programming language begins in the late 1980s as a hobby project by Dutch programmer Guido van Rossum. His goal was to create an easy-to-read, intuitive scripting language that could serve as a successor to the ABC language and bridge the gap between C programming and shell scripts.'''
words= str.split(' ')
print(words)
word_dict={}
for word in words:
    print(word)
    if word is word_dict.keys:
        word_dict[word]=word_dict.get(word,0)+1
    else:
        word_dict[word]=1
    
print(word_dict)