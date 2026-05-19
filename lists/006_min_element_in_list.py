#minimum number in a list
num=list(map(int,input().split()))
min_num=digits[0]
for i in range(1,len(digits)):
    if digits[i]<min_num:
        min_num=digits[i]
print(min_num)
