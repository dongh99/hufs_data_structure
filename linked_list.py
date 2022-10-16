# 연결된 스택 


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def clear(self):
        self.top = None
    def push(self, item):
        n = Node(item,self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self,msg='LinkedStack:'):
        print(msg,end='')
        node = self.top
        while not node == None:
            print(node.data, end = ' ')
            node = node.link
        print()

# odd = LinkedStack()
# even = LinkedStack()

# for i in range(10):
#     if i % 2 == 0:
#         even.push(i)
#     else:
#         odd.push(i)
# odd.display()
# even.display()    
# print(even.peek())
# print(odd.peek())
# for _ in range(2):
#     even.pop()
# for _ in range(3):
#     odd.pop()
# even.display()
# odd.display()

# 연결된 리스트

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self,msg='LinkedList:'):
        print(msg,end='')
        node = self.head
        while not node == None:
            print(node.data, end= ' ')
            node = node.link
        print()
    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
    def replace(self,pos,elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return None
    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
        else:
            node = Node(elem,before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
    # def merge(self, merge_list):
    #     len_list = merge_list.size()
    #     size_num = self.size()
    #     for i in range(len_list):
    #         data = merge_list.getEntry(i)
    #         self.insert(size_num+i,data)




# s = LinkedList()
# s.display()
# s.insert(0,10)
# s.insert(0,20)
# s.insert(1,30)
# s.insert(s.size(),40)
# s.insert(2,50)
# s.display()
# s.replace(2,90)
# s.display()
# s.delete(2)
# s.delete(s.size()-1)
# s.delete(0)
# s.display()

# 연결된 큐 with 원형연결리스트
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self):
        return self.tail == None
    def clear(self):
        self.talii = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self,item):
        node = Node(item,None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self,msg='CircularLinkedQueue:'):
        print(msg,end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data,end=' ')
                node = node.link
            print(node.data,end=' ')
        print()

# q = CircularLinkedQueue()
# for i in range(8):
#     q.enqueue(i)
# q.display()
# for i in range(5):
#     q.dequeue()
# q.display()
# for i in range(8,14):
#     q.enqueue(i)
#     # print(q.isFull())
# q.display() 

# 연결된 덱 -> 이중연결리스트 응용
class DNode:
    def __init__(self,elem,prev=None,next=None):
        self.data = elem
        self.prev = prev
        self.next = next
class DoublyLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def clear(self):
        self.front = self.rear = None
    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count
    def display(self, msg = 'DoublyLinkedQueue:'):
        print(msg, end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()
    def getFront(self):
        return self.front.data
    def getRear(self):
        return self.rear.data
    def addFront(self,item):
        node = DNode(item,None,self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def addRear(self,item):
        node = DNode(item,self.rear,None)
        if self.isEmpty():
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

# dq = DoublyLinkedQueue()
# for i in range(9):
#     if i % 2 == 0:
#         dq.addRear(i)
#     else:
#         dq.addFront(i)
# dq.display()
# for i in range(2):
#     dq.deleteFront()
# for i in range(3):
#     dq.deleteRear()
# dq.display()
# for i in range(9,14):
#     dq.addFront(i)
# dq.display()           

# 6.12
# lq = CircularLinkedQueue()

# while True:
#     n = input('양의 정수를 입력하세요(종료: -1): ')
#     if n == '-1':
#         break
#     lq.enqueue(n)
# for i in range(lq.size()+1):
#     print(lq.dequeue(),end=' ')

# 6.13, 6.14
# n = int(input('노드의 개수: '))
# linked_list = LinkedList()
# for i in range(1,n+1):
#     data = int(input(f'노드 #{i} 데이터 : '))
#     linked_list.insert(i-1,data)
# plus_data = int(input('끝에 추가할 데이터: '))
# linked_list.insert(n,plus_data)
# linked_list.display()

# 6.15
# n = int(input('노드의 개수: '))
# linked_list = LinkedList()
# for i in range(1,n+1):
#     data = int(input(f'노드 #{i} 데이터 : '))
#     linked_list.insert(i-1,data)
# linked_list.display()
# linked_list.delete(0)
# linked_list.display()

# 6.16
# n = int(input('노드의 개수: '))
# linked_list = LinkedList()
# for i in range(1,n+1):
#     data = int(input(f'노드 #{i} 데이터 : '))
#     linked_list.insert(i-1,data)
# result = 0
# for i in range(linked_list.size()):
#     result += linked_list.getEntry(i)
# print(result)

# 6.17
# n = int(input('노드의 개수: '))
# linked_list = LinkedList()
# for i in range(1,n+1):
#     data = int(input(f'노드 #{i} 데이터 : '))
#     linked_list.insert(i-1,data)
# find_num = int(input('탐색할 값을 입력하시오: '))
# cnt = 0
# while not n == None:
#     n = linked_list.find(find_num)
#     cnt+=1
#     linked_list.delete(n) # delete 함수 수정후
# print(cnt)

# 6.1

# word = input('회문 입력: ')
# final = ''
# for i in word:
#     if i.isalpha():
#         final += i
# final = final.lower()

# palin_stack = LinkedStack()
# for i in final:
#     palin_stack.push(i)

# result = ''
# for i in range(palin_stack.size()):
#     result += palin_stack.pop()

# if final == result:
#     print(True)
# else:
#     print(False)

# 6.2

# A = LinkedList()
# B = LinkedList()
# for i in range(5):
#     A.insert(i,i+1)
# for i in range(5):
#     B.insert(i,i+11)
# A.merge(B)
# A.display()



