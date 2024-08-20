class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()  # Sort the original array
        n = len(nums)
        i = 0
        j = 0
        count = 0
        while j < n:
            if nums[j] > nums[i]:
                count += 1
                i += 1
            j += 1

        return count