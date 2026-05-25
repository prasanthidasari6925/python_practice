#secod largest element in list to deal with -ve num too
num=list(map(int,input().split()))
largest=float('-inf')
sec_largest=float('-inf')
for i in range(len(num)):
    if num[i]>largest:
        sec_largest=largest
        largest=num[i]
    elif num[i]>sec_largest and num[i]!=largest:
        sec_largest=num[i]
if sec_largest==float('-inf'):
    print("No second largest element")
else:
    print(sec_largest)