class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        while len(stones) and len(stones) != 1 and len(stones) != 0:
            heapq.heapify(stones)
            first = -1 * heapq.heappop(stones)
            sec = -1 * heapq.heappop(stones)
            print("first and sec are ",first, sec)
            if first == sec:
                continue
            if first != sec:
                if first > sec:
                    temp = sec
                    sec = first
                    first = temp
                print("first and sec are ",first, sec)
                heapq.heappush(stones, -1 * abs(first-sec))
        # print("stones are ",stones)
        for i in range(len(stones)):
            if stones[i] < 0:
                stones[i] = -1 * stones[i]
        print("Final stones are ",stones)
        if len(stones):
            return stones[0]
        return 0



        