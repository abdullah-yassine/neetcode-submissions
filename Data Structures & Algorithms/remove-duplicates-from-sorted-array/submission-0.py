class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left =0 # last unique
        right =1 # looks for something new
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1