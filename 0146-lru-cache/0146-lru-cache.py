class Node:
    def __init__(self,key,val) -> None:
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
        self.map={}


    def get(self, key: int) -> int:


        if key not in self.map:
            return -1
        
        node=self.map[key]
        nodel=node.prev
        noder=node.next
        nodel.next=noder
        noder.prev=nodel

        nodel=self.right.prev
        nodel.next=node
        node.prev=nodel
        node.next=self.right
        self.right.prev=node

        return node.val      

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            node = self.map[key]
            nodel=node.prev
            noder=node.next
            nodel.next=noder
            noder.prev=nodel
            del self.map[key]
            
        elif len(self.map)==self.cap:     

            node=self.left.next
            self.left.next=node.next
            node.next.prev=self.left
            keyr=node.key
            del self.map[keyr]

        node = Node(key,value)
        
        node.next=self.right
        node.prev=self.right.prev
        self.right.prev.next=node
        self.right.prev=node
        self.map[key]=node
        l=self.left
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)