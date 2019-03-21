## Read input as specified in the question.
## Print output as specified in the question.
'''
Sum or Product
Send Feedback
Write a program that asks the user for a number N and a choice C. And then give him the possibility to choose between computing the sum and computing the product of 1 ,..., N.
If user enters C is equal to -

 1 : Print sum of 1 to N numbers
 2 : Print product of 1 to N numbers
 Any other number : print -1

Input format :

Line 1 : Integer N
Line 2 : Choice C (1 or 2)

Output Format :

 Sum or product according to user's choice

'''
import math

n = int(input())
c = int(input())

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fact(n-1) * n

if c == 1:
    print( int((n * (n+1)) / 2) )
elif c == 2:
    #prod = fact(n)
    prod = math.factorial(n)
    print(prod)
else:
    print(-1)