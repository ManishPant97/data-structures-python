'''
Find average Marks
Send Feedback
Write a program to input name (as a single character) and marks of three tests of a student (all integers). Then calculate and print the name and average (integer) of best two test marks.
All the test marks are integers and calculate average also as integer. That is, you need to print the integer part of average only, neglect the decimal part.
Input format :

Line 1 : Name (Single character)
Line 2 : 3 Test marks (separated by space)

Output format :

Name Average (separated by space)


'''

## Read input as specified in the question.
## Print output as specified in the question.

name = input()
marks = [int(m) for m in input().strip().split(' ')]
marks.sort()

print(name, int(sum(marks[-2:])/2))
