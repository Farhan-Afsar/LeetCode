class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        right_sum = 0
        max_sum = 0

        for i in range(k):
            left_sum += cardPoints[i]
        
        max_sum = left_sum
        right_index = len(cardPoints)-1

        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            right_index -= 1

            max_sum = max(max_sum,left_sum + right_sum)

        return max_sum