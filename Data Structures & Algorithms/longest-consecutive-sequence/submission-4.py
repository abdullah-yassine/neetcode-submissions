class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table = set(nums)
        longest_sequence = 0
        for num in hash_table:
            if num - 1 in hash_table:
                continue
            else:
                cnt = 1
                while num + 1 in hash_table:
                    cnt += 1
                    num += 1
                longest_sequence = max(longest_sequence, cnt)
        return longest_sequence
            
            
            
            
