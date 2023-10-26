forb = 0
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        limit = 2000 + a + b
        visited = set(forbidden)
        queue = deque([(0, True)])
        hops = 0
        while queue:
            l = len(queue)
            while l>0:
                l -= 1
                pos, isForward = queue.popleft()
                if pos == x :
                    return hops
                if pos in visited:
                    continue
                visited.add(pos)
                if isForward == True:
                    if pos - b >= 0:
                        queue.append(((pos-b), False))
                if pos + a <= limit:
                    queue.append(((pos+a), True))
            hops += 1
                
        return -1
            