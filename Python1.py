# Code for area of circle
import math

r=float(input("Enter the radius of the circle:- "))
area= math.pi*r*r
print("area of circle is ", area)


# Code to find Extension of a file
filename= input("INput the filename:- ")
f=filename.split(".")
print("the extension is "+repr(f[-1]))
