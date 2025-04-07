def burbuja_doble_direccion(data):
    n = len(data)
    if n <= 1:
        return data

    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Recorrido de izquierda a derecha
        for i in range(start, end):
            if data[i][1] < data[i + 1][1]:  # Comparar por frecuencia (orden descendente)
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break

        # Reducir el rango del recorrido
        end -= 1
        swapped = False

        # Recorrido de derecha a izquierda
        for i in range(end, start, -1):
            if data[i - 1][1] < data[i][1]:  # Comparar por frecuencia (orden descendente)
                data[i], data[i - 1] = data[i - 1], data[i]
                swapped = True

        # Incrementar el rango del recorrido
        start += 1

    return data