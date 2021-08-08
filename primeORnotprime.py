num = int(input("Enter Number"))
flag = False
for j in range(num):
    if j > 1:
        for i in range(2, num):
            if (j % i) == 0:
                flag = True
                break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")