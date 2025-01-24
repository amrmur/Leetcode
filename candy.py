class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        tc = n # give each child the minimum of one candy
        i = 1
        while(i < n):
            if(ratings[i] == ratings[i-1]):
                i = i + 1 # no need to give candy they are good with the one they got
            
            peak = 0
            while(i < n and ratings[i] > ratings[i-1]):
                peak = peak + 1
                tc = tc + peak # pretty much one more then the previous
                i = i + 1
            
            valley = 0
            while(i < n and ratings[i] < ratings[i-1]):
                valley = valley + 1
                tc = tc + valley # this candy given to the previous "valley" children
                i = i + 1
            
            tc = tc - min(peak, valley) 
            # we overcompensate with two edges when we only need 
            # one due to having a base level of 1 candy
        return tc
    # time complexity: O(n)
    # space complexity: O(1)
            
