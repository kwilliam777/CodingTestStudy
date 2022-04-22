class MyHashMap:

    def __init__(self):
        self.my = dict()

    def put(self, key: int, value: int) -> None:    
        self.my[key] = value

    def get(self, key: int) -> int:
        if key in self.my: return self.my[key]
        else: return -1

    def remove(self, key: int) -> None:
        if key in self.my:
            del self.my[key]
