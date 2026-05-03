#fibanocci series
no_of_terms=int(input())
num1=0
num2=1
for i in range(0,no_of_terms):
    print(num1,end=" ")
    next_num=num1+num2
    num1=num2
    num2=next_num