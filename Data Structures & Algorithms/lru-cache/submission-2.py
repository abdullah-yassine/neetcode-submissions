class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.capacity = capacity
        self.hashmap = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            to_be_moved = self.hashmap[key]
            to_be_moved.prev.next = to_be_moved.next
            to_be_moved.next.prev = to_be_moved.prev

            self.insert_at_tail(to_be_moved)

            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 1. exists
        if key in self.hashmap:
            self.hashmap[key].val = value
            node = self.hashmap[key]
            # connection of prev and next nodes
            next_node, prev_node = node.next, node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            # change
            self.insert_at_tail(node)
        else:
            new_node = Node(value, key)
            # check capacity
            if self.size == self.capacity:
                self.hashmap.pop(self.head.next.key, None)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            self.insert_at_tail(new_node)
            self.hashmap[key] = new_node

            self.size += 1 if self.size < self.capacity else 0

    def insert_at_tail(self, node):
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
        

        # 2. does not exist, check size or capacity
class Node:
    def __init__(self, val : int = 0, key : int = 0, next : Node = None, prev : Node = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

