class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        max_len = 0
        palindrome = ""

        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > max_len:
                max_len = len(odd_palindrome)
                palindrome = odd_palindrome

            # Even length palindromes
            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > max_len:
                max_len = len(even_palindrome)
                palindrome = even_palindrome

        return palindrome

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]
