"""
Author: Mai Duc Nhat Minh
Date: 04/09/2021
Problem:  Write a program that takes as input a number of kilometers and prints the corresponding number of nautical
miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North
Pole and the equator.
• A nautical mile is 1 minute of an arc.
Solution:
    ....
"""
Kilometers = int(input("Enter the amount of kilometers: "))
degrees = 90 * 60
onekilo = degrees/10.000
print("nautical mile: ", onekilo * Kilometers)