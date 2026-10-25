class TimeMap:

    def __init__(self):
        self.customMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.customMap:
            self.customMap[key] = []
        self.customMap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.customMap:
            return ""
        res = ""
        l, r = 0, len(self.customMap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            v, t = self.customMap[key][m]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = m - 1
            else:
                res = v
                l = m + 1
        return res


        
        
