"""
Author: Mai Duc Nhat Minh
Date: 29/08/2021
Problem:   Enter an input statement using the input function at the shell prompt. When the
prompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened.
Solution:
    Lỗi tại dòng num = num + 1 vì không thể chuyển đổi hoàn toàn đối tượng int thành str
    ....
"""
num = input('Số:')
num = num + 1
print(num)