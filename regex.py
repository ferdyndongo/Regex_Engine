#!/usr/bin/env python 3
from regex_functions import match

string = input()
regex, char = string.split('|')
# print(matching(regex, char))
print(match(regex, char))
