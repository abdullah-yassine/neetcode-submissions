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
            
            
        
        actualFirstCnt = actualSecondCnt = 0
        for num in nums:
            if firstNum == num:
                actualFirstCnt += 1
            if secondNum == num:
                actualSecondCnt += 1
        
        result = []
        if actualFirstCnt > len(nums)//3:
            result.append(firstNum)
        if actualSecondCnt > len(nums)//3:
            result.append(secondNum)
        return result
            