start=int(input("Start:"))
to=int(input("stop:"))
number=1
while number>=1:
    for i in range(start,to+1):
        if number%i==0:
            print(number)
            number+=1
        else:
            print("nothing")
        number+=1