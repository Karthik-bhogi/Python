'''
Created on Aug 25, 2021

@author: Karthik
'''
import queue
q = queue.PriorityQueue()
print("Select the Operation \n 1.Enqueue \n 2.Dequeue \n 3.Quit")
def enqueue():
    element = input("Enter the Element :")
    q.put(element)

def dequeue():
    if not q : # one condition is enough
        print("queue is Empty")
    else:
        e = q.get()
        print("Removed Element :",e)
       
while True :
    print("Choice :",end='')
    choice = int(input())
    if choice == 1 :
        enqueue()
    elif choice == 2 :
        dequeue()
    elif choice == 3 :
        break
    else :
        print("Enter the correct choice")
print("Program Execution completed")