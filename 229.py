class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3

        res = []
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq :
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for num,val in freq.items():
            if val > n:
                res.append(num)
        
        return res