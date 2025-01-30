class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        return list(nums + nums)
    
        res = []
        for i in nums:
            res.append(i)

        for i in nums:
            res.append(i)
        
        return res

        res = [0]*(2*len(nums))

        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        return res

        