'''
Created on Aug 24, 2021

@author: Karthik
'''
import collections
stack = collections.deque()
print("Select the Operation \n 1.Push \n 2.Pop \n 3.Top \n 4.Quit")
def push(N):
    if len(stack)==N :
        print("Stack is full")
    else :
        element = input("Enter the Element :")
        stack.append(element)
        print(stack)
def pop():
    if not stack or len(stack)==0 : # one condition is enough
        print("Stack is Empty")
    else:
        e = stack.pop()
        print("Removed Element :",e)
        print(stack)
def top(stack):
    if len(stack) != 0 :
        print("Top element :",stack[-1])
    else :
        print("Stack is Empty")

N = int(input("Enter the limit of stack :"))
while True :
    print("Choice :",end='')
    choice = int(input())
    if choice == 1 :
        push(N)
    elif choice == 2 :
        pop()
    elif choice == 3 :
        top(stack)
    elif choice == 4 :
        break
    else :
        print("Enter the correct choice")
print("Program Execution completed")
    
