class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False

        target_sum = sum_arr // 3
        curr_sum = 0
        partition = 0

        for num in arr:
            curr_sum += num

            if curr_sum == target_sum:
                partition += 1
                curr_sum = 0
            
            if partition == 3:
                return True
        
        return False
