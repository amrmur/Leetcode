class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        k = len(s)
        for i in range(1, len(strs)):
            if(k > len(strs[i])): k = len(strs[i])
            for j in range(0, k):
                if(strs[i][j] != s[j]):
                    k = j
                    break
        return s[0:k]
        # Time Complexity: O(n*k) n is length of strs and k is shortest string length
        # Space Complexity: O(1)
                    
