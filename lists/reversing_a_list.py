#reversing a list
num=list(map(int,input().split()))
def reverse_in(digits):
    start=0
    end=len(digits)-1
    while start<end:
        digits[start],digits[end]=digits[end],digits[start]
        start+=1
        end-=1
    return digits
print(reverse_in(digits))