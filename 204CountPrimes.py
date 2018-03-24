'''
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

'''


class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        primes = [True] * n
        primes[:2] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

'''
Count prime numbers up to n (inclusive)???.
'''
aa = Solution()
print(aa.countPrimes(5))