class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join([i for i in s if i.isalpha() or i.isdigit()])).lower()
        return s == s[::-1]
        