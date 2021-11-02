"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:  Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing inputs.
After the user presses the enter key, the program should print the sum of the
numbers and their average
Solution:

    ....
"""
numbers = []
print("enter key to stop")
while(True):
    num = input("enter a number :")
    if num:
        numbers.append(int(num))
    elif(num == ''):
            break
sum_num =0
for num in numbers:
    sum_num += num
avg = sum_num / len(numbers)
print(sum_num)
print(avg)