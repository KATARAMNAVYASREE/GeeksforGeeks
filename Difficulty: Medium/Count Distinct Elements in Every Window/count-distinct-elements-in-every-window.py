class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        res = []
        for i in range(k):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        res.append(len(freq))
        for i in range(k, len(arr)):
            if arr[i] in freq:
                freq[arr[i]] +=1
            else:
                freq[arr[i]] = 1
            freq[arr[i-k]] -= 1
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]

            res.append(len(freq))

        return res