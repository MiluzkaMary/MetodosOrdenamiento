# Proyecto Análisis de Algoritmos - Frecuencia de Términos

Este proyecto analiza y ordena la frecuencia de términos específicos encontrados en un conjunto de abstracts extraídos de un archivo JSON. Utiliza múltiples algoritmos de ordenamiento para comparar su rendimiento.

## Requisitos previos

1. **Instalar Python**: Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Configuración del entorno virtual

1. **Crear un entorno virtual**:
    ```sh
    python -m venv env
    ```

2. **Activar el entorno virtual**:

    - En Command Prompt:
        ```sh
        env\Scripts\activate.bat
        ```
3. **Instalar dependencias**:

    Instala las dependencias dentro del entorno virtual:
    ```txt
    matplotlib
    tabulate
    ```

## Ejecución del proyecto

1. **Preparar el archivo JSON**:
    Asegúrate de que el archivo `ResultadosFiltrados.json` se encuentre en la ruta esperada.

2. **Ejecutar el script principal**:
    ```sh
    python Main\FrecuenciaTerminos.py
    ```

- Los resultados de cada algoritmo de ordenamiento se mostrarán en la consola como tablas y gráficos de barras.

## Algoritmos de Ordenamiento Implementados

El proyecto incluye los siguientes algoritmos de ordenamiento:

1. Burbuja Doble Dirección
2. Selection Sort
3. Shell Sort
4. Tim Sort
5. Comb Sort
6. Tree Sort
7. Pigeonhole Sort
8. Bucket Sort
9. Quick Sort
10. Heap Sort
11. Bitonic Sort
12. Gnome Sort
13. Binary Insertion Sort
14. Radix Sort
15. Bubble Sort

## Autor

- **Nombre del Estudiante:** Mary Saire
- **Curso:** Análisis de Algoritmos
- **Profesor:** Sergio Cardona

---