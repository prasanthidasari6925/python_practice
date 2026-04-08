#Counting the number of digits
num=int(input("Enter number:"))
count=0
if num==0:
    count=1
else:
    num=abs(num)
    while num>0:
        num=num//10
        count+=1
print(f"number of digitsd:{count}")