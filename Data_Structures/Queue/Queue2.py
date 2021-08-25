'''
Created on Aug 25, 2021

@author: karthik
'''
queue = []
print("Select the Operation \n 1.Enqueue \n 2.Dequeue \n 3.First \n 4.Last \n 5.Quit")
def enqueue(N):
    if len(queue)==N :
        print("queue is full")
    else :
        element = input("Enter the Element :")
        queue.insert(0,element)
        print(queue)

def dequeue():
    if not queue or len(queue)==0 : # one condition is enough
        print("queue is Empty")
    else:
        e = queue.pop()
        print("Removed Element :",e)
        print(queue)

def front(queue):
    if not queue or len(queue)==0 : # one condition is enough
        print("queue is Empty")
    else:
        print("First Element :",queue[-1])

def back(queue):
    if not queue or len(queue)==0 : # one condition is enough
        print("queue is Empty")
    else:
        print("Last Element :",queue[0])
        
N = int(input("Enter the limit of stack :"))
while True :
    print("Choice :",end='')
    choice = int(input())
    if choice == 1 :
        enqueue(N)
    elif choice == 2 :
        dequeue()
    elif choice == 3 :
        front(queue)
    elif choice == 4 :
        back(queue)
    elif choice == 5 :
        break
    else :
        print("Enter the correct choice")
print("Program Execution completed")