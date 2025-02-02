class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        left, right = 0, len(height) - 1
        while(left < right):
            lH, rH, cur = height[left], height[right], min(height[left], height[right]) * (right - left)
            if cur > curMax: curMax = cur
            if lH <= rH: left += 1
            elif rH <= lH: right -= 1
        return curMax
    # Time Complexity: O(n)
    # Space Complexity: O(1)
