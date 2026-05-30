#merging two lists in sorting order
list1=list(map(int,input("Enter sorted list 1:").split()))
list2=list(map(int,input("Enter sorted list 2:").split()))
merged_list=[]
i=0
j=0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        merged_list.append(list1[i])
        i+=1
    else:
        merged_list.append(list2[j])
        j+=1
while i<len(list1):
    merged_list.append(list1[i])
    j+=1
while j<len(list2):
    merged_list.append(list2[j])
    j+=1
print(merged_list)