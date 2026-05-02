#LCM using formula
num1 = int(input())
num2 = int(input())
num1 = abs(num1)
num2 = abs(num2)
if num1 == 0 or num2 == 0:
    print("GCD:", max(num1, num2))
    print("LCM: 0")
else:
    gcd = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    lcm = (num1 * num2) // gcd
    print("GCD:", gcd)
    print("LCM:", lcm)