'''
Terms of AP
Send Feedback
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
N varies from 1 to 1000.
Input format :

Integer x

Output format :

Terms of series (separated by space)
'''

x = int(input())
n = 1
for i in range(x):
    if ((n%2) == 0) and ((n%4) != 0):
        n += 1
    print( (3*n) + 2 )
    n += 1


# Watch time complexity very clearly