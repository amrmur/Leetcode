class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = []

        i = 0
        while(i < n and ord(s[i]) == 32):
            i += 1

        while(i < n):
            beg = i
            while(i < n and ord(s[i]) != 32):
                i += 1
            words.insert(0, s[beg:i])

            while(i < n and ord(s[i]) == 32):
                i += 1
        return " ".join(words)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
