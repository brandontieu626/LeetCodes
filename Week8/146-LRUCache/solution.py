class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left 
    
    def remove(self,node):
        prev=node.prev
        prev.next=node.next
        node.next.prev=prev
    
    def insert(self,node):
        save=self.right.prev
        save.next=node
        node.prev=save
        node.next=self.right
        self.right.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])
        else:
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])

            if len(self.cache)>self.capacity:
                self.cache.pop(self.left.next.key)
                self.remove(self.left.next)

        