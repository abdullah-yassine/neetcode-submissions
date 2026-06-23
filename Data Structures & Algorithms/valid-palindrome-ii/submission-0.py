class Solution:
    def validPalindrome(self, s: str) -> bool:
        # call palindrome helper function on the two decisions, if either is correct
        # move on
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left + 1, right) or isPalindrome(s, left ,right - 1)
            left += 1
            right -= 1
        return True