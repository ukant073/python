import math
class Triangle:

    def __init__(self, side1,side2,side3):

      self.side1=side1
      self.side2=side2
      self.side3=side3
    if(side1 and side2 and side3<0):
       print("triangle is not defined:")

    else:
     
      def Perimeter(self,side1,side2,side3):
        self.Perimeter=side1+side2+side3

      def Area(self,side1,side2,side3):
        s=(side1+side2+side3)/2
        a=(s*(s-side1)*(s-side2)*(s-side3))
        self.Area=math.sqrt(a)

t1 = Triangle(3,4,5)
t2 = Triangle(6,7,8)
     
 
