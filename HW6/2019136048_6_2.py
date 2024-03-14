# Linked List.
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

# 연결 리스트 기반 스택 구현
class LinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, elem):
        new_node = Node(elem, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.link
            return popped
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return None

# 중위 표기식을 후위 표기식으로 변환
def InToPost(expr):
    link= LinkedList()
    output = []
    tokens = expr.split()
    precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for term in tokens:
        if term == '(':
            link.push('(')
        elif term == ')':
            while not link.is_empty() and link.peek() != '(':
                output.append(link.pop())
            if not link.is_empty() and link.peek() == '(':
                link.pop()
        elif term in "+-*/":
            while not link.is_empty() and precedence.get(term, 0) <= precedence.get(link.peek(), 0):
                output.append(link.pop())
            link.push(term)
        else:
            output.append(term)

    while not link.is_empty():
        output.append(link.pop())

    postfix_expr = ' '.join(output)

    return postfix_expr

# 후위 표기식 계산
def evalPostfix(postfix):
    link = LinkedList()

    for token in postfix:
        if token.isdigit():
            link.push(int(token))
        elif token in "+-*/":
            operand2 = link.pop()
            operand1 = link.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    print("Error: Division by zero")
                    return None
                result = operand1 / operand2
            link.push(result)

    if not link.is_empty():
        return link.pop()
    else:
        return None

if __name__ == "__main__":
    print(' 중위표기식 후위표기 변환 및 계산\n')

    infix_expr = input('중위 표기식을 입력하세요 (연산자와 피연산자는 공백으로 분리): ')
    postfix_expr = InToPost(infix_expr)
    result = evalPostfix(postfix_expr.split())
    print('중위표기식:', infix_expr)
    print('후위표기식:', postfix_expr)
    print('계산결과:', result)
