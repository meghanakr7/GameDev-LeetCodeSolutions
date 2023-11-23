class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -1 * gifts[i]
        heapq.heapify(gifts)
        for i in range(k):
            val = -1 * heapq.heappop(gifts)
            heapq.heappush(gifts, -1 * int(val**0.5))
            heapq.heapify(gifts)
        for i in range(len(gifts)):
            if gifts[i] < 0:
                gifts[i] = -1 * gifts[i]
        # print("At last gifts are ",gifts)
        # print("Sum is ",sum(gifts))
        return sum(gifts)

        