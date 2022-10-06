from collections import defaultdict
class TimeMap:
    rec = {}
    def __init__(self):
        self.rec = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.rec[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        ts = timestamp
        while ts not in self.rec or key not in self.rec[ts]:
            if ts == 0: break
            ts-=1
        return "" if ts==0 else self.rec[ts][key]
