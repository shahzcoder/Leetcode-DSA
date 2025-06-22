class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [] * len(nums)
        for num in nums:
            result.append(num**2)

        return sorted(result)
