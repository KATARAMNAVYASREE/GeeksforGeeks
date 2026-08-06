class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    seen = set()
        ans = ""

        for ch in s:
            if ch not in seen:
                seen.add(ch)
                ans += ch

        return ans