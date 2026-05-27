#merging two lists
list1=list(map(int,input("Enter sorted list 1:").split()))
list2=list(map(int,input("Enter sorted list 2:").split()))
merged_list=[]
for i in range(len(list1)):
    merged_list.append(list1[i])
for i in range(len(list2)):
    merged_list.append(list2[i])
print(merged_list)