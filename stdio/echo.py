"""
    Echo Echo Echo Lab
    By: Will Cucco
    CSCI 110
    Date: 9/6/23

    Goal: to solve the the Kattis "Echo Echo Echo" problem - https://open.kattis.com/problems/echoechoecho

    1. Create an algorithm that will print "Echo" three times from a command containing only one "Echo"
    2. Upload to Kattis to see if the solution is successful
    3. Paste a screenshot of a successful solution from Kattis to the "stdio" folder
"""

ECHO = input().strip()
print(ECHO + " " + ECHO + " " + ECHO + " ")