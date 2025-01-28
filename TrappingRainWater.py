class Solution:
    def trap(self, height: List[int]) -> int:  
        # we store a pointer and max seen by left and right
        L = 0
        R = len(height) - 1
        LM = height[L]
        RM = height[R]
        water = 0
        while(L != R):
            # look at the side with the lower max (you know that much water can be supported)
            # then we move the pointer, record the new max, and add the water
            if(RM <= LM):
                R -= 1
                curHeight = height[R]
                RM = max(RM, curHeight)
                if(RM - curHeight > 0):
                    water += RM - curHeight
            if(LM < RM):
                L += 1
                curHeight = height[L]
                LM = max(LM, curHeight)
                if(LM - curHeight > 0):
                    water += LM - curHeight
        return water
