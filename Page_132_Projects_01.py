"""
Author: Mai Duc Nhat Minh
Date: 25/09/2021
Problem:     Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
Solution:

    ....
"""
message = input("Nhap van ban: ")
distanceValue = int(input("Nhap khoang cach: "))
result = " "
for x in message:
    result += chr(ord(x) + distanceValue)
print(" " + result)