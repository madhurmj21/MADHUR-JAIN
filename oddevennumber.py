def is_odd(num):
        if num % 2 == 1:
            return('{} is home odd'.format(num))
        else:
            return('{} is not odd'.format(num))

def is_even(number):
    if number % 2 == 0:
        print("{} is even number".format(number))
    else :
        print("{} is not even number".format(number))
is_even(23)
print(is_odd(23))