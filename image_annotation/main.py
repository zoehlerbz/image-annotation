import os
import logging
import pandas as pd
from ultralytics import YOLO
from image_annotation.src.services.object_detection import ObjectDetection
from image_annotation.src.controllers.annotate import Annotate

class App:
    def __init__(self, input_path, output_imgs_path, output_infos_path, imgs_dataframe):
        self.input_path = input_path
        self.output_imgs_path = output_imgs_path
        self.output_infos_path = output_infos_path
        self.imgs_dataframe = imgs_dataframe
        self.model = YOLO("yolo11n.pt")

    def run(self, class_name="bird"):
        logging.info("Iniciando anotações...")

        for _, row in self.imgs_dataframe.iterrows():
            img_path = os.path.join(self.input_path, row['img_name'])

            if not os.path.exists(img_path):
                logging.warning(f"Imagem '{img_path}' não encontrada. Pulando...")
                continue

            try:
                detection = ObjectDetection(self.model, class_name)
                coordinates = detection.run(img_path)

                annotation = Annotate(coordinates, self.output_imgs_path, self.output_infos_path, threshold=0.6)
                annotation.run(img_path, row['class'])

            except Exception as e:
                logging.error(f"Erro ao processar '{img_path}': {e}")

        logging.info("Anotações concluídas.")