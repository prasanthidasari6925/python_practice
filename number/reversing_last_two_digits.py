#reversing last two digits
a=int(input("Enter number:"))
print((a%10)*10 + (a//10)%10)