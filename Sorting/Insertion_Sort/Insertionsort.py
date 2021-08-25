# Ascending Order
def insertionsort1(list1):
    for i in range(1,len(list1)):
        current_element = list1[i]
        pos = i 
        while current_element < list1[pos-1] and pos>0:
            list1[pos] = list1[pos-1]
            pos = pos -1
        list1[pos] = current_element

#Descending Order
def insertionsort2(list1):
    for i in range(1,len(list1)):
        current_element = list1[i]
        pos = i 
        while current_element > list1[pos-1] and pos>0:
            list1[pos] = list1[pos-1]
            pos = pos -1
        list1[pos] = current_element
        
num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)]
print("Given list :",list1)
insertionsort1(list1)
print("Ascending Order :",list1)
insertionsort2(list1)
print("Descending Order :",list1)
