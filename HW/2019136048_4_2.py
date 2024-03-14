from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

def precedence(op):
    if op in ('(', ')'):
        return 0
    elif op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    else:
        return -1

def InToPost(expr):
    s = ArrayStack(100)
    output = []
    tokens = expr.split()  

    for term in tokens:
        if term == '(':
            s.push('(')
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
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

    postfix_expr = ' '.join(output)

    return postfix_expr

if __name__ == "__main__":
    print('스택의 응용3: 중위표기식 후위표기 변환 및 계산\n')

    infix_expr = input('중위 표기식을 입력하세요 (연산자와 피연산자는 공백으로 분리): ')
    postfix_expr = InToPost(infix_expr)
    result = evalPostfix(postfix_expr.split())  
    print('중위표기식:', infix_expr)
    print('후위표기식:', postfix_expr)
    print('계산결과:', result)
