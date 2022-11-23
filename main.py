from binary_tree import BinaryTree

arvore = BinaryTree()
arvore.adicionar(5)
arvore.adicionar(3)
arvore.adicionar(4)
arvore.adicionar(2)
arvore.print_arvore("postorder")
arvore.remover(4)
arvore.print_arvore("postorder")

