def primes():
    n = int(input())
    num = 3
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        while num <= n//3:
            if n%num == 0:
                return False
            num += 2
        return True

while True:
    print(primes())