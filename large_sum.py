var =int(input("Enter the Number"))
sum=0
f=open("large_sum.txt",'w')
for i in range(0,var+1):
    sum+=i
f.write(sum)  
f.close()