'''
Find character case
Send Feedback
Write a program to determine whether the entered character is in uppercase or lowercase, or is an invalid character.
Print

 1 for uppercase
 0 for lowercase
-1 for any other character (special characters or others)

Input format :

Single Character

Output format :

1 or 0 or -1

'''

char = input()

if char.isupper():
    print(1)
elif char.islower():
    print(0)
else:
    print(-1)