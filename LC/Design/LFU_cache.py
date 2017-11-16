'''
460
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class Node():
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self._prev = None
        self._next = None


class NodeList():

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

    #add To head
    def addNode(self, node):

        if not self.head._next and not self.tail._prev:
            self.head._next = node
            node._prev = self.head
            self.tail._prev = node
            node._next = self.tail
        else:
            node._next = self.head._next
            self.head._next._prev = node
            self.head._next = node

    #remove from tail
    def removeLastNode(self):
        if self.tail._next:
            self.tail._prev._next = None
            self.tail = self.tail._prev

    #remove a node
    def removeNode(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev



class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_info = {}
        self.count_list = NodeList()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_info:
            node = self.key_info[key]

            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.key_info.has_key(key):
            value, count, index = self.key_info[key]
            del(self.count_list[count][index])
            self.count_list[count+1].append(key)
            self.key_info[key][1] += 1
            self.key_info[key][value] = value
        else:
            count = 1
            node = Node(value, count)
            #if count in self.count_list.count_map:
        bucket_head = self.count_list.addBucket(count, node)













        # Your LFUCache object will be instantiated and called as such:
obj = LFUCache(3)
print obj.get(1)
obj.put(1,1)
obj.put(1,1)
obj.put(2,1)
obj.put(3,2)

