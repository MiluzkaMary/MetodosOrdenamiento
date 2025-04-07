def tree_sort(data):
    class Node:
        def __init__(self, item):
            self.data = item
            self.left = None
            self.right = None

    def insert(root, data):
        if root is None:
            return Node(data)
        if data[1] < root.data[1]:  # Comparar por frecuencia
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root

    def reverse_inorder_traversal(root, result):
        if root is not None:
            reverse_inorder_traversal(root.right, result)
            result.append(root.data)
            reverse_inorder_traversal(root.left, result)

    # Construir el árbol binario de búsqueda
    root = None
    for item in data:
        root = insert(root, item)

    # Realizar un recorrido en orden inverso para obtener los datos ordenados
    sorted_data = []
    reverse_inorder_traversal(root, sorted_data)
    return sorted_data