import math

def localIndex(index, base):
    if index < (1 << base):
        return 0, index
    i = 0
    val = index
    while val != 0:
        val >>= 1
        i += 1
    maxpos = 1<<i - 1
    return i - base, index - maxpos


class LinkedArray:
    def __init__(self, iterable, base):
        self.base = base
        self.iterable = iterable
        self.length_previous = len(iterable)
        self.length = base**2
        i = 1
        while self.length < len(iterable):
            self.length += base**(2 + i)
            i += 1
        for i in range(self.length - len(iterable)):
            self.iterable.append(None)
        # print(self.iterable)
        next_node = None
        j = 0
        self.i = 0
        for i in range(int(localIndex(len(iterable), base)[0])):
            self.head = ArrayNode(self.iterable[j: j + 2 ** (base + i)], next_node)
            next_node = self.head
            j += 2 ** (base + i)
            self.i = i

    def __str__(self):
        result = []
        elem = self.head
        i = 0
        while elem is not None:
            result.append(f'[{str(elem)}]')
            elem = elem.next_node
        s = '\n'.join(reversed(result))
        return s

    def append(self, value):
        elem1 = self.head
        elem2 = elem1.head
        check = True
        while elem2.value is not None:
            if elem2.next_node is None:
                a = [value]
                for i in range(2**(self.base+self.i+1) - 1):
                    a.append(None)
                self.head = ArrayNode(a, elem1)
                check = False
                self.i += 1
                break
            elem2 = elem2.next_node
        if check:
            elem2.value = value

    def delete(self):
        elem1 = self.head
        elem2 = elem1.head
        if elem2.next_node.value is None:
            self.head = elem1.next_node
            self.i -= 1
        else:
            while elem2.next_node.value is not None:
                if elem2.next_node.next_node is None:
                    elem2 = elem2.next_node
                    break
                elem2 = elem2.next_node
            elem2.value = None

    def get(self, index):
        global_index, local_index = 0, 0
        i = 0
        while index - global_index >0:
            if index - (global_index + 2**(self.base+i)) > 0:
                global_index += 2**(self.base+i)
                i += 1
            else:
                break
        local_index = index - global_index
        global_index = i
        elem1 = self.head
        for i in range(self.i - global_index):
            elem1 = elem1.next_node
        elem2 = elem1.head
        for j in range(local_index - 1):
            elem2 = elem2.next_node
        return elem2.value

    def lengt(self):
        res = 0
        for i in range(self.i):
            res += 2**(self.base + i)
        elem1 = self.head
        elem2 = elem1.head
        while elem2.value is not None:
            elem2 = elem2.next_node
            res += 1
            if elem2.next_node is None:
                res += 1
                break
        return res

class ArrayNode:
    def __init__(self, values, next_node):
        self.values = values
        self.next_node = next_node
        next_node = None
        # print(values)
        self.head = Node(values[0], None)
        for elem in reversed(values):
            self.head = Node(elem, next_node)
            next_node = self.head

    def __str__(self):
        result = ''
        elem = self.head
        while elem is not None:
            result += f'{str(elem)}, '
            elem = elem.next_node
        return result[:-2]


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


a = LinkedArray([1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 11, 12, 13], 2)
# print(a)
# a.append(15)
# print(a)
# a.delete()
# print(a)
# print(a.get(9))
# print(a)
# print(a.lengt())