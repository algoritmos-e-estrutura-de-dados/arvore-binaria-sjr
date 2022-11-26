from pastaTree.binary_tree import BinaryTree

arvore = BinaryTree()
arvore.adicionar(12)
arvore.adicionar(8)
arvore.adicionar(5)
arvore.adicionar(10)
arvore.adicionar(1)
arvore.adicionar(6)
arvore.adicionar(9)
arvore.adicionar(11)


arvore.remover(8)


arvore.print_arvore("preorder")

