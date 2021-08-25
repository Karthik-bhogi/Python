'''
Created on Aug 25, 2021

@author: Karthik
'''
import queue
q = queue.Queue()
print("Select the Operation \n 1.Enqueue \n 2.Dequeue \n 3.Quit")
def enqueue():
    element = input("Enter the Element :")
    q.put(element)
    print(q)

def dequeue():
    if not q : 
        print("queue is Empty")
    else:
        e = q.get()
        print("Removed Element :",e)
        print(q)
       
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