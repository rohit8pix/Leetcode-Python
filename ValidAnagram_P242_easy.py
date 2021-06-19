class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_1 = sorted(s)
        t_1 = sorted(t)
        if s_1 == t_1:
            return True
        else:
            return False
