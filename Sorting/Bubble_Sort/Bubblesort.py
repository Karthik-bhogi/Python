#use < for getting descending order and > for getting ascending order
num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)] # for user input
# list1 = [10,23,4,23,0] #for direct declaration
#first method
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print("First method :",list1)

#second method
for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print("Second method :",list1)
