class Solution:
    def findEquilibrium(self, arr):
        total = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            right_sum = total - left_sum - arr[i]
            
            if left_sum == right_sum:
                return i
                
            left_sum += arr[i]
        return -1