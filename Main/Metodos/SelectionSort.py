def selection_sort(data):
    if not data:
        return data
    
    n = len(data)
    
    # Recorrer la lista
    for i in range(n - 1):
        # Encontrar el índice del elemento más grande en el resto de la lista
        max_index = i
        for j in range(i + 1, n):
            # Comparamos el segundo elemento de la tupla (el entero)
            # Buscamos el mayor (>) para ordenar de mayor a menor
            if data[j][1] > data[max_index][1]:
                max_index = j
        
        # Intercambiar el elemento más grande con el elemento en la posición actual
        if i != max_index:
            data[i], data[max_index] = data[max_index], data[i]
    
    return data