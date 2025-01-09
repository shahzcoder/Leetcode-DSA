class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT , stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t , i])
        return res

















        # n = len(temperatures)  # brute force
        # answer = [0] * n
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
            
        # return answer