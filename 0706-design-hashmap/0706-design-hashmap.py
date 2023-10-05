class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.keylist = [Node(-1,1) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hash_val = key%10**4
        cur = self.keylist[hash_val]
        flag = False
        while cur.next:
            if key==cur.next.key:
                cur.next.value = value
                flag=True
                break
            cur = cur.next
        if not flag:
            cur.next = Node(key,value)

    def get(self, key: int) -> int:
        hash_val = key%10**4
        cur = self.keylist[hash_val]
        while cur.next:
            if key == cur.next.key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hash_val = key%10**4
        cur = self.keylist[hash_val]
        while cur.next:
            if key == cur.next.key:
                cur.next = cur.next.next
                break
            cur = cur.next
        
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)