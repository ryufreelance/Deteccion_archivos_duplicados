import os
import hashlib
from concurrent.futures import ThreadPoolExecutor

def calcular_hash(archivo):
    sha256 = hashlib.sha256()
    try:
        with open(archivo, 'rb') as f:
            while True:
                bloque = f.read(4096)  # Leer bloques de 4 KB
                if not bloque:
                    break
                sha256.update(bloque)
    except IOError:  # Manejo de errores si un archivo no se puede leer
        return None
    return sha256.hexdigest()

def procesar_archivo(ruta_completa, hashes, progreso_actual, total_archivos):
    hash_archivo = calcular_hash(ruta_completa)
    if not hash_archivo:  # Si no se pudo calcular el hash, lo omitimos
        return None
    if hash_archivo in hashes:
        return (ruta_completa, hashes[hash_archivo])
    else:
        hashes[hash_archivo] = ruta_completa
    # Mostrar progreso
    progreso_actual[0] += 1
    porcentaje = (progreso_actual[0] / total_archivos) * 100
    print(f"Progreso: {porcentaje:.2f}% completado", end="\r")
    return None

def encontrar_duplicados(ruta, extensiones_relevantes=None):
    hashes = {}
    duplicados = []
    archivos_para_procesar = []

    # Recoger rutas relevantes
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            # Filtrar por extensiones si se especifica
            if extensiones_relevantes and not archivo.lower().endswith(extensiones_relevantes):
                continue
            ruta_completa = os.path.join(carpeta_actual, archivo)
            archivos_para_procesar.append(ruta_completa)

    total_archivos = len(archivos_para_procesar)
    progreso_actual = [0]  # Usamos una lista mutable para rastrear el progreso

    print(f"Total de archivos a analizar: {total_archivos}")

    # Procesar en paralelo
    with ThreadPoolExecutor() as executor:
        resultados = executor.map(
            lambda archivo: procesar_archivo(archivo, hashes, progreso_actual, total_archivos), 
            archivos_para_procesar
        )
        for resultado in resultados:
            if resultado:
                duplicados.append(resultado)

    # Mostrar duplicados encontrados
    print("\n")
    if duplicados:
        print("Archivos duplicados encontrados:")
        for duplicado, original in duplicados:
            print(f"- {duplicado} es duplicado de {original}")
        print(f"\nTotal de archivos duplicados encontrados: {len(duplicados)}")
    else:
        print("No se encontraron duplicados.")

# Ejemplo de uso
ruta_carpeta = r'C:\Users\TuUsuario\Carpeta'
extensiones = ('.jpg', '.png', '.jpeg', '.mp4', '.avi', '.mkv', '.heic')  # Solo imágenes y videos
encontrar_duplicados(ruta_carpeta, extensiones)
