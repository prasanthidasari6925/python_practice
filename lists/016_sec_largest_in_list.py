#secod largest element in list
num=list(map(int,input().split()))
largest=num[0]
sec_largest=-1
for i in range(len(num)):
    if num[i]>largest:
        sec_largest=largest
        largest=num[i]
    elif num[i]>sec_largest and num[i]!=largest:
        sec_largest=num[i]
if sec_largest==-1:
    print("No second largest element")
else:
    print(sec_largest)