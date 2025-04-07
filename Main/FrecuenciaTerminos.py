import json
import matplotlib.pyplot as plt
from tabulate import tabulate  
from Metodos.BinaryInsertionSort import binary_insertion_sort
from Metodos.BitonicSort import bitonic_sort
from Metodos.BucketSort import bucket_sort
from Metodos.CombSort import comb_sort
from Metodos.GnomeSort import gnome_sort
from Metodos.HeapSort import heap_sort
from Metodos.QuickSort import quick_sort
from Metodos.RadixSort import radix_sort
from Metodos.SelectionSort import selection_sort
from Metodos.TimSort import tim_sort
from Metodos.TreeSort import tree_sort
from Metodos.BubbleSort import bubble_sort 
from Metodos.BurbujaDobleDireccion import burbuja_doble_direccion 
from Metodos.ShellSort import shell_sort  
from Metodos.PigeonHoleSort import pigeonhole_sort
import time  

def extract_abstracts_from_json(file_path):
    abstracts = []

    try:
        # Abrir y leer el archivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Cargar el contenido del archivo JSON como una lista de objetos

            # Iterar por cada objeto en el JSON
            for obj in data:
                # Verificar si el campo "abstract" existe y no es nulo o vacío
                if "abstract" in obj and obj["abstract"]:
                    abstracts.append(obj["abstract"])  # Agregar el abstract a la lista

    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")

    return abstracts

def count_terms_occurrences(abstracts, terms):
    term_counts = {term.lower(): 0 for term in terms}  # Inicializar el contador para cada término

    # Iterar por cada abstract en la lista
    for abstract in abstracts:
        abstract_lower = abstract.lower()  # Convertir el abstract a minúsculas para comparación

        # Contar cuántas veces aparece cada término
        for term in terms:
            term_lower = term.lower()
            term_counts[term_lower] += abstract_lower.count(term_lower)

    return term_counts

def plot_term_frequencies(term_frequencies, execution_time_ms, algorithm_name):
    # Diagrama de barras
    terms = [term for term, _ in term_frequencies]
    frequencies = [freq for _, freq in term_frequencies]

    plt.figure(figsize=(10, 6))
    plt.barh(terms, frequencies, color='skyblue')
    plt.xlabel('Frecuencia')
    plt.ylabel('Términos')
    plt.title(f'{algorithm_name} ({execution_time_ms:.2f} ms)')
    plt.gca().invert_yaxis()  # Invertir el eje Y para mostrar el mayor primero
    plt.show()

def print_frequency_table(term_frequencies, algorithm_name):
    # Tabla usando tabulate
    print(f"\nTabla de frecuencias ordenada con {algorithm_name}:")
    table = [["Término", "Frecuencia"]]
    table.extend(term_frequencies)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

def measure_sorting_algorithm(algorithm, term_frequencies, algorithm_name):
    # Copiar los datos para no modificar la lista original
    data_copy = term_frequencies.copy()

    # Medir el tiempo de ejecución
    start_time = time.perf_counter()
    sorted_data = algorithm(data_copy)  # Ordenar las tuplas directamente
    end_time = time.perf_counter()

    # Calcular el tiempo en milisegundos
    execution_time_ms = (end_time - start_time) * 1000

    # Imprimir la tabla de frecuencias
    print_frequency_table(sorted_data, algorithm_name)

    # Generar el gráfico de barras
    plot_term_frequencies(sorted_data, execution_time_ms, algorithm_name)

def main():
    """
    Función principal del programa.
    """
    # Ruta al archivo JSON
    file_path = "C:/Users/Mary/Documents/7mo semestre/Analisis Algoritmos/AnalisisAlgoritmosMetodos/Main/ResultadosFiltrados.json"
    
    # Extraer los abstracts del archivo JSON
    abstracts = extract_abstracts_from_json(file_path)
    print(f"Se extrajeron {len(abstracts)} abstracts.")

    # Lista de términos a buscar
    terms = [
        "Abstraction", "Motivation", "Algorithm", "Persistence", "Coding", "Block",
        "Creativity", "Mobile application", "Logic", "Programming", "Conditionals",
        "Robotic", "Loops", "Scratch"
    ]

    # Contar las ocurrencias de los términos en los abstracts
    term_counts = count_terms_occurrences(abstracts, terms)

    # Convertir el diccionario en una lista de tuplas
    term_frequencies = list(term_counts.items())

    # Lista de algoritmos de ordenamiento
    algorithms = [
        (burbuja_doble_direccion, "BurbujaDobleDireccion"),
        (selection_sort, "SelectionSort"),
        (shell_sort, "ShellSort"),
        (tim_sort, "TimSort"),
        (comb_sort, "CombSort"),
        (tree_sort, "TreeSort"),
        (pigeonhole_sort, "PigeonholeSort"),
        (bucket_sort, "BucketSort"),
        (quick_sort, "QuickSort"),
        (heap_sort, "HeapSort"),
        (bitonic_sort, "BitonicSort"),
        (gnome_sort, "GnomeSort"),
        (binary_insertion_sort, "BinaryInsertionSort"),
        (radix_sort, "RadixSort"),
        (bubble_sort, "BubbleSort"),
    ]

    # Ejecutar cada algoritmo de ordenamiento
    for algorithm, algorithm_name in algorithms:
        measure_sorting_algorithm(algorithm, term_frequencies, algorithm_name)

# Ejecutar la función principal
if __name__ == "__main__":
    main()