class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = 0
        r = len(nums) - 1
        min_average = float('inf')
        
        while l < r:
            average = (nums[l] + nums[r]) / 2
            min_average = min(average, min_average)
            l += 1
            r -= 1

        return min_average

            

