class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort()
        left, right = 0, len(people) - 1
        while left <= right:
            if people[right] + people[left] <= limit:
                result += 1
                left += 1
                right -= 1
            else:
                right -= 1
                result += 1
        return result
