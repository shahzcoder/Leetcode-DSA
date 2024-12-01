class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        for num in nums:
            while original in nums:
                original *= 2
        
        return original
            


