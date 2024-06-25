class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        carry = 0
        i = len(num) - 1

        while k > 0 or i >= 0 or carry > 0:
            sum = carry
            
            if k > 0:
                sum += k % 10
                k //= 10
            
            if i >= 0:
                sum += num[i]
                i -= 1
            
            carry = sum // 10
            ans.append(sum % 10)

        ans.reverse()
        return ans        