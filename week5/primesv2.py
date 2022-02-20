# a prime number generator

# added an input to this original, and followed the tutor's optimisation steps

primes = []
upto = int ( 
        input ( "Enter a maximum number:" ) 
        ) + 1

for candidate in range ( 2 , upto ) :
    isPrime = True
    # only checks against the numbers already in the primes range
    for divisor in primes :
        if ( candidate % divisor == 0 ) :
            isPrime = False
            break
    if isPrime:
        primes.append ( candidate )

print ( primes )
