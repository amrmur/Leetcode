class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, ret = len(nums), []

        for i in range(0, n - 2):
            if(i > 0 and nums[i - 1] == nums[i]):
                continue
            j = i + 1
            k = n - 1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0: k -= 1
                elif sum < 0: j += 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
        return ret

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
