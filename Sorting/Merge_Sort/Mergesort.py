#Mergesort
#Ascending order
def mergesort1(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort1(left_list)
        mergesort1(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list) :
            if left_list[i]<right_list[j]:
                list1[k] = left_list[i]
                i = i+1
                k = k+1
            else :
                list1[k] = right_list[j]
                j = j+1
                k = k+1
        while i < len(left_list) :
            list1[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list) :
            list1[k] = right_list[j]
            j = j+1
            k = k+1

#Descending Order
def mergesort2(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort2(left_list)
        mergesort2(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list) :
            if left_list[i]>right_list[j]:
                list1[k] = left_list[i]
                i = i+1
                k = k+1
            else :
                list1[k] = right_list[j]
                j = j+1
                k = k+1
        while i < len(left_list) :
            list1[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list) :
            list1[k] = right_list[j]
            j = j+1
            k = k+1

num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)]
print("Given list :",list1)
mergesort1(list1)
print("Ascending Order :",list1)
mergesort2(list1)
print("Descending Order :",list1)
