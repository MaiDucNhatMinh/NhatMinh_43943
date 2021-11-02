"""
Author: Mai Duc Nhat Minh
Date: 16/09/2021
Problem:  Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem
that in a right triangle, the square of one side equals the sum of the squares of the other two sides.
Solution:

    ....
"""
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if (z**2) == (x**2) + (y**2) or (y**2) == (x**2) + (z**2) or (x**2) == (y**2) + (z**2):
    print("Right triangle")
else:
    print("Not right triangle")