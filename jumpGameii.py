class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far+1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        return jumps

        # store your current jump length with count steps
        # if you can't reach the goal in count steps, max is now jump and take a step
        # count = jump = max = 0

        # for i in range(0, len(nums) - 1):
        #     jump = jump - 1
        #     max = max - 1
        #     if(nums[i] > max):
        #         max = nums[i]
        #     if(jump <= 0):
        #         jump = max
        #         count = count + 1
        #         max = 0
        # return count
        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
