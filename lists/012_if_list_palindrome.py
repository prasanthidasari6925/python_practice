#checking if list is palindrome
num=list(map(int,input().split()))
def reversing_list(num):
    start=0
    end=len(num)-1
    while start<end:
        num[start],num[end]=num[end],num[start]
        start+=1
        end-=1
    return num
temp_num=num[:]
reversed_num=reversing_list(num)
if temp_num==reversed_num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")