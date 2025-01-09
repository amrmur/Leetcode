class Solution:
    def hIndex(self, citations: List[int]) -> int:
        num = len(citations)
        buckets = [0] * (num + 1)

        for i in range(num):
            recieved = citations[i]
            if(recieved > num):
                recieved = num
            buckets[recieved] += 1
        
        count = 0
        for j in range(num, -1, -1):
            count += buckets[j]
            if(count >= j):
                return j

        # SPACE/TIME COMPLEXITY: O(n) BUCKETS SOLUTION
        # 1 1 0 1 0 2
        # 0 1 2 3 4 5

        # 0 2 0 1
        # 0 1 2 3



        # # ATTEMPT 1
        # # reverse sort the array
        # # 6 5 3 1 0
        # # citations[i] >= (i + 1) then return i + 1

        # citations.sort(reverse = True)
        # for i in range(len(citations) - 1, -1, -1):
        #     if(citations[i] >= i + 1):
        #         return i + 1
        # return 0

        # # SPACE COMPLEXITY: O(1)
        # # TIME COMPLEXITY: O(nlog(n))
