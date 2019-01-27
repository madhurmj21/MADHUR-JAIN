def is_prime(num):
    prime_number = True
    for i in range(2,num-1):
        if num % i == 0:
            prime_number = False

    if prime_number:
        print ("{} is prime number".format(num))
    else:
        print ("{} is not prime number".format(num))

is_prime(23)