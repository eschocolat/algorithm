class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        k = n
        i = 2
        while i * i <= n and k != 1:
            while k % i == 0:
                k /= i
            if (k != 1):
                i += 1
            if i > 5:
                return False
        if k > 5:
            return False
        return True
