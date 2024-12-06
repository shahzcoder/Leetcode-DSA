class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum = 0
        count = 0
        for num in range(1, n+1):
            if num not in banned and sum + num <= maxSum:
                sum += num
                count += 1
            elif sum + num > maxSum:
                break
        
        return count