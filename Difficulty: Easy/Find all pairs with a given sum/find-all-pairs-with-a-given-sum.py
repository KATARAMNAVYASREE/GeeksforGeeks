class Solution:
    def allPairs(self, target, arr1, arr2):
        freq = {}
        res = []
        for num in arr2:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        arr1.sort()
        for i in arr1:
            need = target-i
            if need in freq:
                for j in range(freq[need]):
                    res.append([i,need])
        return res