class LinkedListNode2 :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None        
                
class LinkedList2:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        
    def addFirst(self, data):
        node = LinkedListNode2(data)
        if self.firstNode == None:
            self.firstNode = node
            self.lastNode = node
        else:
            node.next = self.firstNode
            self.firstNode.prev = node
            self.firstNode = node
    
    def addLast(self, data):
        node = LinkedListNode2(data)
        if self.lastNode == None:
            self.firstNode = node
            self.lastNode = node
        else:
            node.prev = self.lastNode
            self.lastNode.next = node
            self.lastNode = node
            
    def findNode(self, data):
        node = self.firstNode
        while not node == None:
            if node.data == data:
                return node
            node = node.next
        return None
            
    def delete(self, node):
        if self.firstNode == None:
            return
            
        #delete only node
        if node == self.firstNode and node == self.lastNode:
            self.firstNode = None
            self.lastNode = None
            return

        #delete firstNode
        if node == self.firstNode :
            self.firstNode = self.firstNode.next
            self.firstNode.prev = None
            return

        #delete lastNode
        if node == self.lastNode :
            self.lastNode = self.lastNode.prev
            self.lastNode.next = None
            return

        #delete middleNode
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return      

    def dump(self):
        node = self.firstNode
        while not node == None:
            print(node.data)
            node = node.next
            
