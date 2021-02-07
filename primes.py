def is_prime(n):
    cur = 2
    while cur ** 2 <= n:
        if n % cur == 0:
            return false
        cur++
    return true


if __name__ == "__main__":
    n = int(input())
    if is_prime(n):
        print("The number if prime!!")
    else:
        print(It is not prime)
