'''
Find power of a number
Send Feedback
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Input format :

Two integers x and n (separated by space)

Output Format :

x^n (i.e. x raise to the power n)
'''

input = [ int(i) for i in input().strip().split(' ') ]
print(input[0] ** input[1])