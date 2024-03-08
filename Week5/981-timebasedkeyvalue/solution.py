class TimeMap:

    def __init__(self):
       self.map={} 

    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.map:
            self.map[key]=[]
        self.map[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
         
        times=self.map[key]
        start=0
        end=len(times)-1
        res=""
        while start<=end:
            mid=start+(end-start)//2

            stamp=times[mid]
            if stamp[1]<=timestamp:
                start=mid+1
                res=stamp[0]
            else:
                end=mid-1
        
        return res
