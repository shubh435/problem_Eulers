import logging 
import math 
logging.basicConfig(level=logging.DEBUG)
#facter of Number
def getFactor(number):
    factor=[]
    for  i in range(1,int(math.sqrt(number))+1):
        if number%i==0:
            factor.append(i)
            factor.append(number//i)
    return factor

logging.debug(getFactor(17))
#check Number is prime or not
def isPrime(number):
    return len(getFactor(number))==2

logging.debug('isPrime(24)=%s'%(isPrime(24)))
logging.debug('isPrime(17)=%s'%(isPrime(17)))

allFactor=getFactor(600851475143)
largestPrimeFactor=0
#for largest prime factor
for factor in allFactor:
    if isPrime(factor) and  factor>largestPrimeFactor:
        largestPrimeFactor=factor 
print(largestPrimeFactor)