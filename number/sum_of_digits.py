#sum of digits
a=int(input("Enter number:"))
sum_of_digits=0
if a==0:
    sum_of_digits=1
else:
    a=abs(a)
    while a>0:
        sum_of_digits=sum_of_digits+a%10
        a=a//10
print(f"Sum of digits: {sum_of_digits}")