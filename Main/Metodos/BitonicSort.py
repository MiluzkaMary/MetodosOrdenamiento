def bitonic_sort(data, ascending=False):
    def bitonic_merge(data, low, count, ascending):
        if count > 1:
            mid = count // 2
            for i in range(low, low + mid):
                if (data[i][1] > data[i + mid][1]) == ascending:
                    data[i], data[i + mid] = data[i + mid], data[i]
            bitonic_merge(data, low, mid, ascending)
            bitonic_merge(data, low + mid, mid, ascending)

    def bitonic_sort_helper(data, low, count, ascending):
        if count > 1:
            mid = count // 2
            bitonic_sort_helper(data, low, mid, True)  # Orden ascendente
            bitonic_sort_helper(data, low + mid, count - mid, False)  # Orden descendente
            bitonic_merge(data, low, count, ascending)

    # Asegurarse de que el tamaño de la lista sea una potencia de 2
    n = len(data)
    while n & (n - 1) != 0:  # Si no es potencia de 2
        data.append((None, float('-inf')))  # Rellenar con valores mínimos
        n += 1

    bitonic_sort_helper(data, 0, len(data), ascending)

    # Eliminar los valores de relleno
    return [x for x in data if x[0] is not None]