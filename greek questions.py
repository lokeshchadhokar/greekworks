'''Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]'''
input = [12, 35, 9, 56, 24]
a=input.pop(0)
b=input.pop(-1)
print(input)
c=len(input)
'''this command shows you'''
input.insert(0,b)
input.insert(-1,a)
print(input)
print('hello world')
