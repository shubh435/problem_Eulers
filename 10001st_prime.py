count=0
arr=[]
i=2
while i >1:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        # print("prime",i)
        arr.append(i)
        count+=1
    i+=1
    if count==10001:
        # print(arr[count])
        break
print("ans=",arr[10000])
