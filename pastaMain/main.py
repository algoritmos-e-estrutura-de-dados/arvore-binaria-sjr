from pastaTree.binary_tree import BinaryTree

arvore = BinaryTree()

arvore.adicionar(8)
arvore.adicionar(5)
arvore.adicionar(1)
arvore.adicionar(6)
arvore.adicionar(9)

arvore.print_arvore("preorder")

arvore.remover_teste(9)


arvore.print_arvore("preorder")

