
prime_numbers = 0


def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


for i in range(int(input("How many numbers you wish to check: "))):
    if is_prime(i):
        prime_numbers += 1
        print(i)

print("We found " + str(prime_numbers) + " prime numbers.")
