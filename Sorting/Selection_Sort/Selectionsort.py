# use max() in place of min() function to sort numbers in descending order
#using min or max functions
num = int(input("How many numbers you want are there in the list ? :"))
list1 = [int(input("Enter Number :")) for x in range(num)] # for user input
# list1 = [3,3,2,78,2,0] #for direct declaration

for i in range(len(list1)-1):    
    m_val = min(list1[i:])
    m_ind = list1.index(m_val,i)
    if list1[i] != list1[m_ind] :
        list1[i],list1[m_ind]= list1[m_ind],list1[i]
print(list1)

#withput using min or max functions
for i in range(len(list1)-1):  
    m_val = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < m_val :
            m_val = list1[j]
    m_ind = list1.index(m_val,i)
    if list1[i] != list1[m_ind] :
        list1[i],list1[m_ind]= list1[m_ind],list1[i]
print(list1)

#withput using min or max or index
for i in range(len(list1)-1):  
    m_ind = i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[m_ind] :
            m_val = i
    if list1[i] != list1[m_ind] :
        list1[i],list1[m_ind]= list1[m_ind],list1[i]
print(list1)
