class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        firstPtr = secondPtr = 0
        result = []
        nums1Cp = nums1.copy()
        nums2Cp = nums2.copy()
        while firstPtr < len(nums1Cp) - n and secondPtr < len(nums2Cp) :
            if nums1Cp[firstPtr] < nums2Cp[secondPtr]:
                nums1[firstPtr+secondPtr] = nums1Cp[firstPtr] 
                firstPtr += 1
            else:
                nums1[firstPtr+secondPtr] = nums2Cp[secondPtr]
                secondPtr += 1
            
        while firstPtr < len(nums1Cp) - n :
            nums1[firstPtr+secondPtr] = nums1Cp[firstPtr] 
            firstPtr += 1
            
        while secondPtr < len(nums2Cp) :
            nums1[firstPtr+secondPtr] = nums2Cp[secondPtr]
            secondPtr += 1
            
        for _ in range(n):
            result.append(0)
       
        
