# start at 2
# check each number to a limit - if number is not prime number, skip it
# Otherwise, mark it 

is_prime = []

for n in range(2,50):
    if n == 1:
        continue
    if n % 3 == 0:
        is_prime.append(n)

print("PRIME: ", is_prime)

max = 50
primes = []
for n in range(2, max +1):
    for m in range(2, n-1):
        if n % m == 0:
            break # not prime
        else:
            primes.append(n)

print(primes)