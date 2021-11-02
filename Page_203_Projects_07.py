"""
Author: Mai Duc Nhat Minh
Date: 20/10/2021
Problem:    Write a recursive function that expects a pathname as an argument. The pathname
can be either the name of a file or the name of a directory. If the pathname
refers to a file, its name is displayed, followed by its contents. Otherwise, if the
pathname refers to a directory, the function is applied to each name in the directory.
Test this function in a new program.
Solution:

    ....
"""
import os


def print_file(file_name):
    with open(file_name, "r") as ifl:
        for data_line in ifl:
            print(data_line)


def myFind(input_path, z):
    spac = ''
    for i in range(z):
        spac = spac + ' '
        if (os.path.isdir(input_path)):
            for contents in os.listdir(input_path):
                new_content = os.path.join(input_path, contents)
                print(spac + new_content)
                if (os.path.isdir(new_content)):
                    myFind(new_content,z+1)
                else:
                    print(spac + input_path)
                    print_file(input_path)