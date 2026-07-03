class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001
        for num, frm, to in trips:      # phase 1: record ALL events
            timeline[frm] += num
            timeline[to]  -= num

        current = 0
        for delta in timeline:          # phase 2: sweep left to right by km
            current += delta
            if current > capacity:
                return False
        return True