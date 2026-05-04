class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        mem = Counter(nums)
        freq = [[] for i in range(n + 1)]
        
        for num in mem:
            freq[mem[num]].append(num)

        res = []
        curr = 0
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                curr += 1
                if curr == k:
                    return res