class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        mx_len = 0
        str_doc = {}
        for i, val in enumerate(s):
            if val in str_doc:
                left = max(left, str_doc[val] + 1)
            str_doc[val] = i
            mx_len = max(mx_len, i-left+1)
        return mx_len
