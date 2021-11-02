"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:    The German mathematician Gottfried Leibniz developed the following method
to approximate the value of π:
π/4 =1 - 1/3 + 1/5 - 1/7 + . . .
Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.
Solution:

    ....
"""
iteration = int(input("n: "))
presumm = 0
div = 1
sign = True
for i in range(iteration):
    presumm = presumm + 1 / div if sign else presumm - 1 / div
    div += 2
    sign = not sign
pi = presumm * 4
print(pi)
