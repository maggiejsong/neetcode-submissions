'''
Input = "abba"
Output = "abba"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = ""
        longest = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                left = i
                right = j

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1
                
                if left >= right and longest < (j - i + 1):
                    sol = s[i : j + 1]
                    longest = j - i + 1
        return sol
        