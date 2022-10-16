class Stack:
    def __init__(self):
        self.top = []
    def __str__(self):
        return str(self.top)
    def isEmpty(self):
        return len(self.top) == 0
    def push(self,item):
        self.top.append(item)
    def pop(self): 
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []

odd = Stack()
even = Stack()
  
for i in range(10):
    if i % 2 == 0:
        even.push(i)
    else:
        odd.push(i)
# print(odd)
# print(even)

# 괄호 검사 구현
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == '}' and left != '{'):
                    return False
    return stack.isEmpty()

str = '{dfdf(dfsad)Df}'
# print(checkBrackets(str))

# 후위표기 수식의 계산
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in '+-*/':
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1+val2)
            elif token == '-':
                s.push(val1-val2)
            elif token == '*':
                s.push(val1*val2)
            elif token == '/':
                s.push(val1/val2)
        else:
            s.push(float(token))
    return s.pop()

sent = ['8','2','/','3','-','3','2','*','+']
# print(evalPostfix(sent))

# 중위표기식의 후위 변환 구현
def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expr):
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop()) 
    return output

infix1 = ['8','/','2','-','3','+','(','3','*','2',')']
# print('중위표기식 후위수식 변환\n',Infix2Postfix(infix1))
# print('계산 결과\n',evalPostfix(Infix2Postfix(infix1)))

# P4.1
def make_reverse(sent):
    new_s = Stack()
    for i in sent:
        new_s.push(i)

    result = ''
    for j in range(len(new_s.top)):
        s = new_s.pop()
        result += s

    return result

# P4.2
def find_palindrome(word):
    temp = ''
    for w in word:
        if w.isalpha():
            temp += w
    
    temp = temp.lower()
    rev = make_reverse(temp) 
    s = Stack()
    s_rev = Stack()
    for i in temp:
        s.push(i)
    for j in rev:
        s_rev.push(j)
    flag = True
    for i in range(len(temp)):
        a = s.pop()
        b = s_rev.pop()
        if a != b:
            flag = False
            break
    return flag
pal_word = 'madam, I"m Adam'
# print(find_palindrome(pal_word))

