def factorial(num):
    if num<=1:
        return  1
    else:
        sum=num*factorial(num-1)
        return sum
num=int(input("Enter the Number:"))
digit_sum=0
sum=factorial(num)
print(sum)
while sum>0:
    r=sum%10
    digit_sum+=r
    sum=sum//10
print("Answer=",digit_sum)