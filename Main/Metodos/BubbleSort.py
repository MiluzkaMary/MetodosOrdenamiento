def bubble_sort(data):
    n = len(data)
    for i in range(n):
        # Banderín para optimización: si no hay intercambios, la lista ya está ordenada
        swapped = False
        for j in range(0, n - i - 1):
            # Comparar el segundo elemento de las tuplas (frecuencia)
            if data[j][1] < data[j + 1][1]:  # Orden descendente
                # Intercambiar las tuplas
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not swapped:
            break
    return data