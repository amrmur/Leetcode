class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        iT, iS, lT, lS = 0, 0, len(t), len(s)
        while(iT < lT):
            if t[iT] == s[iS]: 
                iS += 1
                if iS == lS: return True
            iT += 1
        return False
