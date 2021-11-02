"""
Author: Mai Duc Nhat Minh
Date: 14/09/2021
Problem:  Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.
Solution:

    ....
"""
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
    print("Equilateral triangle")
else:
    print("Not Equilateral triangle")