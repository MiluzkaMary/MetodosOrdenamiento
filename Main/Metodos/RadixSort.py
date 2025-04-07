def radix_sort(data):
    if not data:
        return data
    
    # Encontrar el valor máximo para determinar el número de dígitos
    max_value = max(abs(item[1]) for item in data)
    
    # Si max_value es 0, no hay nada que ordenar
    if max_value == 0:
        return data
    
    # Determinar el número de dígitos en el número más grande
    max_digits = len(str(max_value))
    
    # Realizar el ordenamiento radix para cada posición de dígito
    # Comenzando desde el dígito menos significativo (unidades)
    placement = 1
    
    # Realizar el ordenamiento para cada posición de dígito
    for _ in range(max_digits):
        # Inicializar buckets (uno para cada dígito posible, 0-9)
        buckets = [[] for _ in range(10)]
        
        # Distribuir los elementos en los buckets según el dígito actual
        for item in data:
            # Calcular el dígito actual
            digit = (abs(item[1]) // placement) % 10
            buckets[digit].append(item)
        
        # Reconstruir la lista desde los buckets
        data = []
        for bucket in buckets:
            data.extend(bucket)
        
        # Avanzar a la siguiente posición decimal
        placement *= 10
    
    # Ahora invertimos la lista para obtener orden descendente (mayor a menor)
    data.reverse()
    
    
    return data