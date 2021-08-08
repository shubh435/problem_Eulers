#Reverse

def reverse(number):
    rev=0
    while number>0:
            rev=rev*10+number%10
            number=number//10

    return(rev)


#is Palindrome
def isPalindrome(number):
    
    if reverse(number)==number:
        return("palindrome of number is :{}".format(reverse(number)))
    else:
        return("Not Palindrome of number {} is :{}".format(number,reverse(number)))
number=int(input("Enter the Number:"))
print(isPalindrome(number))