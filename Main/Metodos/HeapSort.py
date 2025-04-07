def heap_sort(data):
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left][1] > data[largest][1]:  # Comparar por frecuencia
            largest = left
        if right < n and data[right][1] > data[largest][1]:  # Comparar por frecuencia
            largest = right
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            heapify(data, n, largest)

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data[::-1]  # Invertir para obtener orden descendente