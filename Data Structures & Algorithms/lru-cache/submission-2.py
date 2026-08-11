def makeMRU(node, right):
    node.next = right
    node.prev = right.prev
    node.prev.next = node
    right.prev = node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # Create your dummy head and tail
        self.left = Node(-1, 0)  # LRU pointer
        self.right = Node(-1, 0) # MRU pointer
        
        # Connect them to each other to start!
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key: int) -> int:
        
        if key in self.cache:
            # link neighbors
            node = self.cache[key]
            node.next.prev = node.prev
            node.prev.next = node.next

            # make node MRU
            makeMRU(node, self.right)

            # return the val
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update if key exists
        if key in self.cache:
            node = self.cache[key]
            node.next.prev = node.prev
            node.prev.next = node.next

            makeMRU(node, self.right)
            
            node.val = value
            return


        # else insert
        if len(self.cache) == self.capacity:
            # remove last node
            node_to_remove = self.left.next
            del self.cache[node_to_remove.key]

            node_to_remove.next.prev = node_to_remove.prev
            node_to_remove.prev.next = node_to_remove.next #this should be same as self.left.next

            # add new node to MRU
            node = Node(key, value)
            makeMRU(node, self.right)

            # add it to hasmap
            self.cache[key] = node
        
        else:
            # make the node the MRU
            node = Node(key, value)
            makeMRU(node, self.right)

            # if first node, connect it to LRU too
            if len(self.cache) == 0:
                self.left.next = node

            # add it to hasmap
            self.cache[key] = node



