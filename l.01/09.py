'''
Number Pattern 3
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
11
121
1221

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines


'''

import sys

input = int(input())
if input<1:
    sys.exit()

print(1)
for row in range(1,input):
    print('1',end='')
    for i in range(row-1):
        print('2',end='')
    print('1', end='\n')