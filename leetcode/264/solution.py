class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cache = [1]
        s2, s3, s5 = 0, 0, 0
        for i in range(n+1):
            k2 = cache[s2] * 2
            k3 = cache[s3] * 3
            k5 = cache[s5] * 5
            m = min(k2, k3, k5)
            cache.append(m)
            if m == k2:
                s2 += 1
            if m == k3:
                s3 += 1
            if m == k5:
                s5 += 1
        return cache[n-1]
