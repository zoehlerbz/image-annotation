import os
import cv2

class ObjectLocation:
    def __init__(self, coordinates, output_imgs_path, threshold=0.7):
        self.coordinates = coordinates
        self.output_imgs_path = output_imgs_path
        self.threshold = threshold

    def run(self, img_path):
        try:
            image = cv2.imread(img_path)
            for coordinate in self.coordinates:
                class_name, confidence, x1, y1, x2, y2, H, W = coordinate

                if confidence < self.threshold:
                    continue

                # Se há pelo menos um objeto válido, a imagem deve ser salva
                save_image = True

                x_center = ((x1 + x2) / 2)
                y_center = ((y1 + y2) / 2)

                cv2.line(image, (x1, int(y_center)), (x2, int(y_center)), (0, 255, 0), 2)
                cv2.line(image, (int(x_center), y1), (int(x_center), y2), (0, 255, 0), 2)
                cv2.putText(image, f"{class_name} {confidence:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Só salva a imagem se ao menos um objeto válido foi detectado
                if save_image:
                    output_path = os.path.join(self.output_imgs_path, os.path.basename(img_path))
                    cv2.imwrite(output_path, image)

        except Exception as e:
            print(f"Erro: {e}")