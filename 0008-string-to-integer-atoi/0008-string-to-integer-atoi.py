class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        res = 0
        for c in s:
            if c.isdigit():
                res = res * 10 + int(c)
            else:
                break
        
        res *= sign
        
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
