class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def divide(penalty):
            operations = 0
            for num in nums:
                operations += (num - 1) // penalty
                if operations > maxOperations:
                    return False
            return True

        left, right = 1 , max(nums)
        while left < right:
            mid = (left + right) // 2
            if divide(mid):
                right = mid
            else:
                left = mid + 1

        return left 