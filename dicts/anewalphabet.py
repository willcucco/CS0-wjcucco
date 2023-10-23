"""
Author: Will Cucco
Date: 10/23/23
CSCI 110

Read and solve the problem - A New Alphabet: https://open.kattis.com/problems/anewalphabet

Steps:
    1. Create a dictionary for the new alphabet as listed in the problem
"""


dict1 = {'A': '@', 'a': '@', 'B': '8', 'b': '8', 'C': '(', 'c': '(', 'D': '|)', 'd': '|)', 'E': '3', 'e': '3', 'F': '#', 'f': '#', 'G': '6', 'g': '6', 'H': '[-]', 'h': '[-]', 'I': '|', 'i': '|', 'J': '_|', 'j': '_|', 'K': '|<', 'k': '|<', 'L': '1', 'l': '1', 'M': '[]\/[]', 'm': '[]\/[]', 'N': '[]\[]', 'n': '[]\[]', 'O': '0', 'o': '0', 'P': '|D', 'p': '|D', 'Q': '(,)', 'q': '(,)', 'R': '|Z', 'r': '|Z', 'S': '$', 's': '$', 'T': '\'][\'', 't': '\'][\'', 'U': '|_|', 'u': '|_|', 'V': '\/', 'v': '\/', 'W': '\/\/', 'w': '\/\/', 'X': '}{', 'x': '}{', 'Y': '`/', 'y': '`/', 'Z': '2', 'z': '2'}


def main():
    """Main function that solves the problem"""
    input_str = input()
    ans = newdict(input_str)
    print(ans)


def newdict(input_str):
    """Turns current alphabet into a new alphabet"""
    output_str = ''
    for char in input_str:
        if char in dict1:
            output_str += dict1[char]
        else:
            output_str += char

    return output_str


if __name__ == "__main__":
    main()