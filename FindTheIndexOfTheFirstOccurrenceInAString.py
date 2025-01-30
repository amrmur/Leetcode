class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # Time Complexity: O(n * m) n is haystack len and m is needle len 
        # Space Complexity: O(1)
