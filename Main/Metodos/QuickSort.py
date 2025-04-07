def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][1]  # Usar la frecuencia como pivote
    left = [x for x in data if x[1] > pivot]
    middle = [x for x in data if x[1] == pivot]
    right = [x for x in data if x[1] < pivot]
    return quick_sort(left) + middle + quick_sort(right)