from binary_tree import BinaryTree

arvore = BinaryTree()
arvore.adicionar(5)
arvore.adicionar(2)
arvore.adicionar(3)
arvore.adicionar(25)
arvore.adicionar(1)

arvore.remover(3)
arvore.remover(1)
arvore.print_arvore("preorder")

