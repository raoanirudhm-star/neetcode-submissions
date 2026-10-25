class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res = ""
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            m = (l + r) // 2
            v, t = self.store[key][m]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = m - 1
            else:
                res = v
                l = m + 1
        return res
