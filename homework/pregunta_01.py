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
    directorio_origen = "files/input" 

    os.makedirs("files/output", exist_ok=True)

    conjuntos = {
        "train": [],
        "test": []
    }

    for tipo_conjunto in ["train", "test"]:
        ruta_base_tipo = f"{directorio_origen}/{tipo_conjunto}"
        for sentimiento in ["negative", "positive", "neutral"]:
            ruta_sentimiento = f"{ruta_base_tipo}/{sentimiento}"
            
            if os.path.exists(ruta_sentimiento):
                for nombre_archivo_txt in os.listdir(ruta_sentimiento):
                    if nombre_archivo_txt.endswith(".txt"):
                        ruta_completa_txt = f"{ruta_sentimiento}/{nombre_archivo_txt}"
                        with open(ruta_completa_txt, 'r', encoding='utf-8') as f:
                            frase = f.read().strip()
                            conjuntos[tipo_conjunto].append({'phrase': frase, 'sentiment': sentimiento})

    for tipo_conjunto, datos in conjuntos.items():
        nombre_archivo_csv = f"{tipo_conjunto}_dataset.csv"
        ruta_csv_salida = f"files/output/{nombre_archivo_csv}"
        
        with open(ruta_csv_salida, 'w', encoding='utf-8') as archivo_csv:
            archivo_csv.write("phrase,target\n")
            
            for fila in datos:
                frase_limpia = fila['phrase'].replace('\n', ' ').replace('\r', ' ').replace('"', '""')
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