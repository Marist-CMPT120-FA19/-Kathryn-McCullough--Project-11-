#name: Kathryn McCullough
#email: kathryn.mccullough1@marist.edu
#description: Write a class to represent spheres. The class should implement
#specific methods

import math

class Sphere:
    def __init__(self, radius):
        self.radius=radius
        self.area=0
        self.volume=0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        self.area= 4 * math.pi * (self.radius**2)
        return (self.area)

    def getVolume(self):
        self.volume= (4/3) * math.pi * (self.radius**3)
        return (self.volume)

def main():
    print("This program will compute the surface area and the volume of a given\nradius of a sphere.\n")
    radius=eval(input("Enter a radius: "))
    r=radius
    rad=Sphere(r)


    #need to add () b/c calling functions from a Class?
    #Note: make sure names aren't getting confused
    #was using "rad.volume" down there and had to change above and below to
    #"getVolume" because of programming confusion> worked after
    print("\nSurface Area: ", rad.surfaceArea())
    print("\nVolume: ", rad.getVolume())

main()
            
