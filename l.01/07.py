'''
Number Pattern 1
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
11
111
1111

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines

'''

input = int(input())

for row in range(input):
    for i in range(row+1):
        print(1,end='')
    print()