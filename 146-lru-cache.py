"""leetcode 146 实现一个LRU缓存算法 中等
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:你是否可以在 O(1) 时间复杂度内完成这两种操作？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import OrderedDict


class LRUCache:
    """使用内置的OrderedDict实现"""
    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.remain = capacity  # 缓存可存储的剩余元素数量，当为0且要插入新元素时需要清除最老的元素

    def get(self, key: int) -> int:
        """获取缓存中的元素值
        1. 若当前元素不在缓存中，返回-1
        2. 若当前元素在缓存中，将当前元素移到链表头部，返回当前元素的值
        :param key:
        :return:
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        """插入元素
        1. 若当前元素不在缓存中，（1）若缓存已满，删除最远一个元素，插入当前元素；（2）若缓存未满，直接插入当前元素
        2. 若当前元素在缓存中，将当前元素移到链表头部（删除当前元素结点，在头部插入当前元素）
        :param key:
        :param value:
        :return:
        """
        if key not in self.dic:
            if self.remain == 0:
                self.dic.popitem(last=False)  # drop
            else:
                self.remain -= 1
        else:
            self.dic.pop(key)
        self.dic[key] = value


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache1:
    """哈希表+双向链表实现"""
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == self.capacity:
                removed = self._remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1
        else:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    @staticmethod
    def _remove_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev
