"""
Author: Mai Duc Nhat Minh
Date: 29/10/2021
Problem:   Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200
Solution:

    ....
"""
for num in range(30,200):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        print(num)