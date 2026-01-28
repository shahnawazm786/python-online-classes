class Circle:
    
    def __init__(self,radius): # This method belongs to Cirle 
        self.radius=radius # radius local variable while self.radius Object attributes
    
    def calculate_area(self): #piersqaure
        return 3.141 * (self.radius ** 2 ) # power raised **2 (square)


circle1=Circle(5) # circle1 is one object
print("Show the radius of circle1 ",circle1.radius)
print(circle1.calculate_area())

print(id(circle1.radius))
#print(id(circle1.calculate_area()))

circle1.color="Red"
print(f'Color of circle is {circle1.color}')
#print(circle1.calculate_area())
circle1.radius=20
print(circle1.calculate_area())

circle2=Circle(10) # circle2 is another object
print(circle2.calculate_area()) 
print(id(circle2.radius))
#print(id(circle2.calculate_area()))
print(f'Color of circle is {circle2.color}')
circle2.radius=50
print(circle2.calculate_area()) 

print(circle1==circle2)
print(id(circle1))
print(id(circle2))
