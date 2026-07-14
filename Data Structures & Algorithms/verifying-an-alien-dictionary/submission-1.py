class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alph = {char : idx for idx, char in enumerate(order)}
        for i in range(1, len(words)):
            first_word = words[i-1]
            second_word = words[i]
            same = False
            for i in range(min(len(first_word), len(second_word))):
                if alph[first_word[i]] > alph[second_word[i]]:
                    return False
                if alph[first_word[i]] < alph[second_word[i]]:
                    same = True
                    break
            if not same and len(first_word) > len(second_word):
                return False
                
        return True