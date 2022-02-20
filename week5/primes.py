# a prime number generator

# had to amend this after the initial run, I had left the if IsPrime ... code at lines 13 and 14 inside
# the for loop at line 10, so it printed each non-prime number once, and each prime number the number of
# times it had been divided.

primes = []

for candidate in range ( 2 , 101 ) :
    isPrime = True
    for divisor in range ( 2 , candidate ) :
        if ( candidate % divisor == 0 ) :
            isPrime = False
            break
    if isPrime:
        primes.append ( candidate )

print(primes)
