class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        chars = [0] * 26
        max_freq = 0
        result = 0
        while right < len(s):
            idx = ord(s[right]) - ord('A')
            chars[idx] += 1
            max_freq = max(max_freq, chars[idx])
            right += 1
            window_size = right - left
            while window_size - max_freq > k:
                idx = ord(s[left]) - ord('A')
                chars[idx] -= 1
                left += 1
                window_size = right - left
            result = max(result, window_size)
        return result