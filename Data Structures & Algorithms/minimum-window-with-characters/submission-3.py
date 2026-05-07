class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter()
        left = right =0
        minimum_length = math.inf
        shortest_substring = ""
        while right < len(s):
            s_counter[s[right]] += 1
            right += 1
            while t_counter <= s_counter:
                if right - left < minimum_length:
                    minimum_length = right- left
                    shortest_substring = s[left:right]
                s_counter[s[left]] -= 1
                left += 1
            
            
        return shortest_substring