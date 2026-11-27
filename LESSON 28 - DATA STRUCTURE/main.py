'''
Lesson 28 - Data structure
bytes
bytearray
stack LIFO
queue FIFO
linked list
'''
from queue import Queue

def demo_bytes():
    print('\n=== Bytes ===')
    b1 = bytes([72, 101, 108, 108, 111])
    print(type(b1), b1)
    print(b1[0])
    print(b1.find(b'o'))
    b2 = b'Hello World'
    print(type(b2), b2)
    s1 = 'Python'
    b3 = bytes(s1, 'utf-8')
    print(type(b3), b3)

def demo_bytearray():
    print('\n=== Bytearray ===')
    b = bytearray([72, 101, 108, 108, 111])
    print(type(b), b)
    b[0] = 74
    print(b)
    b.append(33)
    print(b)
    b.pop()
    print(b)
    b.extend(b)
    print(b)


def demo_stack():
    print('\n=== Stack ===')
    stack = []
    stack.append('a')
    print(type(stack), stack)
    stack.append('b')
    stack.append('c')
    print(stack)
    stack.pop()
    print(stack)

def demo_queue():
    print('\n=== Queue ===')
    q = Queue()
    print(type(q), q.queue)
    q.put('1')
    print(q.queue)
    q.put('2')
    print(q.queue)
    q.put('3')
    print(q.queue)
    q.get()
    print(q.queue)
    q.get()
    print(q.queue)






    
         


class LinkedList:
    def __init__(self):
        self.head = None

def demo_linked_list():
    print('\n=== Linked List ===')
    l = LinkedList()
    n1 = Node(1)
    l.head = n1
    print(l.head, l.head.next)
    n2 = Node(2)
    n3 = Node(3)
    l.head.next = n2
    n2.next = n3
    print(n1, n1.next)
    print(n2, n2.next)
    print(n3, n3.next)

    current = n1
    while current:
        print(current.data, end=' -> ')
        current = current.next
    else:
        print(current)

class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.childnode = []





class Nodev2:
    def __init__(self, name, data, parent_node=None):
        self.name = name
        self.data = data
        self.parentnode = parent_node
        self.childnode = []

        if parent_node is not None:
            parent_node.childnode.append(self)

class Path_taken:
    def __init__(self):
        self.path = []
    
        

def demo_linked_list_v2():
    n1 = Nodev2('n1','Ace')
    n21 = Nodev2('n21', 'king', n1)
    n31 = Nodev2('n31', 'queen', n21)
    n32 = Nodev2('n32', 'queen', n21)
    n33 = Nodev2('n33', 'queen', n21)
    n22 = Nodev2('n22', 'king', n1)
    n34 = Nodev2('n34', 'queen', n22)
    n35 = Nodev2('n35', 'queen', n22)
    n36 = Nodev2('n36', 'queen', n22)
    n23 = Nodev2('n22', 'king', n1)
    n37 = Nodev2('n37', 'queen', n23)
    n38 = Nodev2('n38', 'queen', n23)
    n39 = Nodev2('n39', 'queen', n23)
    
    tree_readerv2(n1, [])
    
def tree_reader1(node, n):
    print(1)
    if node.childnode:
        node = node.childnode[n]
        tree_reader(node, n)
    else:
        print(f'{node.parentnode.name} {node.name},{node.data}')
        node = node.parentnode
        
        if (len(node.childnode)-1) != n:
            print('heelo')
            n += 1
            tree_reader(node, n)
        else:
            print('end')
            node = node.parentnode
            print(f'{node.name},{node.data}')
            tree_reader(node, n +1  )


def tree_reader(node):
    print(f"{node.name} {node.data}")

    for child in node.childnode:
        tree_reader(child)


def tree_readerv2(node, p): #p must be [0] i think
    if not node.childnode:
        if node.parentnode is None:
            print(f'{node.name} {node.data} at a super parent node')
        else:
            print(f'{node.parentnode.name} {node.name} {node.data}')
            node = node.parentnode
            print(f'{node.name}')
        for a in range(len(node.childnode)):
            
            if (p[-1] + 1) == len(node.childnode):
                if node.parentnode is None:
                    print('super parent')
                else:
                    node = node.parentnode
                    p.pop()
                    print(f'{node.parentnode.name} {node.name} {node.data}')
            else:
                p[-1] =  a + 1
                tree_readerv2(node, p)
                break
            
    else:
        if not p:
            p.append(0)
            node = node.childnode[0]
            tree_readerv2(node, p)
        if p[-1] != 0:
            node = node.childnode[p[-1]]
            tree_readerv2(node, p)
        else:    
            node = node.childnode[p[-1]]
            
            tree_readerv2(node, p)

        

        

    

    

   
    


def main():
    #demo_bytes()
    #demo_bytearray()
    #demo_stack()
    #demo_queue()
    #demo_linked_list()
    demo_linked_list_v2()
    

if __name__ == "__main__":
    main()