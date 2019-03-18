'''
Roots of quadratic equation
Send Feedback
Write a program to calculate the roots of a given quadratic equation -

      a(x^2) + bx + c = 0

Print roots specifying their nature. If roots are imaginary, no need to print the roots.
Print the nature of roots in the form of an integer -

 0 : if roots are real & same
 1 : if roots are real & different
-1 : if roots are imaginary

Round off the roots and then print the integral part only i.e. without any decimal places.
You can assume that, input will always be a quadratic equation.
Input format :

a b c (separated by space)

Output format :

Line 1 : Nature of roots (0 or 1 or -1)
Line 2 : Root 1 and Root 2 (separated by space)

'''
input = [int(n) for n in input().strip().split(' ')]
d = (input[1]**2) - (4*input[0]*input[2])
if d==0:
    print(0)
    ax = round((-input[1]) / (2 * input[0]))
    print(ax, ' ', ax)
elif d>0:
    print(1)
    ax = round((-input[1] + pow(d,0.5)) / (2 * input[0]))
    bx = round((-input[1] - pow(d,0.5)) / (2 * input[0]))
    print(ax, ' ', bx)
else:
    print(-1)