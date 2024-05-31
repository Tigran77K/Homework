#Write a function that prints all prime numbers up to a given limit.
def prime_num(num):
    prime_numbers = [2]
    stop = 3
    while stop < num:
        prime = True
        for i in range(2, int(stop ** 0.5) + 1):
            if stop % i == 0:
                prime = False
                break
        if prime:
            prime_numbers.append(stop)
        stop += 2
    return prime_numbers
print(prime_num(100))
