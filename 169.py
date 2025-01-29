class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2

        freq={}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] = freq.get(nums[i],0)+1
            else:
                freq[nums[i]] = 1

        for num,val in freq.items():
            if val > n:
                return num