class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # problem: given an array of integers, remove the duplicate elements inplace and return
        # the number of unique elements
        
        # iterate through the array
        # use a pointer to track the unique elements
        ptr = 1
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[ptr] = nums[i]
                ptr = ptr + 1
        return ptr
        # TIME COMPLEXITY: O(n) where n is the length of the array
        # SPACE COMPLEXITY: O(1) just two pointers
        

        # ATTEMPT 1:
        # use a hashset to store if a number has occured
        # iterate through the nums array starting from the front
        # use a seperate pointer to rewrite the array with just the unique elements
        # s = set()
        # ptr = 0
        # for i in range(0,len(nums)):
        #     if(nums[i] not in s):
        #         s.add(nums[i])
        #         nums[ptr] = nums[i]
        #         ptr = ptr + 1
        # return ptr

        # TIME COMPLEXITY: O(n) where n is the length of the array
        # SPACE COMPLEXITY: O(m) where m is the number of unique elements in nums
