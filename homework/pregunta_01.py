# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import csv
import re

def pregunta_01():
    """
    Genera "train_dataset.csv" y "test_dataset.csv" en "files/output"
    a partir de la estructura de archivos ya descomprimida.
    Utiliza el módulo csv para la escritura robusta y limpia las frases
    agresivamente para asegurar compatibilidad.
    """
    # Esta es la ruta donde se espera que se encuentre la carpeta 'input'
    # después de la descompresión, dentro de 'files'.
    directorio_origen = "files/input" 

    # Crea la carpeta de salida si no existe
    os.makedirs("files/output", exist_ok=True)

    # Diccionario para almacenar las frases y sus sentimientos
    conjuntos = {
        "train": [],
        "test": []
    }

    # Patrón de expresión regular para limpiar las frases:
    # 1. Reemplaza cualquier secuencia de uno o más espacios (incluyendo saltos de línea) con un solo espacio.
    # 2. Elimina cualquier carácter que no sea alfanumérico, espacio, o puntuación básica común.
    patron_limpieza_frase = re.compile(r'[^a-zA-Z0-9\s.,!?;:\'"`-()&@#$%/+*=<>[]{}|~]')

    # Recorre los tipos de conjunto (train/test)
    for tipo_conjunto in ["train", "test"]:
        ruta_base_tipo = os.path.join(directorio_origen, tipo_conjunto)
        
        # Recorre los sentimientos (negative/positive/neutral)
        for sentimiento in ["negative", "positive", "neutral"]:
            ruta_sentimiento = os.path.join(ruta_base_tipo, sentimiento)
            
            # Verifica si la carpeta de sentimiento existe
            if os.path.exists(ruta_sentimiento):
                # Recorre los archivos de texto dentro de la carpeta de sentimiento
                for nombre_archivo_txt in os.listdir(ruta_sentimiento):
                    if nombre_archivo_txt.endswith(".txt"):
                        ruta_completa_txt = os.path.join(ruta_sentimiento, nombre_archivo_txt)
                        
                        # Abre y lee el contenido del archivo de texto
                        with open(ruta_completa_txt, 'r', encoding='utf-8') as f:
                            frase_original = f.read()
                            
                            # Limpieza de la frase:
                            # 1. Normaliza los espacios (múltiples a uno, elimina al inicio/fin).
                            frase_limpia = re.sub(r'\s+', ' ', frase_original).strip()
                            # 2. Elimina caracteres no deseados para asegurar compatibilidad CSV.
                            frase_limpia = patron_limpieza_frase.sub('', frase_limpia)

                            # Añade la frase limpia y su sentimiento al conjunto correspondiente
                            conjuntos[tipo_conjunto].append({'phrase': frase_limpia, 'sentiment': sentimiento})

    # Escribe los datasets (train y test) en archivos CSV
    for tipo_conjunto, datos in conjuntos.items():
        nombre_archivo_csv = f"{tipo_conjunto}_dataset.csv"
        ruta_csv_salida = os.path.join("files/output", nombre_archivo_csv)
        
        # Abre el archivo CSV para escritura. 'newline='''' es crucial para evitar
        # problemas de doble salto de línea en algunos sistemas operativos.
        with open(ruta_csv_salida, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Crea un escritor de CSV que maneja comas como delimitadores,
            # comillas dobles para citar campos y cita solo cuando es necesario.
            escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Escribe la fila de encabezado
            escritor_csv.writerow(["phrase", "target"])
            
            # Escribe cada fila de datos
            for fila in datos:
                # El módulo csv.writer se encarga automáticamente de poner comillas
                # y escapar las comillas internas en la frase si es necesario.
                escritor_csv.writerow([fila['phrase'], fila['sentiment']])
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

pregunta_01()