class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ('-','+'):
            sign = -1 if s[0]=='-' else 1
            s = s[1:]

        result = 0
        for i in s:
            if i.isdigit():
                result = result*10+int(i)
            else:
                break
        result *= sign
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result