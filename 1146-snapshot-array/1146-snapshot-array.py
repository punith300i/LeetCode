class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_arraymap = {}
        
        for i in range(length):
            self.snap_arraymap[i] = [(0,0)]

    def set(self, index: int, val: int) -> None:
        self.snap_arraymap[index].append((self.snap_id,val))

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        
        index_arraymap = self.snap_arraymap[index]
        low = 0
        high = len(index_arraymap)-1
        
        result = 0
        while low<=high:
            
            mid = low + (high-low)//2
            
            if index_arraymap[mid][0]<=snap_id:
                low = mid+1
                result = index_arraymap[mid][1]
            else:
                high = mid-1
        
        return result


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)