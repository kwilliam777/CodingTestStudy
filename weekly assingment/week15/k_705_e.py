class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        if key not in self.stack: self.stack.append(key)

    def remove(self, key: int) -> None:
        if key in self.stack: self.stack.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.stack else False
