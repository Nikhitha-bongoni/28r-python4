def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1  
    while not is_prime(n):
        n += 1
    return n

num = 10
print("Next prime after", num, "is:", next_prime(num))
