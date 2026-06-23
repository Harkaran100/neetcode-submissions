class TimeMap:

    def __init__(self): # {key : list[val, timestamp]}
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        left = 0
        right = len(values) -1
        while right >= left:
            mid = (left + right) // 2
            if values[mid][1] <=timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid -1
        
        return res

        # hashmap
        # key is key
        # value is list of value
        # need to go through list of values to find
        
