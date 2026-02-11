class Car:

    def __init__(self,engineno):
        self.engine_no=engineno
    
    def get_info(self):
        print('Engine no',self.engine_no)

class SUV:

    def __init__(self,milage):
        self.milage=milage
    
    def get_info(self):
        print('Milage is',self.milage)


class ERTIGA(Car,SUV):

    def __init__(self, engineno,milage,no_of_seat):
        Car.__init__(self,engineno)
        SUV.__init__(self,milage)
        self.no_of_seat=no_of_seat

    
    def get_info(self):
        Car.get_info(self)
        SUV.get_info(self)
        print('No of seat',self.no_of_seat)

e=ERTIGA(1234,20,7)
e.get_info()
        