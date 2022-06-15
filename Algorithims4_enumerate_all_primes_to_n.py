# Write a program that takes an integer argument and returns all the primes between 1 and that integer
# for example if the input is 18 you should return [2, 3, 5, 7, 11, 13, 17]
# A natural number is called a prime if its bigger than 1 and has no divisors other than 1 and itself

# (N^2)
# def enumerate_primes(n):
#    primes = []

#    for i in range(2, n + 1):
#        for p in range(2, i + 1):
#            if p == i:
#                primes.append(i)
#                break
#            if i % p == 0:
#                break

#    return primes

# O(N)
def enumerate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)

    for p in range(2, n + 1):    # 2, 3, 4, 5, ..., n - 1, n
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):   # range(start, stop, step)
                is_prime[i] = False # 2, 4, 6, 8, 10, .... not prime numbers

    return primes


test_n = 18  # [2, 3, 5, 7, 11, 13, 17]
print(enumerate_primes(test_n))