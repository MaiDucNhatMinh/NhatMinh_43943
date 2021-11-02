"""
Author: Mai Duc Nhat Minh
Date: 04/09/2021
Problem:  The kinetic energy of a moving object is given by the formula KE = (1 / 2) mv^2
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
Solution:
    ....
"""
mass = float(input("Enter mass in kgs: "))
velocity = float(input("Enter velocity in m/s: "))
motivation = 1/2 * mass * velocity * velocity
print("motivation: ", motivation)