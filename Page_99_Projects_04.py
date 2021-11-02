"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:  A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball
dropped from a height of 10 feet bounces 6 feet high, the index is 0.6, and the total distance traveled by the ball is
16 feet after one bounce. If the ball were to continue bouncing, the distance after two bounces would be 10 ft 6 111 ft
6 ft 3.6 ft 5 25.6 ft. Note that the distance traveled for each successive bounce is the distance to the floor plus 0.6
of that distance as the ball comes back up. Write a program that lets the user enter the initial height
from which the ball is dropped and the number of times the ball is allowed to
continue bouncing. Output should be the total distance traveled by the ball.
Solution:

    ....
"""
height = float(input("Nhập độ cao mà quả bóng được thả xuống: "))
bounci_index = float(input("Nhập chỉ số độ nảy của bóng: "))
bounces = int(input("Nhập số lần bóng được phép tiếp tục nảy: "))
distance = height
for i in range(bounces-1):
   height *= bounci_index
   distance += 2*height
   distance += height*bounci_index
   print('\nTổng quãng đường đã đi là: ' + str(distance) + ' cm.')