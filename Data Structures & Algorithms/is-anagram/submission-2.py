class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        o = {}
        for i in s:
            o[i] = o.get(i, 0) + 1
        for i in t:
            o[i] = o.get(i, 0) - 1
        for i in o.values():
            if i!=0:
                return False
        return True