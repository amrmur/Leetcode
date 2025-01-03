class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove duplicates after appearing twice
        
        # scan through array from front
        # use ptr to keep track of unique elements appearing twice
        # add number if doesnt equal second previous element 
        # if it does that mean element appears twice already
        n = len(nums)
        if(n < 2):
            return n
        ptr = 2
        for i in range(2, n):
            if(nums[i] != nums[ptr-2]):
                nums[ptr] = nums[i]
                ptr = ptr + 1
        return ptr
        # space comp. O(1) just pointers
        # time comp. O(n) iterate through array




        # handle base cases (first two integers)
        # iterate from start of nums and add number if not equal to one of last two nums
        # ptr = 2
        # dup = nums.copy()
        # for i in range(2, len(nums)):
        #     if(nums[i] != dup[i-1] or nums[i] != dup[i-2]):
        #         nums[ptr] = nums[i]
        #         ptr = ptr + 1
        #     print(ptr)
        # return ptr
        # space comp. O(n), time comp. O(n)
        
