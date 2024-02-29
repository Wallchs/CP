#a stack ao contrário da linked listed ela fica em pé e não tem o tail, sempre adiciona e remove elementos pelo top
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
         

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while(temp is not None):
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
        

my = Stack(2)
my.push(11)
my.push(3)
my.push(23)
my.push(7)
my.print_stack()
print("---------------------------")
my.pop()
my.print_stack()
