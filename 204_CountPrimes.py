# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution(object):
    def countPrimes(self, n):
        if n<3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for x in range(2, int(n** 0.5)+1):
            if primes[x]:
                primes[x*x:n:x] = [0] * len(primes[x*x:n:x])
        return sum(primes)

if __name__ == "__main__":
    n = 12
    print(Solution().countPrimes(n))