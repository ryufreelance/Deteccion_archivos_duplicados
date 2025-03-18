# Detección de Archivos Duplicados

Este programa permite identificar y gestionar archivos duplicados en una carpeta específica y sus subcarpetas, analizando su contenido mediante un cálculo de hash criptográfico (SHA-256). Es útil para liberar espacio y organizar el almacenamiento eliminando archivos redundantes.

## Características

- **Cálculo de Hash**: Usa el algoritmo SHA-256 para asegurar una comparación precisa de los archivos.
- **Compatibilidad con Extensiones**: Posibilidad de especificar extensiones relevantes como imágenes, videos, etc.
- **Procesamiento en Paralelo**: Mejora el rendimiento utilizando múltiples hilos con `ThreadPoolExecutor`.
- **Progreso Visual**: Muestra el porcentaje de progreso durante el análisis.

## Requisitos Previos

- Python 3.x instalado en el sistema.
- Módulos estándar de Python (`os`, `hashlib`, `concurrent.futures`).

## Cómo Usar

1. Clona o descarga este repositorio en tu máquina.
2. Ejecuta el script `detectar_archivos_duplicados.py` especificando el directorio objetivo y, opcionalmente, las extensiones relevantes.

### Ejemplo de Uso

```python
ruta_carpeta = r'C:\Users\TuUsuario\Carpeta'
extensiones = ('.jpg', '.png', '.jpeg', '.mp4', '.avi', '.mkv', '.heic')  # Especificar extensiones
encontrar_duplicados(ruta_carpeta, extensiones)
