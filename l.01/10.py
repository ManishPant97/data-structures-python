'''
Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4

1234
123
12
1

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines
'''


import sys

input = int(input())
if input<1:
    sys.exit()


for row in range(input):
    for i in range(1,input-row+1):
        print(i,end='')
    print()