class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstCount = secondCount = 0
        firstNum = secondNum = None
        for num in nums:
            if firstCount == 0 and secondNum != num:
                firstNum = num
            elif secondCount == 0 and firstNum != num:
                secondNum = num
            
            if num != secondNum:
                firstCount += 1 if firstNum == num else -1
            if num != firstNum:
                secondCount += 1 if secondNum == num else -1
            
            
        
        firstCount=secondCount =0
        for num in nums:
            if firstNum == num:
                firstCount += 1
            if secondNum == num:
                secondCount += 1
        
        result = []
        if firstCount > len(nums)//3:
            result.append(firstNum)
        if secondCount > len(nums)//3:
            result.append(secondNum)
        return result
            