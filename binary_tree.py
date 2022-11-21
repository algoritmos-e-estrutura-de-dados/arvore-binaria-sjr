from node import Node

class Binary_tree:

    def __init__(self):
        self.root = None



    def adicionar(self,value):
        node = Node(value)
        if self.root is None:
            self.root = node
            #aux = self.root
        #verificar se o valor vai ficar na direita ou esquerda
        else:
            pai:Node
            while(True):
                if self.root.value <= value:
                    pai = self.root
                    self.root = self.root.getEsquerda()
                    filho_esquerda = True #verificar se há valor na esquerda
                else:
                    pai = self.root
                    self.root = self.root.getDireita()
                    filho_esquerda = False #verificra se há na direita

                if self.root is None:
                    break
            if filho_esquerda is False:
                pai.setDireita(node)
            else:
                pai.setEsquerda(node)
    #percorrimento pré-ordem
    def pre_ordem(self):
        print(self.root.value)
        self.pre_ordem(self.root.getEsquerda)
        self.pre_ordem(self.root.getDireita)








