"""
    R2 Lab
    Name: Will Cucco
    Date: 9/15/23
    CSCI 110

    Goal: To solve the Kattis "R2" problem - https://open.kattis.com/problems/r2

    1. Create a program that will find the mean of two numbers
    2. Upload to Kattis and take a screenshot of a successful submission
"""

r1, s = input().split()

r1 = int(r1)
s = int(s)

r2 = (2*s)-r1

print(int(r2))