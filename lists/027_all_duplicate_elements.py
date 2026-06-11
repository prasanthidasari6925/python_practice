#Find all duplicate elements
num=list(map(int,input("Enter the list").split()))
duplicate_elements=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            if num[i] not in duplicate_elements:
                duplicate_elements.append(num[i])
print(duplicate_elements)