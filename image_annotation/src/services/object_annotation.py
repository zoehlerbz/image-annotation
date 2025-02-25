import os
import cv2
import logging

class ObjectAnnotation:
    def __init__(self, coordinates, img_path, threshold=0.7):
        self.coordinates = coordinates
        self.img_path = img_path
        self.threshold = threshold

    def run(self, class_index, output_imgs_path, output_infos_path):
        image = cv2.imread(self.img_path)
        if image is None:
            logging.error(f"Erro ao carregar imagem '{self.img_path}'. Pulando...")
            return
        
        for coordinate in self.coordinates:
            class_name, confidence, x1, y1, x2, y2, H, W = coordinate

            if confidence > self.threshold:
                self.location(image, class_name, confidence, x1, y1, x2, y2, output_imgs_path)
                self.annotation(x1, y1, x2, y2, H, W, output_infos_path, class_index)

    def location(self, image, class_name, confidence, x1, y1, x2, y2, output_imgs_path):
        try:
            x_center = ((x1 + x2) / 2)
            y_center = ((y1 + y2) / 2)

            cv2.line(image, (x1, int(y_center)), (x2, int(y_center)), (0, 255, 0), 2)
            cv2.line(image, (int(x_center), y1), (int(x_center), y2), (0, 255, 0), 2)
            cv2.putText(image, f"{class_name} {confidence:.2f}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Só salva a imagem se ao menos um objeto válido foi detectado
            output_path = os.path.join(output_imgs_path, os.path.basename(self.img_path))
            cv2.imwrite(output_path, image)

        except Exception as e:
            logging.error(f"Erro ao processar imagem '{self.img_path}': {e}")

    def annotation(self, x1, y1, x2, y2, H, W, output_infos_path, class_index):
        try:
            x_center = ((x1 + x2) / 2) / W  # Coordenada central de x normalizada
            y_center = ((y1 + y2) / 2) / H  # Coordenada central de y normalizada
            width = (x2 - x1) / W  # Largura normalizada
            height = (y2 - y1) / H  # Altura normalizada

            annotations = [class_index, x_center, y_center, width, height]

            output_path = os.path.join(output_infos_path, os.path.basename(self.img_path)).replace('.jpg', '.txt')
            with open(output_path, 'a') as f:
                f.write('\t'.join([str(a) for a in annotations]) + '\n')

        except Exception as e:
            logging.error(f"Erro ao anotar imagem '{self.img_path}': {e}")
