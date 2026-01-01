City={'Kolkatta','Delhi','Mumbai','Chennai','Hyderabad'}
print(City)
City.discard('Patna') # will not throw any error if item not present
#City.remove('Patna') # will throw an error when item not present
City.discard('Delhi')
print(City)
City.remove('Hyderabad')
print(City)



