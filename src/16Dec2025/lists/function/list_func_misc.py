player=['MS Dhoni','Rahul','Yuvraj','Pathan']
print(len(player)) # total no of element
#count() - occurance of element
player.append('MS Dhoni')
print(len(player))
print(player)
print(player.count('MS Dhoni'))
print('"Azhar" is not in a list')
print(player.count('Azhar'))
#sum
#indian player
run=[12000,15000,11000,10000]
print(f'Total run => {sum(run)}')
print(f'Highest run => {max(run)}')
print(f'Lowest run => {min(run)}')
print(list(reversed(run)))
print(list(sorted(run)))
