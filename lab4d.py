#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(strFive):
    # Place code here - refer to function specifics in section below
    return strFive[0:5]

def last_seven(strSeven):
    # Place code here - refer to function specifics in section below
    return strSeven[-7:]

def middle_number(intMiddle):
    # Place code here - refer to function specifics in section below
    strMiddle = str(intMiddle)
    return strMiddle[1] + strMiddle[2]


def first_three_last_three(strFirst3,strLast3):
    # Place code here - refer to function specifics in section below
    return strFirst3[0:3] + strLast3[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
