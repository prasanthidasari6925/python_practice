#check if 2 lists are equal
list1=list(map(int,input("Enter sorted list 1:").split()))
list2=list(map(int,input("Enter sorted list 2:").split()))
if len(list1)!=len(list2):
    print("Both lists are not equal")
else:
    is_equal=True
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            is_equal=False
            break
if is_equal:
    print("Both lists are equal")
else:
    print("Both lists are not equal")