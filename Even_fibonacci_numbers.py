n=int(input("Enter number:"))
a,b,sum=0,1,0
for i in range(1,n+1):
    a,b=b,a+b
    if b%2==0:
        sum+=b
    print(b) 
print("sum=",sum)