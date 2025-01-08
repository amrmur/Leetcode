class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if(i + nums[i] >= goal):
                goal = i

        return True if goal == 0 else False
        # same time and space complexity but going backwards

        # # keep a jump counter
        # jump = nums[0]
        # for i in range(1, len(nums) - 1):
        #     # if you can't jump, you lose
        #     if(jump == 0):
        #         return False
        #     # keep track of the highest jump, either current jump amount, or new element
        #     jump = jump - 1
        #     if(nums[i] > jump):
        #         jump = nums[i]

        # # if you don't have to jump or you can jump to the last point, you win
        # if(len(nums) == 1 or jump > 0):
        #     return True
        # return False
        # # TIME COMPLEXITY: O(n)
        # # SPACE COMPLEXITY: O(1)

        # # recursive attempt, got time limit exceeded
        # visited = [False] * (len(nums) - 1)
        # def h(visited, nums, current):
        #     if(current >= len(nums) - 1):
        #         return True
        #     if(visited[current] == True):
        #         return False
        #     visited[current] = True
        #     found = False
        #     for i in range(current + 1, current + nums[current] + 1):
        #         found = found or h(visited, nums, i)
        #     return found
        # return h(visited, nums, 0)        
