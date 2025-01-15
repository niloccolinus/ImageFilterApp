from PIL import Image

class ImageFilter:
    def __init__(self, name, intensity = 0.0):
        self.name = name
        self.intensity = intensity

    # Méthode abstraite pour appliquer le filtre
    # Elle retourne l'image modifiée
    def apply(self, image, intensity):
        raise NotImplementedError("The apply method must be implemented in subclasses.")
