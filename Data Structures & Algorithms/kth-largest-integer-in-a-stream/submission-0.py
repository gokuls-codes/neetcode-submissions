class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mem = nums
        heapq.heapify(self.mem)
        self.k = k
        self.currLen = len(nums)
        while self.currLen > k:
            heapq.heappop(self.mem)
            self.currLen -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.mem, val)
        self.currLen += 1
        if self.currLen > self.k:
            heapq.heappop(self.mem)
        
        return self.mem[0]

