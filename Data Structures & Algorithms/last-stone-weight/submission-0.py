class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        currLen = len(stones)

        while currLen > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            currLen -= 2
            if x != y:
                heapq.heappush(stones, -abs(x-y))
                currLen += 1

        return -stones[0] if currLen > 0 else 0

        