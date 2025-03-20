def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = [x for x in range(1, 101) if is_prime(x)]
print(primes)
