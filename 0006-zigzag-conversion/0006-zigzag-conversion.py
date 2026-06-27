class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or len(s)<=numRows:
            return s
        
        result = ['']*numRows
        index = 0
        step_val = 1

        for i in s:
            result[index] += i
            if index==(numRows-1):
                step_val = -1
            elif index==0:
                step_val = 1
            index += step_val

        return ''.join(result)