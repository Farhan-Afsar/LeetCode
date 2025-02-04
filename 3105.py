class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        in_count,in_max = 1,1
        d_count ,d_max= 1,1

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                in_count += 1
                d_count = 1
            elif nums[i] < nums[i-1]:
                d_count += 1
                in_count = 1
            else:
                in_count = 1
                d_count = 1
            in_max = max(in_max,in_count)
            d_max = max(d_max,d_count)
        
        return max(in_max,d_max)