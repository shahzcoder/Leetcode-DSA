class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0 
        for right in range(len(nums) - 1):
            if nums[right] == nums[right + 1] and nums[right] != 0 :
                nums[right] *= 2
                nums[right + 1] = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1

        return nums