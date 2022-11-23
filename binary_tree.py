from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        else:
            aux = self.root
            print(aux.getDireita())
            while True:
                if aux.value >= value:
                    pai = aux
                    print("auxEsquerda",aux.getEsquerda()) #get esquerda não esta  funcionando
                    aux = aux.getEsquerda()
                    filho_esquerda = True  # verificar se há valor na esquerda
                else:
                    pai = aux
                    aux = aux.getDireita()
                    print(aux) # getDireita ---> funcionando
                    filho_esquerda = False  # verificar se há na direita

                if aux is None:
                    break
            if filho_esquerda is False:
                pai.setDireita(node)
            else:
                pai.setEsquerda(node)



    def remover(self, value):
        aux = self.root
        if aux.value is None:
           # print("Árvore vazia")
            return False
        # realizar o percorrimento para achar o elemanto

        while aux.value != value:
           # print(aux.value)
            pai = aux
            if value < aux.value:
               # print(aux.getDireita()) # getEsquerda não esta armazenando valor
                aux = aux.getEsquerda()
                filho_esquerda = True
            else:
                aux = aux.getDireita()
                filho_esquerda = False

            if aux is None:
                # break
                return False # não está saindo do loop
        # remoção do elemento
        if aux.getEsquerda() is None and aux.getDireita() is None:   #testar depois se está funcionando
            if aux == self.root:
                self.root = None
            elif filho_esquerda is True:
                pai.setEsquerda(None)
            else:
                pai.setDireita(None)
        elif aux.getDireita() is None:
            if aux == self.root:
                self.root = self.root.getDireita()
            elif filho_esquerda is True:
                pai.setEsquerda(aux.getEsquerda())
            else:
                pai.setDireita(aux.getEsquerda())
        else:
            if aux == self.root:
                self.root = self.root.getDireita()
            elif filho_esquerda is True:
                pai.setEsquerda(aux.getDireita())
            else:
                pai.setDireita(aux.getDireita())
        return True

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
