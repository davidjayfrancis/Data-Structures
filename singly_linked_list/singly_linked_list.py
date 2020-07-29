class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node = Node(value)
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    def contains(self, value):
        cur_node = self.head
        while cur_node is not None: 
            if value == cur_node.get_value():
                return True
            cur_node = cur_node.get_next()
        return False

    def remove_head(self):
        # case 1: long list 
        # 1. create temporary var for head.next_node
        if self.head == self.tail and self.length > 0:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_head.value
        elif self.length == 0:
            return None
        else:
            temp = self.head.get_next()
            old_head = self.head
            self.head.set_next(None)
            self.head = temp
            self.length -=1
            return old_head.value
        
    def get_max(self):
        cur_node = self.head
        
        if cur_node == None:
            return None
            
        max_val = self.head.value
        while cur_node is not None: 
            if cur_node.value > max_val: 
                max_val = cur_node.value
            cur_node = cur_node.get_next()
        return max_val


