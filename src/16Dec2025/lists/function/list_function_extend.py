player=['MS Dhoni','Rahul','Yuvraj','Pathan']
print('🚀 Old Player')
print(player)
new_player=['Gill','Sarfraj','Nadeem','Yashswi']

print('🚀 New Player')
print(new_player)

t20=['Messi','Ronaldo']
print('🚀 T20 team')
print(t20)
t20.extend(player)
print('🚀 Extended T20 team')
print(t20)

t20.extend(new_player)
print('🚀 Extended T20 team')
print(t20)

#append() or insert() -> at a time only one element add into the list
# multiple element -> extend()



