class MyHashSet:

    def __init__(self):
        self.mem = [False] * 1_000_000

    def add(self, key: int) -> None:
        self.mem[key] = True

    def remove(self, key: int) -> None:
        self.mem[key] = False

    def contains(self, key: int) -> bool:
        return self.mem[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)