#Find pair with given sum
num=list(map(int,input("Enter the list").split()))
target=int(input())
if len(num)==0:
    print("List is empty")
else:
    for i in num:
        for j in num:
            if i+j==target:
                print(f"({i},{j})",end=' ')