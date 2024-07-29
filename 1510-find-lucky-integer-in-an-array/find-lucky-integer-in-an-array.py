class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [-1]
        new_arr = set(arr)

        for i in new_arr:
            if arr.count(i) == i:
                count.append(i)
        return max(count)