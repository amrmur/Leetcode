class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply every number into product except zero
        # then divide product by each number
        # if 0 was encountered once, 0 number is the product, that's it
        # if 0 was encountered more than once, everything is zero

        zeroIndex = -1
        product = 1
        length = len(nums)
        ret = [0] * length

        for i in range(0, length):
            if(nums[i] == 0): 
                if(zeroIndex != -1):
                    return ret
                zeroIndex = i
            else: product *= nums[i]

        if(zeroIndex != -1):
            ret[zeroIndex] = product
            return ret
        
        for i in range(0, length):
            ret[i] = product // nums[i]
        return ret
        
