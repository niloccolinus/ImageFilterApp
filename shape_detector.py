import cv2
import math

class ShapeDetector:
    def __init__(self):
        pass

    # Fonction pour détecter et annoter des formes géométriques sur une image
    def detect_shapes(self, image_path):
        # charger l'image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"L'image '{image_path}' n'a pas été trouvée.")

        # convertir en niveaux de gris
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # appliquer un seuil pour obtenir une image binaire inversée
        _, thresh_image = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY_INV)

        # trouver les contours dans l'image
        contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # compteur de formes
        shapes_count = {"triangle": 0, "rectangle": 0, "square": 0, "quadrilateral": 0, "circle": 0, "polygon": 0}

        # couleurs et polices
        contour_color = (0, 255, 0)
        text_color = (0, 0, 0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # parcourir les contours
        for contour in contours:
            # approximation du contour pour simplifier la forme
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # calculer la boîte englobante (sert pour différencier rectangle et carré)
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)

            # calculer le cercle minimum englobant
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            circularity = (4 * math.pi * area) / (perimeter ** 2) if perimeter > 0 else 0

            # position pour annoter le texte
            coords = (x + w // 4, y + h // 2)

            # identifier la forme en comptant les aretes
            if len(approx) == 3:  # Triangle
                cv2.putText(image, "Triangle", coords, font, 0.6, text_color, 2)
                shapes_count["triangle"] += 1
            elif len(approx) == 4:  # Quadrilatère
                if 0.9 <= aspect_ratio <= 1.1:  # Carré
                    cv2.putText(image, "Square", coords, font, 0.6, text_color, 2)
                    shapes_count["square"] += 1
                elif self.is_rectangle(approx):  # Rectangle
                    cv2.putText(image, "Rectangle", coords, font, 0.6, text_color, 2)
                    shapes_count["rectangle"] += 1
                else:  # Autre quadrilatère
                    cv2.putText(image, "Quadrilateral", coords, font, 0.6, text_color, 2)
                    shapes_count["quadrilateral"] += 1
            elif circularity > 0.8:  # Cercle
                cv2.putText(image, "Circle", coords, font, 0.6, text_color, 2)
                shapes_count["circle"] += 1
            else:  # Autre polygone
                cv2.putText(image, "Polygon", coords, font, 0.6, text_color, 2)
                shapes_count["polygon"] += 1

            # Dessiner le contour
            cv2.drawContours(image, [approx], -1, contour_color, 2)

        return image, shapes_count

    # Fonction pour vérifier si un quadrilatère est un rectangle
    def is_rectangle(self, approx):
        if len(approx) == 4:
            # vérifier les anlges entre les sommets
            angles = []
            for i in range(4):
                pt1 = approx[i][0]
                pt2 = approx[(i + 1) % 4][0]
                pt3 = approx[(i + 2) % 4][0]

                v1 = (pt2[0] - pt1[0], pt2[1] - pt1[1])
                v2 = (pt3[0] - pt2[0], pt3[1] - pt2[1])

                dot_product = v1[0] * v2[0] + v1[1] * v2[1]
                norm1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
                norm2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)

                if norm1 > 0 and norm2 > 0:
                    angle = math.degrees(math.acos(dot_product / (norm1 * norm2)))
                    angles.append(angle)

            # vérifier si tous les angles sont proches de 90 degrés
            return all(80 <= angle <= 100 for angle in angles)
        return False
