class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0 

        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                X += 1
            else:
                X -= 1
            
        return X