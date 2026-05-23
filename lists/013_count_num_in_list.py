#count the number in list
num_list=list(map(int,input().split()))
num=int(input("Enter the number you want to count:"))
count=0
for i in range(0,len(num_list)):
    if num==num_list[i]:
        count+=1
if count==0:
    print(f"{num} doesn't exist in the list")
else:
    print(f"Number of {num}s is: {count}")