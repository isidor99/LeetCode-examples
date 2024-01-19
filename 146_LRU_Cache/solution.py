class LRUCache(object):
    
    class Node(object):
        def __init__(self, key, value, next, prev):
            self.key = key
            self.value = value
            self.next = next
            self.prev = prev
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
    
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        ret = -1
        
        if key in self.cache:
            # get value
            ret = self.cache[key].value
            
            # move node to from
            self.moveToFront(self.cache[key])

        return ret
    
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            # key already exists, update its value
            node = self.cache[key]
            node.value = value
            
            # move node to front of the list
            self.moveToFront(node)
            
            # return
            return None
            
        elif len(self.cache) == self.capacity:
            # remove node from list
            k = self.listBackRemove()
            
            self.cache.pop(k)
        
        # insert node to list
        node = self.listFrontInsert(key, value)
        
        # insert key into hash map
        self.cache[key] = node

        # return
        return None


    def moveToFront(self, node):
        """
        :type node: Node
        """
            
        if self.head == node:
            return
        
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        else:      
            # get pointers to next and prev
            p = node.prev
            n = node.next
                
            n.prev = p
            p.next = n
                
            # place this node at the beginning of the list
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node


    def listFrontInsert(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: Node
        """
        
        node = self.Node(key, value, None, None)
        
        if self.head == None and self.tail == None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        
        return node


    def listBackRemove(self):
        """
        :rtype: int
        """
        
        ret = -1
        
        if self.head == self.tail:
            ret = self.head.key
            self.head = self.tail = None
        else:
            ret = self.tail.key
            self.tail = self.tail.prev
            self.tail.next = None

        return ret
