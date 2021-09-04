num=2000000
print(type(num))
sum=0
for i in range(2,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        sum+=i


print("sum=",sum)