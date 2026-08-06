class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        s = float('inf')
        ss = float('inf')
        small = []
        for num in arr:
            if num < s:
                ss = s
                s = num
            elif num < ss and num != s:
                ss = num
        if ss != float('inf'):
            small.append(s)
            small.append(ss)
        else:
            small.append(-1)
        return small
