class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_ = {}
        for s in strs:
            ss = str(sorted(s))
            if ss in strs_:
                strs_[ss].append(s)
            else:
                strs_[ss] = [s]
        return list(strs_.values())
