def shell_sort(data):
    n = len(data)
    gap = n // 2  # Inicializamos el intervalo (gap)

    # Reducimos el intervalo en cada iteración
    while gap > 0:
        for i in range(gap, n):
            # Guardamos el elemento actual
            temp = data[i]
            j = i

            # Comparamos y movemos los elementos en el intervalo
            while j >= gap and data[j - gap][1] < temp[1]:  # Orden descendente
                data[j] = data[j - gap]
                j -= gap

            # Colocamos el elemento en su posición correcta
            data[j] = temp

        # Reducimos el intervalo
        gap //= 2

    return data