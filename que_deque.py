# 원형 큐
MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front,self.rear),out)

# q = CircularQueue()
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

# 덱 구현 -> 원형 큐 클래스 상속 
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self,item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0:
                self.front = MAX_QSIZE - 1 
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item
    def getRear(self):
        return self.items[self.rear]

# dq = CircularDeque()
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

# 우선순위 큐 구현
class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

# q = PriorityQueue()
# q.enqueue(34)
# q.enqueue(18)
# q.enqueue(27)
# q.enqueue(45)
# q.enqueue(15)

# print("PQueue:",q.items)
# while not q.isEmpty():
#     print('Max Priority = ', q.dequeue()) 


# 5.17
# dq1 = CircularDeque()
# q1 = CircularQueue()
# for i in range(1,9):
#     dq1.addRear(i)
# for i in range(8):
#     item = dq1.deleteRear()
#     q1.enqueue(item)
# for i in range(8):
#     item = q1.dequeue()
#     dq1.addRear(item)
# dq1.display()

# P5.2

# P5.3

# fibo = CircularQueue()
# fibo.enqueue(0)
# fibo.enqueue(1)
# n = int(input())
# for i in range(n-1):
#     f1 = fibo.dequeue()
#     f2 = fibo.peek()
#     f3 = f1 + f2
#     fibo.enqueue(f3)
# fibo.dequeue()
# fibo.display()

# P5.4

sent = input()
def find_palin(sent):
    palin = CircularDeque()
    for i in sent:
        palin.addRear(i)
    flag = True
    for i in range(len(sent) // 2):
        if palin.getFront() == palin.getRear() or len(palin.items) == 1:
            palin.deleteFront()
            palin.deleteRear()
        else:
            flag = False
    return flag
print(find_palin(sent))