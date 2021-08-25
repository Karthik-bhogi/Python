#Ascending Order
def shellsort1(list1):
    gap = len(list1)//2
    while gap > 0 :
        for i in range(gap,len(list1)) :
            current_element = list1[i]
            pos = i
            while pos >= gap and current_element <= list1[pos-gap] :
                list1[pos] = list1[pos-gap]
                pos = pos-gap
            list1[pos] = current_element
        gap = gap//2

#Descending Order    
def shellsort2(list1):
    gap = len(list1)//2
    while gap > 0 :
        for i in range(gap,len(list1)) :
            current_element = list1[i]
            pos = i
            while pos >= gap and current_element >= list1[pos-gap] :
                list1[pos] = list1[pos-gap]
                pos = pos-gap
            list1[pos] = current_element
        gap = gap//2

num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)]
print("Given list :",list1)
shellsort1(list1)
print("Ascending Order :",list1)
shellsort2(list1)
print("Descending Order :",list1)
