class Solution:
	def removeVowels(self, s):
		# code here
		vowels = "aeiou"
        ans = ""

        for ch in s:
            if ch not in vowels:
                ans += ch

        return ans