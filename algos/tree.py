# A árvore é a mesma coisa da linked list pois é! Como eu nunca pensei nisso.
# a diferença é que ela tem duas direções a mais no seu node left e right o
# restante
# do código é parecido
# os elementos são chamados de parent(pais) e após os galhos são chamados de
# childNodes(galhos/filhos), que também pode ter ramificações os
# chamados leaf(folhas)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


mytree = BinarySearchTree()
mytree.insert(23)
mytree.insert(13)
mytree.insert(35)

print("Esse é o valor do primeiro", mytree.root.value)
print("esse é o valor da esquerda", mytree.root.left.value)
print("Esse valor é o da direita", mytree.root.right.value)
print(mytree.contains(1))
