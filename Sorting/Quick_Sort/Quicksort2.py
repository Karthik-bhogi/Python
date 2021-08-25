'''
Created on Aug 22, 2021

@author: Karthik
'''
# to get the correct position of the pivot element
#we have taken last element as pivot
# Ascending order
def pivot_place1(list1,first,last):
    pivot = list1[last]
    left = first
    right = last-1
    while True :
        while left<=right and list1[left] <= pivot :
            left = left + 1
        while left<=right and list1[right] >= pivot :
            right = right - 1
        if right < left :
            list1[last],list1[left] = list1[left],list1[last]
            break
        else :
            list1[left],list1[right] = list1[right],list1[left]
    return left

#descending order
def pivot_place2(list1,first,last):
    pivot = list1[last]
    left = first
    right = last-1
    while True :
        while left<=right and list1[left] >= pivot :
            left = left + 1
        while left<=right and list1[right] <= pivot :
            right = right - 1
        if right < left :
            list1[last],list1[left] = list1[left],list1[last]
            break
        else :
            list1[left],list1[right] = list1[right],list1[left]
    return left

def quicksort1(list1,first,last):
    if first < last :
        p1 = pivot_place1(list1, first, last) 
        quicksort1(list1,first,p1-1)
        quicksort1(list1,p1+1,last)

def quicksort2(list1,first,last):
    if first < last :
        p2 = pivot_place2(list1, first, last) 
        quicksort2(list1,first,p2-1)
        quicksort2(list1,p2+1,last)
        
#main
num = int(input("How many numbers you want are there in the list ? :"))
list1 = []
for k in range(num):
    list1.append(int(input("Enter Number :")))
# list1 = [56,26,93,17,31,44,17]
print("Given list :",list1)
n = len(list1)
quicksort1(list1,0,n-1)
print("Ascending Order :",list1)
quicksort2(list1,0,n-1)
print("Descending Order :",list1)


    