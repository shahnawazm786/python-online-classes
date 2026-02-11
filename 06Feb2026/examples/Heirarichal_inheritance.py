class Car:

    def __init__(self,engineno):
        self.engine_no=engineno
    
    def get_info(self):
        print('Engine no',self.engine_no)
    
class Maruti(Car):
    def __init__(self, engineno,milage):
        super().__init__(engineno)
        self.milage=milage
    
    def get_info(self):
        super().get_info()
        print('Milage',self.milage)


class Toyata(Car):

    def __init__(self, engineno,speed):
        super().__init__(engineno)
        self.speed=speed
    
    def get_info(self):
        super().get_info()
        print('Speed',self.speed)
    
m=Maruti('ADCF45678',22)
m.get_info()

t=Toyata('1234567',180)
t.get_info()




