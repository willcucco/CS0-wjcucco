"""
Falling Apart and Unittest

Author: Will Cucco
Date: 10/7/23
CSCI 110

Read and solve the problem "Falling Apart" - https://open.kattis.com/problems/fallingapart

Steps:
    1. Record the number of pieces that the integer shattered into
    2. :
        1. 
"""


def main():
    """Main function that solves the problem
    """
    n = int(input())
    PieceValue = [int(x) for x in input().split()]
    ans = answer(PieceValue)
    strAns = []
    for i in ans:
        strAns.append(str(i))
    strAns = ' '.join(strAns)
    print(strAns)


def answer(PieceValue):
    alice = 0
    bob = 0
    while PieceValue:
        alice += max(PieceValue)
        PieceValue.remove(max(PieceValue))
        if PieceValue:
            bob += max(PieceValue)
            PieceValue.remove(max(PieceValue))
    
    return alice, bob


if __name__ == "__main__":
    main()