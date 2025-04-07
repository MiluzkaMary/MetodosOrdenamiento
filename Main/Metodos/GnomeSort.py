def gnome_sort(data):
    index = 0
    while index < len(data):
        if index == 0 or data[index][1] <= data[index - 1][1]:  # Comparar por frecuencia en orden descendente
            index += 1
        else:
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1
    return data