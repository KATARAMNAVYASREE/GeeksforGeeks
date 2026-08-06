class Solution:
    def longestSubarray(self, arr, k):
        n = {}
        s = 0
        res = 0
        
        for i in range(len(arr)):
            s += arr[i]
            if s == k:
                res = i + 1
            if (s - k) in n:
                res = max(res, i - n[s - k])
            if s not in n:
                n[s] = i
        return res