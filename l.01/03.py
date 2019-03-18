'''
Total Salary
Send Feedback
Write a program to calculate the total salary of a person. The user has to enter the basic salary (an integer) and the grade (an uppercase character), and depending upon which the total salary is calculated as -

    totalSalary = basic + hra + da + allow – pf

where :

hra   = 20% of basic
da    = 50% of basic
allow = 1700 if grade = ‘A’
allow = 1500 if grade = ‘B’
allow = 1300 if grade = ‘C' or any other character
pf    = 11% of basic.

Round off the total salary and then print the integral part only.
Input format :

Basic salary & Grade (separated by space)

Output Format :

Total Salary


'''

input = input().strip().split(' ')
input[0] = int(input[0])

def get_allow(a):
    allow = {
        'A' : 1700,
        'B' : 1500,
    }
    return allow.get(a,1300)

print( round( (1.59*input[0]) + get_allow(input[1]) ) )
