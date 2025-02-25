import logging
from image_annotation.src.services.object_annotation import ObjectAnnotation

class Annotate:
    def __init__(self, coordinates, output_imgs_path, output_infos_path, threshold=0.7):
        self.coordinates = coordinates
        self.output_imgs_path = output_imgs_path
        self.output_infos_path = output_infos_path
        self.threshold = threshold

    def run(self, img_path, class_index):
        try:
            Annotation = ObjectAnnotation(self.coordinates, img_path, self.threshold)
            Annotation.run(class_index, self.output_imgs_path, self.output_infos_path)
        except Exception as e:
            logging.error(f"Erro ao anotar a imagem '{img_path}': {e}")