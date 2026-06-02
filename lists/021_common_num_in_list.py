#Find common elements
list1=list(map(int,input("Enter sorted list 1:").split()))
list2=list(map(int,input("Enter sorted list 2:").split()))
com_elements=[]
for i in list1:
    for j in list2:
        if i==j:
            com_elements.append(i)
        j+=1
    i+=1
print(com_elements)