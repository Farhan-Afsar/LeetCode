class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = 0
        sum = (n * (n + 1)) / 2

        for i in range(n):
            arr_sum+=nums[i]
        
        return int(sum-arr_sum)
        