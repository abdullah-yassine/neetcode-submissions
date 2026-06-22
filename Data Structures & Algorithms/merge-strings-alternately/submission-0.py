class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        firstPtr = secondPtr = 0
        turn = True
        result = ""
        while firstPtr < len(word1) and secondPtr < len(word2):
            if turn:
                result += word1[firstPtr]
                turn = False
                firstPtr += 1
            else:
                result += word2[secondPtr]
                turn = True
                secondPtr += 1
        while firstPtr < len(word1):
            result += word1[firstPtr]
            firstPtr += 1
        while secondPtr < len(word2):
            result += word2[secondPtr]
            secondPtr += 1
        return result
        