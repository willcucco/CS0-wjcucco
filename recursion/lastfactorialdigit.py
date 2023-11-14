"""
Name: Will Cucco
Date: 11/13/23
CSCI 110

Read and solve the Kattis problem - The Last Factorial Digit: https://open.kattis.com/problems/lastfactorialdigit

Steps:
    1. Input the amount of numbers to calculate the last digit of
    2. Calculate the factorial number of the input numbers after step 1
    3. Print the last digit of the calculated factorial number
"""


import math


def main():
    """Main function that solves the problem"""
    n = int(input())
    for i in range(n):
        num = int(input())
        factorial_num = find_num(num)
        str_factorial_num = str(factorial_num)
        find_last_digit = str_factorial_num[-1]
        print(find_last_digit)


def find_num(num):
    """Finds factorial of input number"""
    find_factorial = math.factorial(num)
    return find_factorial


if __name__ == "__main__":
    main()