import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i) == 0:
            return False
    return True


def listGame(num):
    if isPrime(num):
        return 1
    count = 1
    x = 2
    while x < int(num / 2) + 1:
        if num % x == 0:
            quotient = num / x
            print("num, x, quotient: ", num, x, quotient)
            if isPrime(x) and isPrime(quotient):
                return 2
            elif isPrime(x) and not isPrime(quotient):
                return listGame(quotient)
            elif not isPrime(x) and not isPrime(quotient):
                return listGame(x) + listGame(quotient)
        x += 1
    return count



num = int(input())

print(listGame(num))