class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # So this solution checks in the beginning if there is a possible circular route
        # then it goes through the gas/costs and when it finds an impossible route, it
        # tries the next station as the start point
        if(sum(gas) < sum(cost)):
            return -1

        total = 0
        start = 0
        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            if(total < 0):
                total = 0
                start = i + 1
        return start
        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
        
        # # ATTEMPT 1
        # for i in range(0, len(gas)):
        #     start = i
        #     total = 0
        #     for j in range(start, start + len(gas)):
        #         total += gas[j%len(cost)]
        #         total -= cost[j%len(gas)]
        #         if(total < 0): break
        #     if(total >= 0): return start
        # return -1
