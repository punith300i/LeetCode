class ListNode():
    def __init__(self, key, nxt=None):
        self.key = key
        self.nxt = nxt

class MyHashSet:

    def __init__(self):
        self.nodes = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        hash_val = key%len(self.nodes)
        cur = self.nodes[hash_val]
        while cur.nxt:
            if cur.nxt.key == key:
                return
            cur = cur.nxt
        cur.nxt = ListNode(key)
        

    def remove(self, key: int) -> None:
        hash_val = key%len(self.nodes)
        cur = self.nodes[hash_val]
        while cur.nxt:
            if cur.nxt.key == key:
                cur.nxt = cur.nxt.nxt
                return
            cur = cur.nxt

    def contains(self, key: int) -> bool:
        hash_val = key%len(self.nodes)
        cur = self.nodes[hash_val]
        while cur.nxt:
            if cur.nxt.key == key:
                return True
            cur = cur.nxt


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)