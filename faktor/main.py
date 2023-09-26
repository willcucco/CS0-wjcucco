"""
Kattis problem - Faktor
CSCI 110
Fall 2023
Author: Will Cucco
Date: 9/22/23

Problem statement: Trying to solve for the minimum amount of scientists needed 
based on the total count of citations recieved by articles published in the journal 
and the total number of articles published

Algorithm steps:
1. Use two functions from the demo code
2. Create an algorithm that can solve the problem
"""

import sys


def main():
    """Main function that solves the problem
    """
    # data = read_data()
    # ans = answer(data)
    # print(ans)


# def answer(a: int, b: int) -> int:
    # """Function returns data input as answer
    # Returns: number output
    # """
    # num1 = input()
    # num2 = input()
    # answer(num1, num2)
    # return answer


def faktor(articles, impact) -> int:
    """_summary_

    Args:
        articles (int): amount of articles published
        impact (int): the impact factor

    Returns:
        int: number of scientists
    """
    num_scientists = int(articles)*(int(impact)-1)+1
    print(num_scientists)
    return faktor


# def read_data() -> int:
    # Reads the int data input and returns it
    # Returns:
    # int: data read from std input
    # data = input()
    # return data


if __name__ == "__main__":
    a, i = sys.stdin.readline().split()
    faktor(a, i)


# articles, impact = map(int, input().split())

# num_scientists = (articles * (impact - 1)) + 1

# print (num_scientists)
