class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse() # o(n)
        nums[0:k] = nums[0:k][::-1] # o(k)
        nums[k:] = nums[k:][::-1] # o(n - k)

                