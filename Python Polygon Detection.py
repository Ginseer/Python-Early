# -*- coding: utf-8 -*-
"""
UTC ID: TYV379
Name: joseph Edwards
Date: 06/20/2021
"""

from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, lengths_of_sides):
        self.number_of_sides = len(lengths_of_sides)
        self.lengths_of_sides = [0] * self.number_of_sides
        self.assign_values_to_sides(lengths_of_sides)
        
    def print_num_sides(self):
        print('Number of sides ' + str(self.number_of_sides))
        
    def assign_values_to_sides(self,lengths_of_sides):
        index = 0
        while index < len(lengths_of_sides):
            self.lengths_of_sides[index] = lengths_of_sides[index]
            index += 1
    
    #These are just to give a simple pass of the,
    #perimeter and the area
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Triangle(Polygon):
    
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 3 , self.number_of_sides
        
    def area(self):
        a, b, c = self.lengths_of_sides
        s = (a+b+c) / 2
        return(s*(s-a)*(s-b)*(s-c))**0.5
        #This calculates the area for the triangle
    
    def perimeter(self):
        s = (self.lengths_of_sides[0] + self.lengths_of_sides[1] + self.lengths_of_sides[2])
        return s

class Quadrilateral(Polygon):
    
    def __init__(self, lengths_of_sides):
        super().__init__([lengths_of_sides[0], lengths_of_sides[1], lengths_of_sides[0], lengths_of_sides[1]])
        assert 4, self.number_of_sides
        
    def area(self):
        x,y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return (x+y) * 2
    
    def perimeter(self):
        w = (self.lengths_of_sides[0] + self.lengths_of_sides[1]) * 2
        return w
    
class Pentagon(Polygon):
    
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 5, self.number_of_sides
        
    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y
    
    def perimeter(self):
        x,y  = self.lengths_of_sides
        return (x+y)/2
class Hexagon(Polygon):
    
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 6, self.number_of_sides
    
    def area(self):
        x,y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x*y
    
    def perimeter(self):
        x,y = self.lengths_of_sides
        return (x+y)*2

class IsoscelesTriangle(Triangle):
    
    def __init__(self,side,base):
        super().__init__([side,side,base])
        
class Rectangle(Quadrilateral):
    
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        
    def area(self):
        x,y = self.lengths_of_sides[0],self.lengths_of_sides[1]
        return x*y
    
    def perimeter(self):
        a = (self.lengths_of_sides[1] + self.lengths_of_sides[0]) * 2
        return a
    
class Square(Rectangle):
    
    def __init__(self,side):
        super().__init__([side, side])
    
    def area(self):
        x = self.lengths_of_sides[0]
        return x * x
    
    def perimeter(self):
        x = self.lengths_of_sides[0]
        return x * 4

