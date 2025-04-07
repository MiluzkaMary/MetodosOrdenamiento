def binary_insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        low, high = 0, i - 1

        # Búsqueda binaria para encontrar la posición correcta
        while low <= high:
            mid = (low + high) // 2
            if data[mid][1] < key[1]:  # Comparar por frecuencia (índice 1 de la tupla)
                high = mid - 1
            else:
                low = mid + 1

        # Insertar el elemento en la posición correcta
        data = data[:low] + [key] + data[low:i] + data[i + 1:]

    return data