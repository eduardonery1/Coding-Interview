def prime():
    n = int(input())
    num = 2
    while num <= n//2:
        if n%num == 0: 
            return False
        num += 1
    return True

while True:
    print(prime())
