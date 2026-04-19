#Prime number check
num=int(input("Enter Number:"))
num=abs(num)
if num<2:
    print("Not prime number")
else:
    is_prime=True
    for i in range(2,int(num/2)):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is prime number")