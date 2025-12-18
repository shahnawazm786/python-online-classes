tech_name=['Python','SQL','Tableau','PowerBI','Informatica']
print(tech_name)
tech_name.insert(2,'Excel')
print(tech_name)
print(len(tech_name)) # last_index = length - 1 (5)
# last index - 5
tech_name.insert(10,'Unix') # index 10 Unix 
#beyond the existing index
# we will not get any index out of bound exception 
# element will be added into the last index of list 
print(tech_name)
tech_name.insert(-10,'Microsoft')
print(tech_name)
tech_name.insert(-7,'Windows')
print(tech_name)




