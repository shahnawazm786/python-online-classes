class Car:

    def __init__(self,engineno):
        self.engine_no=engineno
    
    def get_info(self):
        print('Engine no',self.engine_no)

class Maruti800(Car):

    def __init__(self, engineno,name,model,speed,milage):
        super().__init__(engineno)
        self.name=name
        self.model=model
        self.speed=speed
        self.milage=milage

    def get_info(self):
        super().get_info()
        print('Name',self.name)
        print('Model',self.model)
        print('Speed',self.speed)
        print('Milage',self.milage)
    
class ERTIGA(Maruti800):
    #type CNG| Petrol|Diesel
    def __init__(self, engineno, name, model, speed, milage,types):
        super().__init__(engineno, name, model, speed, milage)
        self.types=types
    def get_info(self):
        super().get_info()
        print('Types',self.types)

mart=Maruti800('MAR3456789','OMNI',2000,80,24)
mart.get_info()
print()
print()
ert=ERTIGA('MAR3456789','ERTIGA SUV',2026,140,18,'CNG')
ert.get_info()

