class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i,num in enumerate(nums):
            n = target - num

            if n in my_dict:
                return [my_dict[n],i]
        
            my_dict[num] = i
        