def pigeonhole_sort(data):
    if not data:
        return data

    # Encontrar el valor mínimo y máximo en las frecuencias
    min_val = min(data, key=lambda x: x[1])[1]
    max_val = max(data, key=lambda x: x[1])[1]

    # Determinar el rango (número de "agujeros")
    range_size = max_val - min_val + 1

    # Crear los "agujeros" (listas vacías)
    pigeonholes = [[] for _ in range(range_size)]

    # Colocar las tuplas en sus respectivos "agujeros"
    for term, freq in data:
        index = max_val - freq  # Invertir el índice para orden descendente
        pigeonholes[index].append((term, freq))

    # Recoger las tuplas ordenadas de los "agujeros"
    sorted_data = []
    for hole in pigeonholes:
        sorted_data.extend(hole)

    return sorted_data