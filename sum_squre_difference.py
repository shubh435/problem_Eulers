sum1,sum2=0,0
n=int(input("n:"))
for i in range(1,n+1):
    sum1=sum1+(i**2)
    sum2=i+sum2

print("Sum Squere difference is:",(sum2**2)-sum1)