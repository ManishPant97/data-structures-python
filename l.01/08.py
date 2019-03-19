'''
Number Pattern 2
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
11
202
3003

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
    print(row,end='')
    for i in range(row-1):
        print(0,end='')
    print(row, end='\n')