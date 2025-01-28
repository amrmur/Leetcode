class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        for i in range(0, n):
            count += d.get(s[i])
            if(i + 1 < n):
                if(s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')):
                    count -= 2
                if(s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')):
                    count -= 20
                if(s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M')):
                    count -= 200
        return count
        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
