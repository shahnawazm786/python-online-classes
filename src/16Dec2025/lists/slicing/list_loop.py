names=['Rahman','Yasin','Mojamil','Taha','Makki','Arabi','Madani']
reverse_name=[]
for name in names:
    if len(name)>5:
        rev_name=reversed(name)
        reverse_name.append(rev_name)
    else:
        print(name)
