from pastaNode.node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        else:
            aux = self.root
            while True:
                if aux.value >= value:
                    pai = aux
                    aux = aux.getEsquerda()
                    filho_esquerda = True  # verificar se há valor na esquerda
                else:
                    pai = aux
                    aux = aux.getDireita()
                    filho_esquerda = False  # verificar se há na direita

                if aux is None:
                    break
            if filho_esquerda is False:
                pai.setDireita(node)
            else:
                pai.setEsquerda(node)

    def remover(self, value):
        #percorrendo
        filho_esquerda = False
        if value is None:
            print("O valor é nulo")
            return
        else:
            pai, aux =self.busca_elemento(value)
        #removendo

        if aux == self.root:
            #removendo a raiz sem filhos
            if aux.getEsquerda() is None and aux.getDireita() is None:
                self.root = None
                print("raiz removida")
                # removendo esquerdaW
            elif aux.getEsquerda() is not None and aux.getDireita() is None:
                if self.root.getEsquerda() is None:
                    self.root = self.root.getEsquerda()
                else:
                    pai, avo = self.buscar_folha(True)
                    #pai.setEsquerda(avo.getEsquerda()) funciona pegando o 2 maior a esquerda caso exista
                    #self.insere_manual(avo)
                    pai.setDireita(self.root.getDireita())
                    self.root = pai
                print("raiz removida, filhoEsquerda nova raiz")
                #removendo direita
            elif aux.getEsquerda() is None and aux.getDireita() is not None:
                if self.root.getDireita() is None:
                    self.root = self.root.getDireita()
                else:
                    pai, avo = self.buscar_folha(False)
                   # pai.setDireita(avo)
                    pai.setEsquerda(self.root.getEsquerda())
                    self.root = pai

                print("raiz removida, filhoDireita nova raiz ")
        else: #removendo quando não é raiz
            aux = self.root
            #removendo filho  esquerda
            if value < aux.value:
                    if aux.getEsquerda().getEsquerda() is None:#verificando se o filho do nó a esquerada existe
                        if aux.getEsquerda().getDireita() is None and aux.getEsquerda().getEsquerda() is None:#no sem filhos
                            self.root.setEsquerda(None)
                        elif aux.getEsquerda().getDireita() is not None and aux.getEsquerda().getEsquerda() is None:#somente filhos a direita
                            self.root.getEsquerda(aux.getEsquerda().getDireita())
                        elif aux.getEsquerda().getDireita() is None and aux.getEsquerda().getEsquerda() is not None: #somente filho a esquerda
                            self.root.setEsquerda(aux.getEsquerda.getEsquerda())
                        elif aux.getEsquerda().getDireita() is not None and aux.getEsquerda().getEsquerda() is not None:
                            print("2 filhos")
                            aux2 = self.root.getEsquerda().getEsquerda()#pegando o filho a esquerda do nó a ser removido
                            self.root.setEsquerda(aux.getEsquerda().getDireita())
                            pai, _ = self.buscar_folha(aux.getEsquerda(), True)
                            pai.setEsquerda(aux2)
                            self.root.setEsquerda(pai)
            else: #verificação do filho a direita
                aux = self.root
                if aux.getDireita().getDireita() is None and aux.getDireita().getEsquerda() is None:
                    self.root.setDireita(None)
                elif aux.getDireita().getDireita() is not None and aux.getDireita().getEsquerda() is None: #somente o filho a direita
                    self.root.getDireita(aux.getEsquerda().getDireita())
                elif aux.getDireita().getDireita() is not None and aux.getDireita().getEsquerda() is not None:
                    aux2 = self.root.getDireita().getEsquerda()  # pegando o filho a direita do nó a ser removido
                    self.root.setDireita(aux.getEsquerda().getDireita())
                    pai, _ = self.buscar_folha(aux.getDireita(), True)
                    pai.setEsquerda(aux2)
                    self.root.setDireita(pai)



    # def insere_manual(self,avo):
    #     node2 = Node(avo.value)
    #     aux = avo
    #     while True:
    #        if aux.getEsquerda() is not None:
    #            node2.setEsquerda(aux.getEsquerda())
    #        elif aux.getDireita() is not None:
    #            node2.setDireita(aux.setDireita())
    #        if aux.getDireita() is None and aux.getEsquerda is None:
    #            break

    def buscar_folha(self,filho_esquerda):
        aux = self.root
        if filho_esquerda:
            aux = aux.getEsquerda()
            nivel = 0
            while aux is not None:
                 pai = aux
                 aux = aux.getDireita()
                 nivel += 1
            avo = self.buscar_pai(nivel,filho_esquerda)
            return pai, avo
        else:
            nivel = 0
            aux = aux.getDireita()
            while aux is not None:
                pai = aux
                aux = aux.getEsquerda()
                nivel += 1
            avo = self.buscar_pai(nivel, filho_esquerda)
            return pai,avo

    def busca_elemento(self,value):
        aux = self.root
        pai = aux
        while aux.value != value:
            if value <= aux.value:
                aux = aux.getEsquerda()
                filho_esquerda = True
            else:
                aux = aux.getDireita()
                filho_esquerda = False
            if aux is None:
                print("elemento inexistente")
                return

        print("valor encontrado é:", aux.value)
        print("e o pai é:", pai.value)
        return pai,aux
    def buscar_pai(self,nivel,filho_esquerda):
        aux = self.root
        cont = 0
        while True:
            pai = aux
            if filho_esquerda:
                aux = aux.getEsquerda()
            else:
                aux = aux.getDireita()
            if cont == nivel - 1:
                break
            cont += 1

        return pai



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
