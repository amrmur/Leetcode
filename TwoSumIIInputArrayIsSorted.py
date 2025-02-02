class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            estimate = numbers[left] + numbers[right]
            if(estimate == target):
                return ([left + 1, right + 1])
            elif(estimate > target):
                right -= 1
            else:
                left += 1
