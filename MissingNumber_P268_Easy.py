class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_1 = 0
        sum_2 = 0
        for i in range(len(nums)):
	        sum_1 = sum_1 + nums[i]
        for i in range(len(nums)+1):
	        sum_2 = sum_2 +i
        return sum_2 - sum_1
