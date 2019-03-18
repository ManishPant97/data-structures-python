'''
Sum of even & odd
Send Feedback
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits means numbers not the places. That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
Input format :

 Integer N

Output format :

Sum_of_Even_Digits Sum_of_Odd_Digits
(Print first even sum and then odd sum separated by space)
'''

input = input().strip()
even_sum = 0
odd_sum = 0
for c in input:
    if int(c) % 2 == 0:
        even_sum += int(c)
    else:
        odd_sum += int(c)

print(even_sum, ' ', odd_sum)

