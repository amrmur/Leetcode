class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse whole array
        # then reverse 0,k and k,length sections
        k %= len(nums)

        def reverse(left,right):
            while(left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        # Time comp: O(n)
        # Space comp.: O(1)

        # # ATTEMPT 2
        # # same time and space complexity as attempt 1
        # k = k % len(nums)
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]


        # # ATTEMPT 1
        # # get remainder of k
        # # make new array
        # # go through nums and make [(index + k) % n] element equal to index element

        # n = len(nums)
        # k = k % n

        # ret = [0] * n

        # for i in range(0, n):
        #     ret[(i+k)%n] = nums[i]

        # for i in range(0, n):
        #     nums[i] = ret[i]

        # # SPACE COMP. : O(n)
        # # TIME COMP.: O(n)
