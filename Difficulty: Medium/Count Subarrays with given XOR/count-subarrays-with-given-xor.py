class Solution:
    def subarrayXor(self, arr, m):
        freq = {0: 1}   # prefix_xor -> frequency
        prefix_xor = 0
        count = 0

        for num in arr:
            prefix_xor ^= num   # update running XOR

            # target prefix we need
            target = prefix_xor ^ k

            if target in freq:
                count += freq[target]

            # update frequency of current prefix_xor
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1

        return count