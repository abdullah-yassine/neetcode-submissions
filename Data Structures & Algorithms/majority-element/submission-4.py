class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_element = len(nums) // 2
        count = defaultdict(int)
        maj_num = maj_cnt = 0
        for num in nums:
            count[num] += 1
            if count[num] > maj_element:
                maj_num= num
                
        return maj_num