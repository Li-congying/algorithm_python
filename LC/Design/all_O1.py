'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''


class ListNode(object):
    def __init__(self, key, val):
        self._prev = None
        self._next = None
        self.val = val
        self.key = key

class CountListNode(object):
    def __init__(self):
        self._next = None
        self.next_cl = None
        self.prev_cl = None

class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}
        self.count_table = {}
        self.head = CountListNode()
        self.tail = CountListNode()


    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # update key node
        if key not in self.hash_table:
            self.hash_table[key] = ListNode(key, 1)
        else:
            self.hash_table[key].val += 1
        node = self.hash_table[key]
        val = node.val

        #print 'inc', key, val
        # delete node from original List
        if node._prev:
            node._prev._next = node._next
        if node._next:
            node._next._prev = node._prev

        # insert node to new List
        if val not in self.count_table:
            cl_node = CountListNode()
            cl_node._next = node
            node._prev = cl_node
            node._next = None
            if not self.head.next_cl and not self.tail.prev_cl:
                self.head.next_cl = cl_node
                cl_node.prev_cl = self.head
                self.tail.prev_cl = cl_node
                cl_node.next_cl = self.tail
            else:
                if val == 1:
                    next_cl_node = self.tail
                else:
                    next_cl_node = self.count_table[val-1]
                cl_node.next_cl = next_cl_node
                cl_node.prev_cl = next_cl_node.prev_cl
                next_cl_node.prev_cl.next_cl = cl_node
                next_cl_node.prev_cl = cl_node

            #print key, val, cl_node.prev_cl == self.head
            self.count_table[val] = cl_node
        else:
            node._next = self.count_table[val]._next
            node._prev = self.count_table[val]
            self.count_table[val]._next._prev = node
            self.count_table[val]._next = node

        print 'inc', key, val
        if val - 1 in self.count_table and not self.count_table[val - 1]._next:
            #print key, val, val-1
            del_node = self.count_table[val-1]
            #print del_node.prev_cl._next
            del_node.prev_cl.next_cl = del_node.next_cl
            del_node.next_cl.prev_cl = del_node.prev_cl
            del (self.count_table[val - 1])

        for v in self.count_table:
            print 'v:',v,
            node = self.count_table[v]._next
            while node:
                print node.key, node.val
                node = node._next

        if self.head.next_cl:
            print 'head',self.head.next_cl._next.key, self.head.next_cl._next.val
        print '\n'


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.hash_table:
            return False
        self.hash_table[key].val -= 1
        node = self.hash_table[key]
        val = node.val

        if node._prev:
            node._prev._next = node._next
        if node._next:
            node._next._prev = node._prev

        if val > 0:
            if val not in self.count_table:
                # insert node to new List
                cl_node = CountListNode()
                cl_node._next = node
                node._prev = cl_node
                node._next = None
                prev_cl_node = self.count_table[val+1]

                cl_node.next_cl = prev_cl_node.next_cl
                cl_node.prev_cl = prev_cl_node.prev_cl
                prev_cl_node.next_cl = cl_node
                cl_node.next_cl.prev_cl = cl_node
                self.count_table[val] = cl_node
            else:
                node._next = self.count_table[val]._next
                node._prev = self.count_table[val]
                self.count_table[val]._next._prev = node
                self.count_table[val]._next = node
        else:
            del(self.hash_table[key])

        if val + 1 in self.count_table and not self.count_table[val + 1]._next:
            del_node = self.count_table[val + 1]
            del_node.prev_cl.next_cl = del_node.next_cl
            del_node.next_cl.prev_cl = del_node.prev_cl
            del (self.count_table[val + 1])

        print 'dec', key, val
        for v in self.count_table:
            print 'v:',v,
            node = self.count_table[v]._next
            while node:
                print node.key, node.val
                node = node._next

        if self.head.next_cl._next:
            print 'head',self.head.next_cl._next.key, self.head.next_cl._next.val
        print '\n'

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head.next_cl and self.head.next_cl != self.tail:
            return self.head.next_cl._next.key
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.tail.prev_cl and self.tail.prev_cl != self.head:
            return self.tail.prev_cl._next.key
        else:
            return ""

import collections

class AllOne_2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = collections.defaultdict(set)
        self.cache = collections.defaultdict()
        self.max_freq = 0
        self.min_freq = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.cache:
            curr_freq = self.cache[key]
            self.freq[curr_freq].remove(key)

            if len(self.freq[curr_freq]) == 0:
                del self.freq[curr_freq]

            curr_freq += 1
            self.freq[curr_freq].add(key)
            self.cache[key] = curr_freq

        else:
            self.cache[key] = 1
            self.freq[1].add(key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.cache:
            curr_freq = self.cache[key]

            self.freq[curr_freq].remove(key)

            if len(self.freq[curr_freq]) == 0:
                del self.freq[curr_freq]

            curr_freq -= 1

            if curr_freq != 0:
                self.freq[curr_freq].add(key)
                self.cache[key] = curr_freq
            else:
                del self.cache[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        print self.freq
        if self.freq:
            max_freq = max(self.freq.keys())
            return list(self.freq[max_freq])[0]

        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """

        if self.freq:
            min_freq = min(self.freq.keys())
            return list(self.freq[min_freq])[0]

        return ''


#["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
#[[],  ["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]
#Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc('hello')
obj.inc('goodbye')
obj.inc('hello')
obj.inc('hello')
print obj.getMaxKey()
obj.inc('leet')
obj.inc('code')
obj.inc('leet')
obj.dec('hello')
obj.inc('leet')
obj.inc('code')
obj.inc('code')
print obj.getMaxKey()

# param_3 = obj.getMaxKey()
# print param_3
# param_4 = obj.getMinKey()
# print param_4


