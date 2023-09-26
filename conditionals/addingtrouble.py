"""
Author: Will Cucco
CSCI 110
Date: 9/25/23
"Adding Trouble" problem

Goal: Solve the Kattis problem "Adding Trouble" - https://open.kattis.com/pronlems/addingtrouble

Steps:
1. Given three integers A, B, and C, make sure that A + B = C, and that they add together correctly
2. Test locally to make sure functions work properly
3. Upload to Kattis and submit a screenshot in the "conditionals" folder
"""


def main():
    """Main function that solves the problem
    """
    line = input()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    #if a + b == c:
       # print('correct!')
    #else:
        #print('wrong!')
    ans = answer(a,b,c)
    print(ans)


def answer(a,b,c):
    if a + b == c:
        return 'correct!'
    else:
        return 'wrong!'


if __name__ == "__main__":
    main()
