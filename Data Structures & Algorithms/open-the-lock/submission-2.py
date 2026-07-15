class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def new_combo(combo, new_num):
            combo_list = list(combo)
            combo_list[i] = str(new_num)
            new_combo = "".join(combo_list)
            if new_combo not in visited:
                q.append((new_combo, moves + 1))
                visited.add(new_combo)
        q = deque()
        q.append(("0000", 0))
        turns = 0
        visited = set()
        deadends = set(deadends)
        while q:
            combo, moves = q.popleft()
            if combo == target:
                return moves
            if combo in deadends:
                continue
            for i in range(len(combo)):
                new_combo(combo, (int(combo[i]) + 1) % 10)
                new_combo(combo, (int(combo[i]) - 1) % 10)
        return -1
        
