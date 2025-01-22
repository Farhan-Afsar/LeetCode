class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0]*len(nums)
        for i in range(len(nums)):
            temp[(i+k)%len(nums)] = nums[i]
        
        nums[:] = temp

# i+k = index+No. of index to move = new address to move % len to 
# be inside array index