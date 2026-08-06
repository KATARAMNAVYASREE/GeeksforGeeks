class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        i = 0
        j = 0
        cnt = 0
        maxi = -1
        freq = [0]*26
        
        while j < n:
            freq[ord(s[j]) - ord('a')] += 1
            
            if freq[ord(s[j]) - ord('a')] == 1:
                cnt += 1
            
            while cnt > k:
                freq[ord(s[i]) - ord('a')] -= 1
                
                if freq[ord(s[i]) - ord('a')] == 0:
                    cnt -= 1
                i += 1
            if cnt == k:
                maxi = max(maxi,j-i+1)
            j += 1
        return maxi