import os
from ultralytics import YOLO

class ObjectDetection:
    def __init__(self, model, class_name):
        self.model = model
        self.class_name = class_name

    def run(self, img_path):
        if not isinstance(img_path, str) or not img_path:
            raise ValueError(f"O caminho da imagem '{img_path}' não é válido.")

        if not os.path.exists(img_path):
            print(f"Erro: O arquivo '{img_path}' não foi encontrado.")
            return []

        try:
            results = self.model(img_path)
            objects = []

            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])  # Classe detectada YOLO
                    class_yolo = self.model.names[class_id]

                    # Verifica se a classe detectada é a classe desejada
                    if class_yolo == self.class_name:
                        confidence = float(box.conf[0])  # Confiança da detecção
                        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas do bounding box
                        H, W = map(int, box.orig_shape)  # Altura e largura da imagem original

                        objects.append((class_yolo, confidence, x1, y1, x2, y2, H, W))
            return objects

        except Exception as e:
            print(f"Erro inesperado: {e}")
            return []