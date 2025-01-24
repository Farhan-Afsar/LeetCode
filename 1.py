class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i,num in enumerate(nums):
            n = target - num

            if n in my_dict:                     #O(n)
                return [my_dict[n],i]
        
            my_dict[num] = i

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):                  #O(n^2)
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []