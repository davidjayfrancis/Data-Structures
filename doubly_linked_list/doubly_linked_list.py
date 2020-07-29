import sys
sys.path.append('../')
# p = sys.path[0][1:].replace('/','.').replace('doubly', 'singly') + '.singly_linked_list.py'
from singly_linked_list.singly_linked_list import Node

node = Node(20, Node(21, None))

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, node):
        self.next = node
    
    def set_prev(self, node):
        self.prev = node

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0: 
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
            return self.head.value
        elif self.length == 1: 
            new_node = ListNode(value)
            self.tail.set_prev(new_node)
            new_node.set_next(self.tail)
            self.head = new_node
            self.length += 1
        else: 
            new_node = ListNode(value)
            new_node.set_next(self.head) # set new_node pointer to old head
            self.head.set_prev(new_node) # set 2nd pos pointer to new_node
            self.head = new_node
            self.length += 1
            return self.head.value
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head
        new_head = self.head.get_next()
        if self.length == 0: 
            return None
        elif self.length == 1: 
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        else: 
            new_head.set_next(old_head.get_next()) # set next pointer to 2nd node
            old_head.get_next().set_prev(new_head) # set 2nd node pointer to new_node
            old_head.set_next(None) # remove right pointer
            self.head = new_head
            self.length -=1
            return old_head.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
        elif self.length == 1: 
            new_node = ListNode(value)
            self.head.set_next(new_node)
            new_node.set_prev(new_node)
            self.tail = new_node
            self.length += 1
        else: 
            new_node = ListNode(value)
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            self.length += 1
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1: 
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        else: 
            old_tail = self.tail
            new_tail = old_tail.get_prev()
            old_tail.set_prev(None)
            self.tail = new_tail
            self.length -= 1
            return old_tail.value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # find the node
        if self.length == 0: 
            return 0
        elif self.length == 1: 
            return node.value
        else: 
            cur_node = self.head
            while cur_node.get_next() is not None:

                if node.get_prev() == None: # it is the head
                    pass
                elif self.length == 1:
                    temp = self.head
                    self.head = self.tail
                    self.tail = temp
                else: 
                    if cur_node == node:
                        temp = self.head
                        cur_node.get_prev().set_next(cur_node.get_next()) # set prev node to point to next node
                        cur_node.get_next().set_prev(cur_node.get_prev()) # set cur_node's next node pointer its prev node
                        self.head.set_prev(node) # 2nd item points to new_head node
                        node.set_next(self.head())
                    else: 
                        pass # node not in the list
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # find node
        if self.length == 0: 
            pass
        elif self.length == 1: 
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            v = node.value
            cur_node = self.head
            while cur_node is not None:
                if cur_node.value == v and cur_node.prev is not None and cur_node.next is not None: 
                    print(f'node value: {cur_node.value}')
                    print(f"next: {cur_node.get_next().value}")

                    cur_node.get_next().set_prev(cur_node.get_prev())
                    cur_node.get_prev().set_next(cur_node.get_next())
                    cur_node.set_next(None)
                    cur_node.set_prev(None)
                    self.length -= 1
                    
                    break
                elif cur_node.value == v and cur_node.prev is None: # delete head
                    print(f'node value: {cur_node.value}')
                    print(f"next: {cur_node.get_next().value}")
                    print(f"prev: {cur_node.get_prev()}")
                    
                    cur_node.get_next().set_prev(None)
                    self.head = cur_node.get_next()
                    cur_node.set_next(None)
                    break
                elif cur_node.value == v and cur_node.next is None: # delete tail

                    cur_node.get_prev().set_next(None)
                    self.tail = cur_node.get_prev()
                    cur_node.set_prev(None)
                    break

                else:
                    cur_node = cur_node.get_next()
                

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass


l = DoublyLinkedList()
l.add_to_head(1)
l.add_to_head(7)
l.add_to_head(3)
l.add_to_tail(1)
l.add_to_tail(2)


l.delete(ListNode(2))


h = l.head

while h.get_next() is not None:
    print(h.value) 
    h = h.get_next()
print(h.value)

