def prime_numbers(low, high):
    if not isinstance(low, int) or not isinstance(high, int) or low >= high:
        return []

    primes = []
    for num in range(low, high + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes


print(prime_numbers(1, 10))
