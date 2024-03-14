
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    def __str__(self):
        arr = []
        node = self.top
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)

def evaluate_polynomial(polynomial, x):
    stack = LinkedStack()
    for coef in polynomial.coef:
        stack.push(coef)
    
    result = 0
    power_of_x = 1

    while not stack.isEmpty():
        coef = stack.pop()
        result += coef * power_of_x
        power_of_x *= x

    return result

class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def evaluate(self, x):
       result = 0
       for i, coef in enumerate(self.coef):
        result += coef * (x ** i)
       return result

  

    def __add__(self, other):
        max_degree = max(len(self.coef), len(other.coef))
        result_coef = [0] * max_degree

        for i in range(max_degree):
            if i < len(self.coef):
                result_coef[i] += self.coef[i]

            if i < len(other.coef):
                result_coef[i] += other.coef[i]

        return Polynomial(result_coef)

    def __sub__(self, other):
        return self.__add__(other *Polynomial([-1]))

    def __mul__(self, other):
        degree1 = len(self.coef) - 1
        degree2 = len(other.coef) - 1
        result_degree = degree1 + degree2
        result_coef = [0] * (result_degree + 1)

        for i in range(degree1 + 1):
            for j in range(degree2 + 1):
                result_coef[i + j] += self.coef[i] * other.coef[j]

        return Polynomial(result_coef)

    def display(self):
        terms = []
        for i, coef in enumerate(self.coef):
            if coef != 0:
                if i == 0:
                    term = f"{coef:.1f}"
                else:
                    term = f"{abs(coef):.1f} * x^{i}"
                if coef < 0:
                    term = "-" + term
                if i > 0:
                    terms.append(term)
                else:
                    terms.insert(0, term)  
        if not terms:
            return "0"  
        return " + ".join(terms)


degree1 = int(input("첫번쨰 다항식의 최고 차수를 입력하세요: "))
coef1 = []

for i in range(degree1 + 1):
    coef = float(input(f"첫번째 다항식,차수{i}의 계수를 입력하세요: "))
    coef1.append(coef)

degree2 = int(input("첫번쨰 다항식의 최고 차수를 입력하세요: "))
coef2 = []

for i in range(degree2 + 1):
    coef = float(input(f"두 번째 다항식, 차수 {i}의 계수를 입력하세요: "))
    coef2.append(coef)

poly1 = Polynomial(coef1)
poly2 = Polynomial(coef2)

x_value = float(input("다항식을 계산할 x 값을 입력하세요: "))

result1 = evaluate_polynomial(poly1, x_value)
result2 = evaluate_polynomial(poly2, x_value)
result_add = poly1 + poly2
result_sub = poly1 - poly2
result_mul = poly1 * poly2

A = evaluate_polynomial(result_add, x_value)
B = evaluate_polynomial(result_sub, x_value)
C = evaluate_polynomial(result_mul, x_value)

print("첫 번째 다항식:", poly1.display())
print("두 번째 다항식:", poly2.display())
print("덧셈 결과:", result_add.display())
print("뺄셈 결과:", result_sub.display())
print("곱셈 결과:", result_mul.display())
print(f"덧셈 결과 (x = {x_value}):", A)
print(f"뺄셈 결과 (x = {x_value}):", B)
print(f"곱셈 결과 (x = {x_value}):", C)
