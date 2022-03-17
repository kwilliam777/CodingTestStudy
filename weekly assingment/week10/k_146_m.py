class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.least = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.items:
            if key in self.least:
                self.least.remove(key)
            self.least.append(key)
            return self.items[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.items and len(self.least) >= self.cap:
            l=self.least.pop(0)
            self.items.pop(l)
        
        self.items[key] = value
        if key in self.least:
            self.least.remove(key)
        self.least.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
