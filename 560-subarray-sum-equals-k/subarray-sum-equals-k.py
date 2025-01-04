class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        hashmap = {0:1}
        for num in nums:
            current_sum += num

            if current_sum - k in hashmap:
                count += hashmap[current_sum - k]
            
            hashmap[current_sum] = hashmap.get(current_sum,0) + 1
        
        return count
            