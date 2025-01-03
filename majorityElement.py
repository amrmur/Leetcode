class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BOYER MOORE MAJORITY VOTE ALGORITHM
        # We have a candidate and count
        # When we encounter a number different from the candidate, count decrements
        # change the candidate to the current number if count hits zero
        # then we increment if the candidate is the same as the current number
        # whatever the candidate is at the end is the majority number in the array

        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if(nums[i] != candidate):
                count = count - 1
            if(count <= 0):
                candidate = nums[i]
            if(candidate == nums[i]):
                count = count + 1
        return candidate
        # time comp: O(n) where n is the length of nums
        # space comp: O(1) two variables

        
        
        
        # d = {}
        # for i in range(0, len(nums)):
        #     if(d.get(nums[i]) == None):
        #         d[nums[i]] = 1
        #     else:
        #         d[nums[i]] = d.get(nums[i]) + 1
        #     if(d.get(nums[i]) > len(nums) / 2):
        #         return nums[i]

        # space comp: O(m) where m is the number of unique elements in nums
        # time comp: O(n) where n is the length of the array nums
        
