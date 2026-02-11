class Father:
    def __init__(self):
        pass
    
    def get_fathe_info(self):
        print('Father class')

class Mother:
    def __init__(self):
        pass
    
    def get_mother_info(self):
        print('Mother class')


class Children(Father,Mother):

    def __init__(self):
        super().__init__()

    def get_child_info(self):
        print('Child information')

    

c=Children()
c.get_fathe_info()
c.get_mother_info()
c.get_child_info()
