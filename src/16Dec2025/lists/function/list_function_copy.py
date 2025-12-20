player=['MS Dhoni','Rahul','Yuvraj','Pathan']
print('🚀 Player list')
print(player)
# clone 
print('🚀 Cloning .. ')
player1=player 
print('🚀 Alfter coloned')
print(player1)

# append new member
player.append('Saurabh Gangooli')
print('🚀 Player list')
print(player)
print('🚀 There is no colone')
print(player1) # automatically player1 will have the appned member also

# if you want no change into the copied list then use copy()

player2=player.copy()
print('🚀 Player2 list')
print(player2)
player.append('Yusuf Pathan')


print('🚀 After appened Yusuf Pathan player list is')
print(player)

print('🚀 Player2 list is not impacted')
print(player2)