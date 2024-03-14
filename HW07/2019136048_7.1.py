class SortedSet:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

    def size(self):
        return len(self.items)

    def contains(self, item):
        left, right = 0, len(self.items) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == item:
                return True
            elif self.items[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def insert(self, e):
        if self.contains(e):
            return
        self.items.append(e)
        self.items.sort()

    def delete(self, e):
        self.items.remove(e)

    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for i in range(self.size()):
            if self.items[i] != setB.items[i]:
                return False
        return True

    def union(self, setB):
        setC = SortedSet()
        i = 0
        j = 0
        while i < self.size() and j < setB.size():
            a = self.items[i]
            b = setB.items[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                setC.insert(b)
                j += 1

        while i < self.size():
            setC.insert(self.items[i])
            i += 1
        while j < setB.size():
            setC.insert(setB.items[j])
            j += 1

        return setC

    def intersect(self, setB):
        setC = SortedSet()
        i = 0
        j = 0
        while i < self.size() and j < setB.size():
            a = self.items[i]
            b = setB.items[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1

        return setC

    def difference(self, setB):
        setC = SortedSet()
        i = 0
        j = 0
        while i < self.size() and j < setB.size():
            a = self.items[i]
            b = setB.items[j]
            if a == b:
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                j += 1

        return setC

if __name__ == "__main__":
    import random
    setA = SortedSet()
    setB = SortedSet()
    for i in range(10):
        setA.insert(random.randint(1, 99))
        setB.insert(random.randint(1, 99))

    print('Set A:', setA)
    print('Set B:', setB)
    print('A U B:', setA.union(setB))
    print('A ^ B:', setA.intersect(setB))
    print('A - B:', setA.difference(setB))
