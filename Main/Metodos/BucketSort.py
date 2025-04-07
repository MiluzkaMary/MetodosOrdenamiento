def bucket_sort(data):
    if not data:
        return data
    
    # Encontrar el máximo y mínimo valor para determinar el rango
    max_val = max(item[1] for item in data)
    min_val = min(item[1] for item in data)
    
    # Si todos los elementos tienen el mismo valor, no hay necesidad de ordenar
    if max_val == min_val:
        return data

    # Calcula el número de buckets basado en el tamaño de los datos
    bucket_count = min(len(data), max_val - min_val + 1)
    
    # Crear los buckets (listas vacías)
    buckets = [[] for _ in range(bucket_count)]
    
    # Colocar cada elemento en su bucket correspondiente
    bucket_size = (max_val - min_val) / bucket_count + 1
    for item in data:
        # Calcular el índice del bucket al que pertenece el elemento
        # Usar floor division para obtener un índice entero
        index = int((item[1] - min_val) / bucket_size)
        # Asegurarnos de que el índice está dentro del rango válido
        index = min(index, bucket_count - 1)
        buckets[index].append(item)
    
    # Ordenar cada bucket individualmente (usando sort con una función clave)
    for bucket in buckets:
        bucket.sort(key=lambda x: x[1], reverse=True)
    
    # Reconstruir la lista ordenada, de mayor a menor
    result = []
    for i in range(bucket_count - 1, -1, -1):  # Recorrer buckets en orden inverso
        result.extend(buckets[i])
    
    return result