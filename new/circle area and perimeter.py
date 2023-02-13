class circle:
     def __init__(self,radius):
         self.radius=radius

     def area_circle(self):
         area=3.14*self.radius*self.radius
         return area

     def perimeter_circle(self):
         perimeter=2*3.14*self.radius   
         return perimeter

c1=circle(4)
print("area of circle:",c1.area_circle()) 
print("perimeter of circle:",c1.perimeter_circle())        
