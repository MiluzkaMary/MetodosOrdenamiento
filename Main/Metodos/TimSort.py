def tim_sort(data):
    if not data or len(data) <= 1:
        return data
    
    # Hacemos una copia para no modificar la entrada original
    result = data.copy()
    n = len(result)
    
    # Tamaño mínimo de sublistas para aplicar ordenamiento por inserción
    RUN = 32
    
    # Aplicamos InsertionSort en sublistas de tamaño RUN
    for i in range(0, n, RUN):
        insertion_sort(result, i, min(i + RUN - 1, n - 1))
    
    # Fusionamos sublistas ordenadas, duplicando el tamaño en cada iteración
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(result, left, mid, right)
        size = 2 * size
    
    return result

def insertion_sort(data, left, right):
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        # Comparamos el segundo elemento de la tupla (el entero)
        while j >= left and data[j][1] < key[1]:  # Cambiado para mayor a menor
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def merge(data, left, mid, right):
    # Creamos copias de las sublistas
    left_sublist = data[left:mid + 1]
    right_sublist = data[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Mezclamos las sublistas en orden descendente de enteros
    while i < len(left_sublist) and j < len(right_sublist):
        if left_sublist[i][1] >= right_sublist[j][1]:  # Cambiado para mayor a menor
            data[k] = left_sublist[i]
            i += 1
        else:
            data[k] = right_sublist[j]
            j += 1
        k += 1
    
    # Copiamos los elementos restantes de left_sublist, si hay alguno
    while i < len(left_sublist):
        data[k] = left_sublist[i]
        i += 1
        k += 1
    
    # Copiamos los elementos restantes de right_sublist, si hay alguno
    while j < len(right_sublist):
        data[k] = right_sublist[j]
        j += 1
        k += 1