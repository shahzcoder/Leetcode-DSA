class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_count = {}
        good_pairs = 0

        for i in range(n):
            diff = nums[i] - i
            if diff in diff_count:
                good_pairs += diff_count[diff]
                diff_count[diff] += 1
            else:
                diff_count[diff] = 1
            
        total_pairs = n * (n - 1) // 2
        bad_pairs = total_pairs - good_pairs

        return bad_pairs
