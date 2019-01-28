print ("function to find the factorial of a number")

num = input("Enter a number:")
def factorial(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact*i
    print ("factorial of {} is {}".format(num,fact))
factorial (num)   