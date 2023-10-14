"""
Author: Will Cucco
Date: 10/10/23
CSCI 110
Avion assingment

Solve the kattis Avion problem - https://open.kattis.com/problems/avion

Steps:
1. Create a program that will take 5 lines of input and use slicing tool to find which input lines have the consecutive letters "FBI"
2. Code will print the amount of lines with "FBI" to the user
"""


def main():
    """Main function that solves the problem
    """
    fbi_blimp_indexes = []
    for i in range(5):
        s = input().strip()
        data = find_FBI(s)
        if data == 'positive':
            fbi_blimp_indexes.append(str(i+1))
        #elif data == 'negative':
            #print("HE GOT AWAY!")
        #else: 
            #continue
        
    if fbi_blimp_indexes:
        # write "if fbi_blimp_indexes == *value it gets when it has FBI data*. Use debug to see what value it has when input contains FBI"
        print(" ".join(fbi_blimp_indexes))
    else:
        print("HE GOT AWAY!")

    
def find_FBI(s):
    theIndex = s.find('FBI')
    if theIndex != -1:
        return 'positive'
    elif theIndex == -1:
        return 'negative'


if __name__ == "__main__":
    main()