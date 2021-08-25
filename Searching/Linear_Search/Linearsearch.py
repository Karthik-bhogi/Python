#Linear Searching
def linearsearch(list1,key):
    list2 = []
    for i in range(len(list1)):
        if list1[i]== key :
            list2.append(i)
        else :
            continue
    return list2

num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)]
key = int(input("Enter the Key element :"))
print("Given list :",list1)
print("Given key :",key)
l = linearsearch(list1, key)
if len(l) != 0 :
    for i in l :
        print("The element is found at index ",i)
else :
    print("The element is not found")
