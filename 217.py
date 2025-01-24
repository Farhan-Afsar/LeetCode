class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True                #O(n)
            a.add(i)
        return False

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):     #O(n^2)
                if nums[i] == nums[j]:
                    return True
        return False

        nums.sort()

        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:      #O(nlogn)
                return True
        return False
