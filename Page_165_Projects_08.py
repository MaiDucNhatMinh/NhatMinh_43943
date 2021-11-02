"""
Author: Mai Duc Nhat Minh
Date: 09/10/2021
Problem:    Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.
Solution:

    ....
"""
import re
import string
fre = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b [a-z]{1-15} \b', text_string)
for word in match_pattern:
    count = fre.get(word, 0)
    fre[word] = count+1
fre_list = fre.keys()
for words in sorted(fre_list):
    print(words, fre[words])