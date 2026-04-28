class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s) - 1
        f = 0
        while l > f:
            f_ = s[f]
            l_ = s[l]
            skip = False
            if not f_.isalnum():
                f+=1
                skip = True
            if not l_.isalnum():
                l-=1
                skip = True
            if skip:
                continue
            if f_.lower() == l_.lower():
                f+=1
                l-=1
                continue
            return False
        return True
            