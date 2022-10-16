class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self,pos, elem): 
        self.items.insert(pos, elem)

    def delete(self,pos):
        return self.items.pop(pos)

    def getEntry(self,pos): 
        return self.items[pos]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def find(self,item):
        return self.items.index(item)

    def replace(self,pos,elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self,lst):
        self.items.extend(lst)

    def display(self,msg='ArrayList:'):
        print(msg,self.size(),self.items)

class Set:
    def __init__(self):
        self.items =[]
    
    def size(self):
        return len(self.items)
    def display(self,msg):
        print(msg, self.items)
    def contains(self, item):
        return item in self.items
    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)
    def delelte(self,elem):
        if elem in self.items:
            self.items.remove(elem)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self,setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def difference(self,setB):   
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC

# P3.1-1
test_list = [1,2,3,4,5,6]
def insert2(pos,elem):
    result = []
    for i in range(pos):
        result.append(test_list[i])
    result.append(elem)
    for j in range(pos,len(test_list)):
        result.append(test_list[j])
    return result

print(insert2(2,7))

# P3.1-2
def delete2():
    return test_list.pop(-1)

print(delete2())

# P3.1-3
def find2(item):
    for i in test_list:
        if i == item:
            return i

print(find2(3))

# P3.1-4
def merge2(lst):
    for i in lst:
        test_list.append(i)
    return test_list
lst = [1,2,3]
print(merge2(lst))

# P3.3-1
def contains2(item):
    for i in test_list:
        if i == item:
            return True
    return False

print(contains2(9))

# P3.3-2
def delete3(item):
    if contains2(item):
        result = 0
        for i in range(len(test_list)):
            if test_list[i] == item:
                result = i
        test_list.pop(result)
    return test_list

print(delete3(4))

# P3.3-3
# in만 contains로 바꿔 구현

# p3.3-4
# def difference2(setB):
#     setC = []
#     for elem in test_list:
#         if elem in setB:
#             test_list - list(str(elem))
#     return test_list
# print(difference2([1,2]))

# P3.3-5
test_set = [1,2,3,4]
def isSubsetOf(otherSet):
    for i in test_set:
        if i not in otherSet:
            return False
    return True
otherSet = [1,2,3,4,5]
print(isSubsetOf(otherSet))

# P3.4
# class Polynomial:
#     def __init__(self):
#         self.items = []
#     def degree(self):
#         return self.items
#     def evaluate(self,scalar):
#         result = 0
#         for index,i in enumerate(self.items):
#             result += i * scalar ** index
#         return result
#     def add(self, rhs):
#         result = []
#         if len(self.items) <= rhs:
#             for i in range(len(self.items)):
#                 result.append(self.items[i]+rhs[i])
#             min_list = len(rhs) - len(self.items)
#             result.extend(rhs[min_list:])
#         else:
#             for j in range(len(rhs)):
#                 result.append(self.items[j]+rhs[j])
#             min_list = len(self.items) - len(rhs)
#             result.extend(self.items[min_list:])
#         return result
#     def read_poly(self,n):
#         for i in range(n+1):
#             self.items.append(int(input()))
#         return self.items
            
# a = Polynomial()
# b = Polynomial()
# a.read_poly(2)
# b.read_poly(3)
# c = a.items.add(b.items)
# print(c)







            


