#Binary Search
def binarysearch(list1,key):
    found = False
    low = 0
    high = len(list1)-1
    while low <= high and not found :
        mid = (low+high)//2
        if key == list1[mid] :
            found = True
        elif key > list1[mid]:
            low = mid+1
        elif key < list1[mid]:
            high = mid-1
    if found :
        print("The element is found")
    else :
        print("The element is not found")
# Main
num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)]
print("Given list :",list1)
list1.sort()
print("Sorted list :",list1)
key = int(input("Enter the Key element :"))
print("Given key :",key) 
