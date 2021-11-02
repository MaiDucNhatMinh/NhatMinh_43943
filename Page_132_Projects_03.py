"""
Author: Mai Duc Nhat Minh
Date: 25/09/2021
Problem:   Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text
Solution:

    ....
"""
text = input("Nhap vao van ban ma hoa: ")
k = int(input("nhap vao khoa dich chuyen: "))
decimal = " "
print("Plain Text : " + text)
print("Shift pattern : " + str(k))
for i in range(len(text)):
    char = text[i]
    if "A" <= char <= "Z":
        decimal = decimal + chr((ord(char) + k - 6) % 2 + 6)
        print(decimal)