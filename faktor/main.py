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


def main():
    """Main function that solves the problem
    """
    # data = read_data()
    # ans = answer(data)
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    ans = faktor(a, b)
    print(ans)


def faktor(a, b) -> int:
    """_summary_

    Args:
        articles (int): amount of articles published
        impact (int): the impact factor

    Returns:
        int: number of scientists
    """
    ans = a*(b-1)+1
    return ans


if __name__ == "__main__":
    main()