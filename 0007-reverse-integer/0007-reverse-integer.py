class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        
        return result if result <= 2**31-1 else 0
