class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        curr_sum = 0
        max_sum = 0
        uniques = set()

        for end, val in enumerate(nums):
            curr_sum += val
            while val in uniques:
                uniques.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
                
            uniques.add(val)

            while end - start + 1 > k:
                uniques.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            
            if end - start + 1 == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum