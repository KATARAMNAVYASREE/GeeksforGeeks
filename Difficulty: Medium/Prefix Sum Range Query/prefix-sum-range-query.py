class Solution:
    def rangeSumQueries(self, arr, queries):
        n = len(arr)
        if n == 0:
            return []
        prefix = [0]*n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]
        res = []
        for L, R in queries:
            if L == 0:
                res.append(prefix[R])
            else:
                res.append(prefix[R] - prefix[L - 1])

        return res