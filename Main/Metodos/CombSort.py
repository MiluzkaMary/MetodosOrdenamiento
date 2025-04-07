def comb_sort(data):
    gap = len(data)
    shrink = 1.3
    sorted_flag = False

    while gap > 1 or not sorted_flag:
        gap = max(1, int(gap / shrink))
        sorted_flag = True
        for i in range(len(data) - gap):
            if data[i][1] < data[i + gap][1]:  # Comparar por frecuencia en orden descendente
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted_flag = False

    return data