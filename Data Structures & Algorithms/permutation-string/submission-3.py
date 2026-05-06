class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[0:len(s1)])
        if s1_counter == s2_counter:
            return True
        while right < len(s2) - 1:
            s2_counter[s2[left]] -= 1
            left += 1
            right += 1
            s2_counter[s2[right]] += 1
            if s1_counter == s2_counter:
                print(s1_counter, s2_counter)
                return True
        return False
        
        
