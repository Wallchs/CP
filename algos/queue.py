#a Queue é como uma fila igualzinha em seu comportamento
#O(n) para adicionar e remove itens no começo e O(1) para adicionar e remover no final
#o funcionamento é parecido com a linkedlisted mas com a troca do nome de head e tail para first e last

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):#adiciona elementos no final da fila
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):#retira elemento do começo da fila
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1 
        return temp

            


myqueue = Queue(4)
myqueue.enqueue(88)
myqueue.enqueue(10)
myqueue.enqueue(16)
myqueue.enqueue(10)
myqueue.print_queue()
print("-----------------------")
myqueue.dequeue()
myqueue.print_queue()

