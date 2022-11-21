from node import Node


class Binary_tree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        else:
            aux = self.root
            while (True):
                if aux.value <= value:
                    pai = aux
                    aux = aux.getEsquerda()
                    filho_esquerda = True  # verificar se há valor na esquerda
                else:
                    pai = aux
                    aux = aux.getDireita()
                    filho_esquerda = False  # verificra se há na direita

                if aux is None:
                    break
            if filho_esquerda is False:
                pai.setDireita(node)
            else:
                pai.setEsquerda(node)



    # preorder
    def preorder_print(self, start, string):
        if start:
            string += (str(start.value) + "-")
            string = self.preorder_print(start.esquerda, string)
            string = self.preorder_print(start.direita, string)
        return string

    # inorder
    def inorder_print(self, start, string):
        if start:
            string = self.inorder_print(start.esquerda, string)
            string += (str(start.value) + "-")
            string = self.inorder_print(start.direita, string)
        return string

    # postorder
    def postorder_print(self, start, string):
        # esquerda - direita - raiz
        if start:
            string = self.postorder_print(start.esquerda, string)
            string = self.postorder_print(start.direita, string)
            string += (str(start.value) + "-")
        return string

    def print_arvore(self, tipo):
        if tipo == "preorder":
            return print(self.preorder_print(self.root, ""))
        elif tipo == "inorder":
            return print(self.inorder_print(self.root, ""))
        elif tipo == "postorder":
            return print(self.postorder_print(self.root, ""))
        else:
            print("Tipo de traversal não existente")
