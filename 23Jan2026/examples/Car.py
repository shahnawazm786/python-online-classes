class CAR:

    def __init__(self): #donder constructor
        self.Engine_no=10001
        self.Model_no=2026
        self.Car_name='Maruti 800'
    
    def start(self):
        print('Car is strated')
    
    def stop(self):
        print('Car is stoped')
         

c=CAR() # c is an object CAR class #default constructor
print(c) # object reference 
# name_of_object.properties/method of the class
print(f'Car name -> {c.Car_name}') # . dot notation  is the way of accessing the properties and method of the class by the help of object
print(f'Model no -> {c.Model_no}')
print(f'Engine no -> {c.Engine_no}')

# Function access
c.start()
c.stop()




