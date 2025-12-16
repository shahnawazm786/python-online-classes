player=['MS Dhoni','Rahul','Yuvraj','Pathan']
#MS Dhoni
print(player)
player.remove('MS Dhoni')
print(player)
#player.remove('MS Dhoni') # ValueError 
#print(player)
player.insert(0,'Sachin')
print(player)
player.insert(4,'Nadeem')
print(player)
player.insert(3,'Sachin')
print(player)
player.append('Sachin')
print(player)
print('Remove "Sachin" from the list')
player.remove('Sachin') # first occurance
print(player) 

