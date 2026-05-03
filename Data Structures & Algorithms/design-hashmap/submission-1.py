class MyHashMap:

    def __init__(self):
        self.mem = [None] * 1_000_001

    def put(self, key: int, value: int) -> None:
        if key >= 1_000_001: return
        self.mem[key] = value

    def get(self, key: int) -> int:
        if self.mem[key] is not None: return self.mem[key]
        return -1

    def remove(self, key: int) -> None:
        self.mem[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)