class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while(ord(s[i]) == 32):
            i -= 1
        
        num = 0
        while(i >= 0 and ord(s[i]) != 32):
            num += 1
            i -= 1
        return num

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
