class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # create a of sorted unique elements
        sorted_unique = sorted(set(arr))

        # create a rank map(element: rank)
        rank_map = {}
        rank = 1
        for num in sorted_unique:
            rank_map[num] = rank
            rank += 1
        
        # replace element in the original array with their rank

        result = []
        for num in arr:
            result.append(rank_map[num])

        return result

