# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os

def pregunta_01():
    """
    Genera "train_dataset.csv" y "test_dataset.csv" en "files/output"
    a partir de la estructura de archivos ya descomprimida.
    """
    directorio_origen = "input" # La carpeta ya existente con los datos descomprimidos

    # Crear la carpeta de salida si no existe
    ruta_salida = "files/output"
    os.makedirs(ruta_salida, exist_ok=True)

    # Diccionario para almacenar los datos de cada conjunto (train y test)
    conjuntos = {
        "train": [],
        "test": []
    }

    # Recorrer la estructura de directorios: train/test -> negative/positive/neutral -> archivos .txt
    for tipo_conjunto in ["train", "test"]:
        ruta_base_tipo = os.path.join(directorio_origen, tipo_conjunto)
        for sentimiento in ["negative", "positive", "neutral"]:
            ruta_sentimiento = os.path.join(ruta_base_tipo, sentimiento)
            
            # Verificar si la ruta del sentimiento existe antes de intentar listar su contenido
            if os.path.exists(ruta_sentimiento):
                for nombre_archivo_txt in os.listdir(ruta_sentimiento):
                    # Procesar solo archivos .txt
                    if nombre_archivo_txt.endswith(".txt"):
                        ruta_completa_txt = os.path.join(ruta_sentimiento, nombre_archivo_txt)
                        with open(ruta_completa_txt, 'r', encoding='utf-8') as f:
                            frase = f.read().strip()
                            # Añadir la frase y su sentimiento al conjunto correspondiente
                            conjuntos[tipo_conjunto].append({'phrase': frase, 'sentiment': sentimiento})

    # Escribir los archivos CSV
    for tipo_conjunto, datos in conjuntos.items():
        nombre_archivo_csv = f"{tipo_conjunto}_dataset.csv"
        ruta_csv_salida = os.path.join(ruta_salida, nombre_archivo_csv)
        
        with open(ruta_csv_salida, 'w', encoding='utf-8') as archivo_csv:
            # Escribir la fila de encabezado
            archivo_csv.write("phrase,sentiment\n")
            
            # Escribir cada fila de datos
            for fila in datos:
                # Limpiar la frase para evitar problemas con comas o saltos de línea dentro del CSV
                frase_limpia = fila['phrase'].replace('\n', ' ').replace('\r', ' ').replace('"', '""')
                # Envolver la frase entre comillas dobles para manejar comas internas si las hubiera
                archivo_csv.write(f'"{frase_limpia}",{fila["sentiment"]}\n')
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