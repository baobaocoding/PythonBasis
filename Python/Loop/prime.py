def isPrime(number):
    """ determine if a number is a prime """
    prime = True
    for i in range(2, int(number ** (0.5))):
        if number % i == 0:
            prime = False
            break
    return prime

# A is divisable by B : A % B == 0
# the power sign is **


print(isPrime(12))  # this should be false
print(isPrime(13))  # this should be true
