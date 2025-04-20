# -*- coding: utf-8 -*-
"""BigTree_E1_Estructuras_JuanTorresNossa.py

  Por: Juan Daniel Torres - 2240082
       Sebastian Nossa - 2211555

  Estructuras de datos y Analisis de algoritmos - E1 - Profesora: Nury Farelo

"""

#pip install 'bigtree[all]' Esto se debe poner en consola (Si no es un notebook en collab)

from bigtree import Node, tree_to_dot
from bigtree import Node, reingold_tilford, plot_tree
import os

#Definir los nodos
root = A = Node("A", gen=1)
B = Node("B", parent=A, gen=2)
C = Node("C", parent=B, gen=3)
J = Node("J", parent=C, gen=4)
H = Node("H", parent=C, gen=4)
I = Node("I", parent=H, gen=5)
M = Node("M", parent=I, gen=6)
L = Node("L", parent=I, gen=6)
K = Node("K", parent=I, gen=6)
D = Node("D", parent=A, gen=2)
E = Node("E", parent=D, gen=3)
G = Node("G", parent=E, gen=4)
F = Node("F", parent=E, gen=4)

#Relaciones padre e hijos
A.children = [B, D]
B.children = [C]
C.children = [J, H]
H.children = [I]
I.children = [M, L, K]
D.children = [E]
E.children = [G, F]

root.show(attr_list=["gen"])
print()
print()
root.hshow(style="ansi")
print()
print()
root.vshow(style="double")
print()

reingold_tilford(root)
fig = plot_tree(root, "-ok")
fig.axes[0].set_title("Ejemplo usando funciones de la libreria (IMAGEN)")

fig.show()
print()

#Algunas funciones de la libreria
print(A.is_leaf) #Es una hoja?

print(B.is_leaf)

print(M.is_leaf)

print(F.is_leaf)

print(root.is_root) #Es la raiz?

print(A.is_root)

print(B.is_root)

print(root.max_depth)	#Altura?

print(M.root) #Raiz?

print(L.node_path) #Camino al nodo?

print(A.node_path)

print(G.node_path)

print(root.children) #Hijos?

print(M.children)

print(L.siblings)  # Hermanos?

print(B.siblings)

print(B.parent)  # Padre?

print(K.parent)  # Padre?

print(C.parent)  # Padre?

print(list(A.ancestors))  # Ancestros?

print(list(M.ancestors))

print(list(F.ancestors))

print(list(B.descendants))  # Descendientes?

print(list(M.descendants))

print(list(A.descendants))

print(list(A.leaves))  # Hojas?

print(list(I.leaves))

#También existen otras funciones para agregar nodos, copiar arboles, entre otros.
	#	root.append(Node("Z"))
  #	root.append(Node("X"))
  # root.extend([Node("V"), Node("N")])

#Copiar Árbol
P = root.copy()

P.vshow(style='double') #Podemos observar como se copio todo el árbol

from bigtree import Node, find, find_name, find_path, find_relative_path, find_full_path, find_attr
print(find_name(root, "I")) #Buscar un nodo y su camino a el

print(find_attr(root, "gen", 1)) #Esta funcion en especifico si encuentra mas de un nodo que cumpla con la condicion genera una excepcion (Probar con gen 2).

#Obtener subarboles

from bigtree import str_to_tree, get_subtree
root_subtree = get_subtree(root, "I")
root_subtree.show()

from bigtree import str_to_tree, get_subtree
root_subtree = get_subtree(root, "B")
root_subtree.show()

#Ver el arbol hasta una altura determinada y (o no) por un camino determinado:
from bigtree import prune_tree
root_pruned = prune_tree(root, "A", max_depth=4)
root_pruned.show()

from bigtree import prune_tree
root_pruned = prune_tree(root, "D", max_depth=4)
root_pruned.show()

P.extend([Node("V")]) #Modificar a la copia P para posteriormente hallar diferencias con el arbol original A
P.extend([Node("N")])
P.extend([Node("T")])

#Diferencias entre arboles
#Por ejemplo, modificaremos a P (Es una copia)

P.show()

from bigtree import get_tree_diff
tree_diff = get_tree_diff(A, P)
tree_diff.show()

#Podemos ver que los nodos N,T,V tienen un signo (+), esto quiere decir que la diferencia entre ambos arboles esque estos nodos son nuevos (No los tiene el arbol A que es el original)

#Algunos metodos para exportar arboles:

from bigtree import tree_to_pillow_graph

pillow_image = tree_to_pillow_graph(root, node_content="{node_name}\nGen {gen}")

from bigtree import tree_to_pillow

pillow_image = tree_to_pillow(root)

from bigtree import tree_to_mermaid

mermaid_md = tree_to_mermaid(root)
print(mermaid_md)

#Nota, si las imagenes no se ve, es debido a que falta una extension en VS Code o en el IDE que se este usando.
#Esto es especialmente cierto si se esta viendo desde una terminal pura.
