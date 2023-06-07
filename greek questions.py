'''Given a list, write a Python program to swap first and last element of the list.

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]'''

input = [12, 35, 9, 56, 24]#list type
print('original list',input)
c=len(input)#its contain length of list
a=input.pop(0)#12 pop working like remove the given indexing occurance from container and store in diff veriable
b=input.pop()#24 pop by default remove last indexing of acept tuple list,set,etc containet
input.insert(0,b)# insert working fill/add the given data on the bases of indexing place
input.insert(c,a)#
print("swap last and first number ",input)


#Examples:

'''
list : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]'''
# make a function
def swap(list):
    c=len(list)#its contain length of list
    print("orignal list is : ",list)
    a=list.pop(0)#12 pop working like remove the given indexing occurance from container and store in diff veriable
    b=list.pop()#24 pop by default remove last indexing of acept tuple list,set,etc containet
    list.insert(0,b)# insert working fill/add the given data on the bases of indexing place
    list.insert(c,a)#
    #print("swap last and first number :")
    return "swap last and first number :",list
li= [10,20,30,40,50]
print(swap(li))


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

