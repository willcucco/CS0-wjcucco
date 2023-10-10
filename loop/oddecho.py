"""
Author: Will Cucco
Date: 10/2/23
CSCI 110
Odd Echo Lab

Solve the Kattis Odd Echo problem - https://open.kattis.com/problems/oddecho

Steps:
1. Create a program that echos every third word from the input
"""


def main():
    """Main function that solves the problem
    """
    n = read_int_data()
    for i in range(n):
        word = input().strip()
        if (i+1)%2 == 1:
            print(word)
        else:
            continue
    ans = read_int_data()
    print(ans)
    
    
def read_int_data():
    #n = int(input())
    n = input()
    n = int(n)
    return n



if __name__ == "__main__":
    main()