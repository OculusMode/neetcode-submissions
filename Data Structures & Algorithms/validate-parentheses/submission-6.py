class Solution:
    def isValid(self, s: str) -> bool:
        open_brakets = {'(', '{', '['}
        close_brakets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        st = []
        for i in s:
            if i in open_brakets:
                st.append(i)
            else:
                if not st:
                    return False
                braket = st.pop()
                if braket != close_brakets[i]:
                    return False
        return not st