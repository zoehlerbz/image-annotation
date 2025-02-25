import os
import pandas as pd
from image_annotation.main import App

BASE = os.getcwd()
INPUT_PATH = os.path.join(BASE, "image_annotation", "data", "raw")  # Caminho para o DIRETÓRIO de imagens de entrada
OUTPUT_IMGS_PATH = os.path.join(BASE, "image_annotation", "data", "processed")  # Caminho para o DIRETÓRIO de imagens de saída
OUTPUT_INFOS_PATH = os.path.join(BASE, "image_annotation", "data", "annotation")  # Caminho para o DIRETÓRIO de anotações

labels = pd.read_csv(os.path.join(BASE, "image_annotation", "data", "imgs_labels.csv"))  # Relação label -> nome do arquivo

def main():
    app = App(INPUT_PATH, OUTPUT_IMGS_PATH, OUTPUT_INFOS_PATH, labels)
    app.run()

if __name__ == "__main__":
    main()