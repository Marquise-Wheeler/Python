#!/usr/bin/python3

# Youtube shorts @b001

# Initializw numbers variable with a range from 1, 1000.
nums=range(1,1001)
# Print statement to verify program functionality remove comment to check.
#print(list(nums))

def is_prime(num):
    for x in range(2,num):
      if (num%x) == 0:
        return False
    return True

# Convert primes to a list to conserve memory
primes=list(filter(is_prime, nums))

print(primes)
