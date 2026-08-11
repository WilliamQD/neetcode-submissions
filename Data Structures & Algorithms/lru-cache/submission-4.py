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
    
    # HELPER 1: Pluck a node out of the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # HELPER 2: Insert a node right before the MRU dummy (self.right)
    def insert(self, node):
        prev_node = self.right.prev
        
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node
    
    def get(self, key: int) -> int:
        
        if key in self.cache:
            # link neighbors
            node = self.cache[key]
            self.remove(node)

            # make node MRU
            self.insert(node)

            # return the val
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # cleaner way
        # # If full, kick out the LRU first
        # if len(self.cache) == self.capacity:
        #     node_to_remove = self.left.next
        #     del self.cache[node_to_remove.key]
        #     self.remove(node_to_remove)

        # # Whether it was full or not, we always add the new node here!
        # node = Node(key, value)
        # self.insert(node)
        # self.cache[key] = node

        
        # update if key exists
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            node.val = value
            return


        # else insert
        if len(self.cache) == self.capacity:
            # remove last node
            node_to_remove = self.left.next
            del self.cache[node_to_remove.key]

            self.remove(node_to_remove)

            # add new node to MRU
            node = Node(key, value)
            self.insert(node)

            # add it to hasmap
            self.cache[key] = node
        
        else:
            # make the node the MRU
            node = Node(key, value)
            self.insert(node)

            # add it to hasmap
            self.cache[key] = node



